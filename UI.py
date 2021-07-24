import tkinter as tk
from PIL import ImageGrab
from prediction import prediction

window = tk.Tk()

window.title('UI')

v = tk.StringVar()
text = tk.Label(window, width=20, textvariable= v, font=('Arial', 20), height=1)
text.pack()

canvas = tk.Canvas(window,width = 512,height = 512,bg='white')
canvas.pack()


def paint(event):
        x1, y1 = (event.x - 3), (event.y - 3)
        x2, y2 = (event.x + 3), (event.y + 3)
        canvas.create_oval(x1, y1, x2, y2, fill='black')
        #canvas.create_oval(x1, y1, x2, y2)

canvas.bind("<B1-Motion>", paint)

def submit():
    x = window.winfo_rootx() + canvas.winfo_x() + 2
    y = window.winfo_rooty() + canvas.winfo_y() + 2
    x1 = x + canvas.winfo_width() - 4
    y1 = y + canvas.winfo_height() - 4
    ImageGrab.grab().crop((x, y, x1, y1)).save("result.jpg")
    final = prediction("result.jpg")
    v.set(final)
    print(final)

def clear():
    canvas.delete("all")

def save():
    x = window.winfo_rootx() + canvas.winfo_x() + 2
    y = window.winfo_rooty() + canvas.winfo_y() + 2
    x1 = x + canvas.winfo_width() - 4
    y1 = y + canvas.winfo_height() - 4
    ImageGrab.grab().crop((x, y, x1, y1)).save("temp.jpg")


submit_bt = tk.Button(window, text='submit', font=('Arial', 18), width=10, height=1, command = submit)
submit_bt.pack(side='left')

claer_bt = tk.Button(window, text='claer', font=('Arial', 18), width=10, height=1, command = clear)
claer_bt.pack(side='left')

save_bt = tk.Button(window, text='save', font=('Arial', 18), width=10, height=1, command = save)
save_bt.pack(side='left')

window.mainloop()
from glob import glob
import os
import cv2

paths = glob(os.path.join('train/*/','*'))

for path in paths:
    img = cv2.imread(path)

    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img,(512,512))

    cv2.imwrite(path,img)
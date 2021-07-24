import os
import torch
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
from PIL import Image
import numpy as np
from torchvision import transforms,datasets,models
import matplotlib.pyplot as plt
from torch import nn
import torch.optim as optim
from torchvision.io import read_image

class Ani_dataset(Dataset):
    def __init__(self,img_path):
        self.img_path = img_path
        #self.name
        print(self.img_path)

    def __getitem__(self, item):
        image = read_image(path=self.img_path)

        return image

    def __len__(self):
        return 1

def prediction(img_path):
    classes = ('cat', 'dog', 'elephant')
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    test_dataset = Ani_dataset(img_path)
    test_loader = torch.utils.data.DataLoader(dataset=test_dataset,
                                               batch_size=1)

    net = models.resnet18()
    net.to(device=device)
    net.load_state_dict(torch.load('best_model.pth', map_location=device))

    pre_final = ''

    for data in test_loader:
        images = data
        images = images.to(device=device, dtype=torch.float32)

        outputs = net(images)
        _, predicted = torch.max(outputs.data, 1)
        _, predictions = torch.max(outputs, 1)

        #print(classes[labels],'Pre = ',classes[predicted])
        #imshow(torchvision.utils.make_grid(images))
        pre_final = classes[predictions]
        #print(predicted,predictions)

    return pre_final

if __name__ == "__main__":
    final = prediction('temp.jpg')

    print(final)
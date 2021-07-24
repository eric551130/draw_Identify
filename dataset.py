import os
import torch
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
from PIL import Image
import numpy as np
from torchvision import transforms,datasets
import matplotlib.pyplot as plt

def imshow(img):
    #img = img / 2 + 0.5     # unnormalize
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1, 2, 0)),cmap='gray')

    plt.show()

if __name__ == "__main__":

    transform = transforms.Compose([
        #transforms.RandomResizedCrop(256),
        transforms.RandomHorizontalFlip(),
        transforms.Grayscale(),
        transforms.ToTensor(),
    ])

    Animal_dataset = datasets.ImageFolder('train\\',transform = transform)

    print(Animal_dataset.class_to_idx)
    print(Animal_dataset.imgs)

    print(len(Animal_dataset))
    #imshow(Animal_dataset[5][0])
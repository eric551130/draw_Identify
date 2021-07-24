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

def train_net(net, device, data_path, epochs=50, batch_size=1, lr=0.0001):
    transform = transforms.Compose([
        #transforms.RandomResizedCrop(256),
        transforms.RandomHorizontalFlip(),
        #transforms.Grayscale(),
        transforms.ToTensor(),
    ])

    Animal_dataset = datasets.ImageFolder('train\\', transform=transform)
    train_loader = DataLoader(dataset=Animal_dataset,batch_size=batch_size,shuffle=True)

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr=lr, momentum=0.9)

    best_loss = float('inf')  # 正無窮

    print('img size =', len(Animal_dataset))
    for epoch in range(epochs):  # loop over the dataset multiple times

        running_loss = 0.0
        correct = 0
        total = 0

        for i, data in enumerate(train_loader, 0):
            # get the inputs
            inputs, labels = data

            # zero the parameter gradients
            optimizer.zero_grad()
            inputs = inputs.to(device=device, dtype=torch.float32)
            labels = labels.to(device=device)
            #print(type(inputs), type(labels))

            # forward + backward + optimize
            outputs = net(inputs)
            loss = criterion(outputs, labels)
            _, predicted = torch.max(outputs.data, 1)

            # print statistics
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
            running_loss += loss.item()
            if i % 50 == 49:
                print('[%d, %5d] loss: %.8f' %(epoch + 1, i + 1, loss.item()))
                running_loss = 0.0

            if loss < best_loss:
                best_loss = loss
                PATH = './best_model.pth'
                torch.save(net.state_dict(), PATH)

            loss.backward()
            optimizer.step()

        print('epoch :',epoch+1,', Accuracy of the network on the train images: %d %%' % (100 * correct / total))

    print('Finished Training')



if __name__ == "__main__":
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(torch.cuda.is_available() )

    resnet18 = models.resnet18()

    resnet18 = resnet18.cuda()
    #summary(net.cuda(), (1, 512, 512))

    data_path = "train/"
    train_net(resnet18, device, data_path)
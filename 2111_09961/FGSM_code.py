import numpy as np
import torch
import torchvision
import torchvision.transforms as transforms

from  torch.utils.data import DataLoader

MyTransforms=transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5))]
)
trainset = torchvision.datasets.CIFAR10(root='./2111_09961/data', train=True,
                                        download=True, transform=MyTransforms)
trainloader = DataLoader(trainset, batch_size=4,
                                          shuffle=True, num_workers=2)

testset = torchvision.datasets.CIFAR10(root='./2111_09961/data', train=False,
                                       download=True, transform=MyTransforms)
testloader = DataLoader(testset, batch_size=4,
                                         shuffle=False, num_workers=2)

classes = ('plane', 'car', 'bird', 'cat',
           'deer', 'dog', 'frog', 'horse', 'ship', 'truck')


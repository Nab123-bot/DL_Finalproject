import os
from torchvision import datasets, transforms

os.makedirs("../images", exist_ok=True)
transform = transforms.Compose([transforms.ToTensor()])
datasets.MNIST("../data", train=True, download=True, transform=transform)
print("Images MNIST prêtes (non générées, mais disponibles via torchvision).")
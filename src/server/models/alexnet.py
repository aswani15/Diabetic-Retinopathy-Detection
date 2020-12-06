from torch import load
import cv2
from torch import tensor
import torchvision.transforms as transforms
from torch import no_grad
from numpy import argmax

class AlexNetModel(object):
    def __init__(self, model_path):
        self.model = load(model_path)
        self.model.eval()

    def predict(self, image_path):
        # read the image as grayscale 
        img = cv2.imread(image_path, 0)
        img = cv2.resize(img, (224, 224))
        

        
        trans = transforms.Compose([transforms.ToTensor(), transforms.Normalize(
                                                              mean=[0.456],
                                                              std= [0.225])])
        img = trans(img)

        out = self.model(img.unsqueeze_(0))

        y_pred = out.data.max(1, keepdim=True)[1].int()
        out.detach()
        return y_pred.item()

    def __str__(self):
        return str(self.model)


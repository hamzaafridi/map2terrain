from PIL import Image
import numpy as np
from os import listdir
from os.path import isfile, join


class Utility:
    
    @staticmethod
    def img2numpy(path):
        img = Image.open(path)
        img.load()
        return np.asarray(img,dtype="int32")
    
    @staticmethod
    def flating(img):
        flat_img = np.empty((0,3), int)
        for i in range(img.shape[0]):
            flat_img = np.append(flat_img,img[i],axis=0)
        return flat_img
    
    @staticmethod
    def listoffiles(path):
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
        return onlyfiles

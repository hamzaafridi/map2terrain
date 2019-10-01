from PIL import Image
import numpy as np

class Utility:
    @staticmethod
    def img2numpy(path):
        img = Image.open(path)
        img.load()
        return np.asarray(img,dtype="int32")
    
    @staticmethod
    def flating(img):
        flat_img = np.empty((0,3), int)
        for i in range(im.shape[0]):
            flat_img = np.append(flat_img,im2[i],axis=0)
        return flat_img
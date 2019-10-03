import sys
sys.path.append("../../")
from classes.utility import Utility
import pandas as pd

class Map2Terrain:
    def __init__(self,dataDirPath):
        self.datapath = dataDirPath
    
    def prepareData(self):
        columns = ["Ri","Gi", "Bi", "Ro", "Go", "Bo"]
        self.imgdf = pd.DataFrame(columns=columns)
        for img in Utility.listoffiles(self.datapath):
           RGBin = Utility.flating(Utility.img2numpy(self.datapath+img)[:,:512,:])
           RGBout = Utility.flating(Utility.img2numpy(self.datapath+img)[:,512:,:])
           data = []
           df = pd.DataFrame(data = )
           
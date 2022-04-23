from PIL import Image
import numpy as np
import pandas as pd
import cv2

class Pd2Img:
    def __init__(self, path):
        self.df = self.image_to_pandas(path)
        self.mode = None
        self.maxlen = self.df.x.max()
    def image_to_pandas(self, imagepath):
        colourImg = Image.open(imagepath)
        self.mode = colourImg.mode
        if self.mode != 'RGBA' and self.mode !='RGB':
            colourImg = colourImg.convert("RGB")
            self.mode = 'RGB'
        if self.mode == "RGB":
            colourArray = np.array(colourImg.getdata()).reshape(colourImg.size + (3,))
            indicesArray = np.moveaxis(np.indices(colourImg.size), 0, 2)
            allArray = np.dstack((indicesArray, colourArray)).reshape((-1, 5))
            return pd.DataFrame(allArray, columns=["y", "x", "red", "green", "blue"])
        if self.mode == "RGBA":
            colourArray = np.array(colourImg.getdata()).reshape(colourImg.size + (4,))
            indicesArray = np.moveaxis(np.indices(colourImg.size), 0, 2)
            allArray = np.dstack((indicesArray, colourArray)).reshape((-1, 6))
            return pd.DataFrame(allArray, columns=["y", "x", "red", "green", "blue", 'alpha'])
    def to_numpy_rgba(self):
        if 'alpha' not in self.df.columns.to_list():
            self.df['alpha'] = 255
        red = np.array(np.array_split(self.df.red.to_numpy(), self.maxlen + 1))
        green = np.array(np.array_split(self.df.green.to_numpy(), self.maxlen+ 1))
        blue = np.array(np.array_split(self.df.blue.to_numpy(), self.maxlen + 1))
        alpha = np.array(np.array_split(self.df.alpha.to_numpy(), self.maxlen + 1))
        return np.dstack((blue, green, red, alpha))
    def to_numpy_rgb(self):
        red = np.array(np.array_split(self.df.red.to_numpy(), self.maxlen + 1))
        green = np.array(np.array_split(self.df.green.to_numpy(), self.maxlen+ 1))
        blue = np.array(np.array_split(self.df.blue.to_numpy(), self.maxlen + 1))
        return np.dstack((blue, green, red))
    def to_file_rgb(self, path):
        picnp = self.to_numpy_rgb()
        cv2.imwrite(path, picnp)
    def to_file_rgba(self, path):
        picnp = self.to_numpy_rgba()
        cv2.imwrite(path, picnp)


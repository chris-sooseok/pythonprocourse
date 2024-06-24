import numpy as np
from PIL import Image

# zeros((5, 4, 3)) defines dimention
# Create 3d numpy array of zeros, then
# replace zeros with colors
data = np.zeros((5, 4, 3), dype=np.uint8)

# yellow
# data[:] accessing every list of the array
data[:] = [255,255,0]
print(data)

# Make a red patch
# data[1:3] accessing index 1, 2 of the array
# data[1:3] is a row of the img
data[1:3] = [255, 0, 0]

# accessing a column of the img
data[:, 1:3] = [255, 0, 0]


img = Image.fromarray(data, 'RGB')
img.save('canvas.png')
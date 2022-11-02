from PIL import Image
import numpy as np
import os

# 20%

SIZE = 250
nuance = [chr(i) for i in range(30, 145)]     #""" .:-=+#%@&$"""
path = 'img/joconde.png'
img = Image.open(path)

ratio = img.size[1] / img.size[0]
img = img.resize((SIZE, int(ratio * SIZE)))

img = np.array(img)



for i in range(len(img)):
    for j in range(len(img[i])):
        gray = 0
        for k in range(3):
            gray += img[i][j][k]
        gray = gray // 3
        img[i][j] = [gray, gray, gray]
result = open('result.txt', 'w')

for i in range(len(img)):
    line = ''
    for j in range(len(img[i])):
        line = line + f"{nuance[(img[i][j][0] * len(nuance) // 255)]}" * 2
    result.write(f"{line}\n")
result.close()

os.system("result.txt")
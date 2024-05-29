import numpy as np
from PIL import Image

img = Image.open("Анодный эффект.jpg")

img = np.asarray(img)
a = (255-img[:,:,0])

max_mpr = 0.24
min_mpr = 0.19
div = max_mpr-min_mpr
a = min_mpr+div*(a/np.max(a))

print(0.6-0.32-np.max(a))

f = open("anodeffect.txt", "w", encoding="utf-8")

for i in range(a.shape[0]):
    f.write(np.array2string(a[i]).replace('\n','').replace('[','').replace(']','\n'))

f.close()

a = (a - (min_mpr+div/2))*0.5+(min_mpr+div/2)

print(0.6-0.32-np.max(a))

f = open("anodeffect2.txt", "w", encoding="utf-8")

for i in range(a.shape[0]):
    f.write(np.array2string(a[i]).replace('\n','').replace('[','').replace(']','\n'))

f.close()
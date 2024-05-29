import numpy as np
from PIL import Image

img = Image.open("Анодный эффект.jpg")

img = np.asarray(img)
a = (255-img[:,:,0])
a = 0.19+(0.21-0.19)*(a/np.max(a))

a = (a - 0.2)*1.5+0.2

f = open("anodeffect2.txt", "w", encoding="utf-8")

for i in range(a.shape[0]):
    f.write(np.array2string(a[i]).replace('\n','').replace('[','').replace(']','\n'))

f.close()
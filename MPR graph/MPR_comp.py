import numpy as np
import matplotlib.pyplot as plt

f = open("h.txt", "r", encoding="utf-8")

d = []

x = np.linspace(0,3.4, 31)
y = np.linspace(0,9.4, 11)

x, y = np.meshgrid(x, y)

for line in f:
    data = line.split()
    d.append([])
    for i in data:
        d[-1].append(float(i))

d = np.array(d)

f.close()

d = abs(0.6-0.25-d)

fig, axs = plt.subplots()
pc = axs.pcolormesh(x, y, d, vmin=0.05, vmax=0.17, cmap='RdBu_r')
fig.colorbar(pc)
axs.set_title('МПР')

#plt.show()

fig = plotly.express.imshow(d)
fig.show()
import matplotlib.pyplot as plt
import numpy as np

f = open("h.txt", "r", encoding="utf-8")

d = []

x = np.arange(1, 32, 1)
y = np.arange(1, 12, 1)
x, y = np.meshgrid(x, y)

for line in f:
    data = line.split()
    d.append([])
    for i in data:
        d[-1].append(float(i))

a = np.array(d)

f.close()

print(0.6-np.max(a)-0.25, np.max(a))

a = (a-0.25)*0.5+0.25
d = a

print(0.6-np.max(a)-0.25, np.max(a))

f.close()

strok = 11
stolb = 4

#print(x[strok-1,stolb-1], y[strok-1,stolb-1], d[strok-1,stolb-1])
#print("l = ", 0.6-d[strok-1,stolb-1])

# Plot the surface
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(x, y, d)
ax.plot_surface(x, y, np.zeros(d.shape), alpha=0)
ax.set_xlabel("Ширина ванны (м)")
ax.set_ylabel("Длинна ванны (м)")
ax.set_zlabel("Расстояние до дна ванны(м)")

plt.show()


f = open("h2.txt", "w", encoding="utf-8")

for i in range(a.shape[0]):
    f.write(np.array2string(a[i]).replace('\n','').replace('[','').replace(']','\n'))

f.close()

import numpy as np
import matplotlib.pyplot as plt

x = np.ones((11))
y = np.ones((40))

x = np.linspace(0,1,100)*10
y = np.linspace(0,1,100)*5

a = np.zeros((100,100))

for i1 in range(len(a)):
    for i2 in range(len(a[0])):
        a[i1][i2] = 0.44+0.05*np.sin(y[i1])*np.cos(x[i2])

'''

low = 0.25
high = 0.29
a = a + low
for i in range(a.shape[0]):
	if i>a.shape[0]//3*2:
		a[i] = (a[i] + x*(high-low)*dx[i]*vx[i-a.shape[0]//3*2])
	a[i] = a[i] + (0.5-abs(x-0.5))*0.01

dy = np.linspace(0,1,a.shape[1])
vy = np.linspace(0,1,a.shape[1]//3+1)

for i in range(a.shape[1]):
	if i>a.shape[1]//3*2:
		a[:,i] = (a[:,i] + y*(high-low)*dy[i]*vx[i-a.shape[1]//3*2])
	a[:,i] = a[:,i] + (0.5-abs(y-0.5))*0.01

#a = a+ np.random.rand(a.shape[0], a.shape[1])*0.001

a[-1] = a[-2]
a[0] = a[1]
a[:,0] = a[:,1]
a[:,-1] = a[:,-2]

'''

'''
a = a+0.22
for i in range(a.shape[0]):
	a[i] = (a[i] + x*(0.25-0.216)/6)
	if i<a.shape[0]//3:
		a[i] = (a[i] + x*(0.25-0.216)/6*v[-i])
	elif i>=a.shape[0]//3*2:
		a[i] = (a[i] + x*(0.25-0.216)/6*v[i-a.shape[0]//3*2])
	a[i] = a[i] + (0.5-abs(x-0.5))*0.01

for i in range(a.shape[1]):
	a[:,i] = (a[:,i] + y*(0.25-0.216)/2)
	a[:,i] = a[:,i] + (0.5-abs(y-0.5))*0.01

a = a+ np.random.rand(a.shape[0], a.shape[1])*0.001
'''


'''
a = a+0.22
for i in range(a.shape[0]):
	a[i] = (a[i] + x*(0.3-0.216)/6)
	if i<a.shape[0]//3:
		a[i] = (a[i] + x*(0.3-0.216)/6*v[-i])
	elif i>=a.shape[0]//3*2:
		a[i] = (a[i] + x*(0.3-0.216)/6*v[i-a.shape[0]//3*2])
	a[i] = a[i] + (0.5-abs(x-0.5))*0.02

for i in range(a.shape[1]):
	a[:,i] = (a[:,i] + y*(0.3-0.216)/2)
	a[:,i] = a[:,i] + (0.5-abs(y-0.5))*0.02

a = a+ np.random.rand(a.shape[0], a.shape[1])*0.001

'''

x, y = np.meshgrid(x, y)
# Plot the surface
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(x, y, a)
ax.plot_surface(x, y, np.ones(a.shape)*0.2, alpha=0)
ax.set_xlabel("y (m)")
ax.set_ylabel("x (m)")
ax.set_zlabel("z (m)")

plt.show()

f = open("6sem2.txt", "w", encoding="utf-8")

for i in range(a.shape[0]):
    f.write(np.array2string(a[i]).replace('\n','').replace('[','').replace(']','\n'))

f.close()
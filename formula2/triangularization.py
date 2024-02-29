import numpy as np
import matplotlib.pyplot as plt

class Grid():
    """A class that stores triangles and their order in a grid"""

    def __init__(self, x, y, z):
        self.triangles = []
        for i1 in range(len(x)-1):
            for i2 in range(len(y)-1):
                self.triangles.append([])
                self.triangles[-1].append(Triangle([x[i1], y[i2], z[i1][i2]],
                                                  [x[i1+1], y[i2], z[i1+1][i2]],
                                                  [x[i1], y[i2+1], z[i1][i2+1]]))
                self.triangles[-1].append(Triangle([x[i1+1], y[i2+1], z[i1+1][i2+1]],
                                                  [x[i1], y[i2+1], z[i1][i2+1]],
                                                  [x[i1+1], y[i2], z[i1+1][i2]]))

    def integral(self):
        """Calculating the integral sum for all triangles"""
        sum = 0
        for square in self.triangles:
            for triangle in square:
                sum += triangle.intpart()
        eta_0 = 0.95
        Squ = 15.8792448
        dot = [6,24]
        dot[0] = dot[0]-1
        dot[1] = dot[1]-1
#        return (1-eta_0)*(0.6-z[dot[0]][dot[1]])/Squ*sum
        return (1-eta_0)/Squ*sum

    def square(self):
        """Calculating the surface area"""
        sum = 0
        for square in self.triangles:
            for triangle in square:
                sum += triangle.squarepart()
        return sum


class Triangle():
    '''the class containing the corner points of a triangle,
    its area and the corresponding value of the function'''

    def __init__(self, dot1, dot2, dot3):
        self.a = np.array(dot1)
        self.b = np.array(dot2)
        self.c = np.array(dot3)

    def square(self):
        return np.linalg.norm(np.cross(self.a-self.b, self.a-self.c))/2

    def function(self):
        return ((f(self.a[2])+f(self.b[2])+f(self.c[2]))/3)

    def intpart(self):
        return self.square()*self.function()
    
    def squarepart(self):
        return self.square()

    def print(self):
        print(self.a, self.b, self.c)


def f(h):
    '''integral function'''
    return ((0.6-args.anod)-h)/h
    #return 1/h


if __name__ == '__main__':

    import argparse


    parser = argparse.ArgumentParser()
    parser.add_argument("--square", help='show square of the surface',
                        action='store_true')
    parser.add_argument("--plot", help='show plot of the surface',
                        action='store_true')
    parser.add_argument("--file_name", help='name of the file with data',
                        type=str, default='h.txt')
    parser.add_argument("--anod", help='Насколько погружен анод', type=float, default=0)
    args = parser.parse_args()


    file = open(args.file_name, "r", encoding="utf-8")
    leny = len(file.readline().split())
    lenx = len(file.readlines())+1
    file.close()

    #x = np.linspace(0, 3.4, lenx)
    #y = np.linspace(0, 9.4, leny)

    x = np.linspace(0, 2, lenx)
    y = np.linspace(0, 5, leny)

    z = []

    file = open(args.file_name, "r", encoding="utf-8")

    data = []
    for line in file:
        data_line = line.split()
        for i in range(len(data_line)):
            data_line[i] = float(data_line[i])
        data.append(data_line)

    h = data

    file.close()


    for i1 in range(len(x)):
        z.append([])
        for i2 in range(len(y)):
            z[-1].append(h[i1][i2])


    grid = Grid(x, y, z)
    x = np.outer(x, np.ones(len(y)))
    y = np.outer(y, np.ones(len(x))).T
    z = np.array(z)
    zero = np.zeros(z.shape)

    print(grid.integral())
    if args.square:
        print(grid.square())
    if args.plot:
        # Creating figure
        fig = plt.figure()
        ax = plt.axes(projection ='3d')
        
        # Creating plot
        ax.plot_surface(x, y, z)
        ax.plot_surface(x, y, zero)

        plt.show()
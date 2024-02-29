import numpy as np
import matplotlib.pyplot as plt
import argparse


def f2l1(x, y):
    return (0.1/40
            * 0.01
            * ((1+0.05*np.cos(x)*np.cos(y)-0.05*np.sin(x)*np.cos(y)))
            / (0.44+0.05*np.sin(x)*np.cos(y)))


def f2l2(x, y):
    return (0.1/40
            * 0.06
            * ((1+0.05*np.cos(x)*np.cos(y)-0.05*np.sin(x)*np.cos(y)))
            / (0.44+0.05*np.sin(x)*np.cos(y)))


def f2l3(x, y):
    return (0.1/40
            * 0.11
            * ((1+0.05*np.cos(x)*np.cos(y)-0.05*np.sin(x)*np.cos(y)))
            / (0.44+0.05*np.sin(x)*np.cos(y)))


def f2ln(x, y):
    return (0.1/40
            * (0.06-0.05*np.sin(x)*np.cos(y))
            * ((1+0.05*np.cos(x)*np.cos(y)-0.05*np.sin(x)*np.cos(y)))
            / (0.44+0.05*np.sin(x)*np.cos(y)))


def f1l1(x,y):
    return (0.1/40
            * 0.01
            * (1+(0.003)**2+(0.004)**2)**(1/2)
            / (0.44+0.003*x+0.004*y))

def f1l2(x,y):
    return (0.1/40
            * 0.06
            * (1+(0.003)**2+(0.004)**2)**(1/2)
            / (0.44+0.003*x+0.004*y))

def f1l3(x,y):
    return (0.1/40
            * 0.11
            * (1+(0.003)**2+(0.004)**2)**(1/2)
            / (0.44+0.003*x+0.004*y))

def f1ln(x,y):
    return (0.1/40
            * (0.06-0.003*x-0.004*y)
            * (1+(0.003)**2+(0.004)**2)**(1/2)
            / (0.44+0.003*x+0.004*y))


def intfun(fun_num:int, des_val:str, x, y):
    match fun_num:
        case 1:
            match des_val:
                case "1":
                    return f1l1(x,y)
                case "2":
                    return f1l2(x,y)
                case "3":
                    return f1l3(x,y)
                case "n":
                    return f1ln(x,y)
        case 2:
            match des_val:
                case "1":
                    return f2l1(x,y)
                case "2":
                    return f2l2(x,y)
                case "3":
                    return f2l3(x,y)
                case "n":
                    return f2ln(x,y)
    print('wrong parameters ', fun_num, ' ', des_val)
    exit()


def surface1(x, y):
    return 0.44 + 0.003 * x + 0.004 * y


def surface2(x,y):
    return 0.44+0.05 * np.sin(x) * np.cos(y)


def surface_plot():

    def f2(x,y):
        return x * 0

    def f3(x,y):
        return x * 0 +0.5

    x = np.linspace(0, 10, 30)
    y = np.linspace(0, 5, 15)

    X, Y = np.meshgrid(x, y)
    match args.function_number:
        case 1:
            Z = surface1(X, Y)
        case 2:
            Z = surface2(X, Y)
    Z2 = f2(X,Y)
    Z3 = f3(X,Y)


    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                    cmap='viridis', edgecolor='none')
    ax.plot_surface(X, Y, Z2, rstride=1, cstride=1,
                    cmap='viridis', edgecolor='none')
    ax.plot_surface(X, Y, Z3, rstride=1, cstride=1,
                    cmap='viridis', edgecolor='none')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('Граница раздела')

    #plt.show()

parser = argparse.ArgumentParser()
parser.add_argument("function_number", type=int)
parser.add_argument("poletopole_distance", 
                    help =  '1-min, 2-medium,3-max, n-inconstant',
                    type=str)
parser.add_argument("--x_dots", help='amount of dots on axis X', type=int, 
                    default=10)
parser.add_argument("--y_dots", help='amount of dots on axis Y', type=int, 
                    default=10)
parser.add_argument("--len_x", help='lengs of area on axis X', type=int, 
                    default=10)
parser.add_argument("--len_y", help='lengs of area on axis Y', type=int, 
                    default=5)
args = parser.parse_args()

surface_plot()

# parameters of the tub
x_len = 10
y_len = 5

x_dots_amount = args.x_dots
y_dots_amount = args.y_dots

x = np.linspace(0, x_len, x_dots_amount)
y = np.linspace(0, y_len, y_dots_amount)

del_x = x[1]-x[0]
del_y = y[1]-y[0]

int = 0

for X in x[:-1]:
    for Y in y[:-1]:
        int += intfun(args.function_number, args.poletopole_distance, X, Y)


res = int * del_x * del_y

print(res)

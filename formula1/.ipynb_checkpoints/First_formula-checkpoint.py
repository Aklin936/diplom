import numpy as np
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--variate", help =  'which variable to variate', type=int,
                    default=0)
parser.add_argument("--dots", help =  'amount of dots', type=int, default=100)
parser.add_argument("--I", help =  'amperage', type=float, default=250)
parser.add_argument("--I_min", help =  'amperage min', type=float, default=150)
parser.add_argument("--I_max", help =  'amperage max', type=float, default=300)
parser.add_argument("--a", help =  'length', type=float, default=10)
parser.add_argument("--a_min", help =  'length min', type=float, default=1)
parser.add_argument("--a_max", help =  'length max', type=float, default=20)
parser.add_argument("--b", help =  'width', type=float, default=5)
parser.add_argument("--b_min", help =  'width min', type=float, default=1)
parser.add_argument("--b_max", help =  'width max', type=float, default=20)
parser.add_argument("--S", help =  'square of anods', type=float, default=42.75)
parser.add_argument("--S_min", help =  'square min', type=float, default=10)
parser.add_argument("--S_max", help =  'square max', type=float, default=100)
parser.add_argument("--i", help =  'electric density', type=float, default=0.5)
parser.add_argument("--i_min", help =  'electric density min', type=float,
                    default=0.1)
parser.add_argument("--i_max", help =  'electric density max', type=float,
                    default=1)
parser.add_argument("--L", help =  'MPR', type=float, default=0.05)
parser.add_argument("--L_min", help =  'MPR min', type=float, default=0.02)
parser.add_argument("--L_max", help =  'MPR max', type=float, default=0.2)
parser.add_argument("--t", help =  'temperature', type=float, default=970)
parser.add_argument("--t_min", help =  'temperature min', type=float, default=940)
parser.add_argument("--t_max", help =  'temperature max', type=float, default=1000)
args = parser.parse_args()

def f(S,i,L,T):
    return ((1-2567*(S**0.21)/(i**0.58)/L/np.exp(12940/T))*100)


S = args.S
i = args.i
L = args.L
t = args.t

match args.variate:
    case 0:
        pass
    case 1:
        var = np.linspace(args.S_min, args.S_max, args.dots)
        S = var
        plt.xlabel('Площадь анода в метрах квадратных')
    case 2:
        var = np.linspace(args.i_min, args.i_max, args.dots)
        i = var
        plt.xlabel('Плотность тока в амперах на метры квадратные')
    case 3:
        var = np.linspace(args.L_min, args.L_max, args.dots)
        L = var
        plt.xlabel('Межполюсное расстояние в метрах')
    case 4:
        var = np.linspace(args.t_min, args.t_max, args.dots)
        t = var
        plt.xlabel('Температура в градусах цельсия')
    case 5:
        var = np.linspace(args.a_min, args.a_max, args.dots)
        S = (var-0.5)**2
        i = 25/var**2
        plt.xlabel('Длина и ширина ванны в метрах')
    case 6:
        var = np.linspace(args.I_min, args.I_max, args.dots)
        i = (var/args.S/10)
        plt.xlabel('Сила тока в кА')

y = f(S, i, L, t)

match args.variate:
    case 1,2,3,4,5,6:
        plt.ylabel('Выход по току (В долях)')

        plt.plot(var, y, 'b')
        plt.show()
    case 0:
        print(y)
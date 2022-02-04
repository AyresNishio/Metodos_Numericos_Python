import numpy as np 

if __name__ == "__main__":
    #exemplo 8.3
    x = [0, 0.05, .1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
    y = [0,   37, 71,  104, 134,  161, 185, 207, 225, 239, 250]

    intervalos = len(y) - 1
    area = 0
    for i in  range(intervalos):
        print(area)
        area = area + (x[i+1]-x[i])*(y[i]+y[i+1])/2

    print(area)

    print(np.sqrt(area*2/0.075) * 3.6)
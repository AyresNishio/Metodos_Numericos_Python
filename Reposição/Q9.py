import numpy as np 

if __name__ == "__main__":
    #exemplo 8.3
    x = [0, 0.5, 1, 1.5, 48, 48.5, 49, 59, 69, 79]
    y = [62, 74, 73.5, 60.5, 49.5, 42.5, 39, 44.5, 58, 61.5]

    intervalos = len(y) - 1
    area = 0
    for i in  range(intervalos):
        print(area)
        area = area + (x[i+1]-x[i])*(y[i]+y[i+1])/2

    print(area)

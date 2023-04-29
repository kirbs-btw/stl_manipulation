import math
import random as r
import numpy as np
from mpl_toolkits import mplot3d
from matplotlib import pyplot

def add_arr(arr, arr2):
    for i in arr2:
        arr.append(i)

def createPoints(arr, fac, count):
    new_arr = []


    for point in arr:
        for _ in range(count):
            x = point[0] + (r.randint(0, 100)*fac)
            y = point[1] + (r.randint(0, 100)*fac)
            z = point[2] + (r.randint(0, 100)*fac)
            new_arr.append([x, y, z])

    add_arr(arr, new_arr)
    
    return arr   

def main():
    points = [[0, 0, 0]]
    points = createPoints(points, 2, 6)
    points = createPoints(points, 0.5, 20)

     # define graph
    fig = pyplot.figure()
    ax = fig.add_subplot(projection='3d')

    # scatter points on graph
    for i in points:    
        print(i)
        ax.scatter(i[0], i[1], i[2])

    # shows the final graph
    pyplot.show()

if __name__ == '__main__':
    main()
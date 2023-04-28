import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot
import math

def manipulate(points) -> list:
    for point in points:
        dist =  math.sqrt(point[0]**2 + point[1]**2 + point[2]**2)

        
        point[2] = dist ** 2

    return points


def create_points() -> list:
    points = []
    size = 4
    for i in range(-size + 1, size):
        for j in range(-size + 1, size):
            for h in range(-size + 1, size):
                points.append([i, j, h])
        
    return points

def main() -> None:
    points = create_points()
    points = manipulate(points)

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
import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot
import math


def manipulate(points) -> list:
    for point in points:
        # dist =  math.sqrt(point[0]**2 + point[1]**2 + point[2]**2)
    
        point[1] = point[1] * point[0] * (-1)
        point[2] = point[1] * point[0]

    return points


def main() -> None:
    plane = mesh.Mesh.from_file('H:/Projekte/Projekte/Project 137/stl_test/plane.stl')

    # define graph
    fig = pyplot.figure()
    ax = fig.add_subplot(projection='3d')

    # get points
    points = np.around(np.unique(plane.vectors.reshape([int(plane.vectors.size/3), 3]), axis=0), 2)
    manipulate(points)

    # scatter points on graph
    for i in points:    
        print(i)
        ax.scatter(i[0], i[1], i[2])

    # shows the final graph
    pyplot.show()


if __name__ == '__main__':
    main()
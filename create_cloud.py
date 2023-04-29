from mpl_toolkits import mplot3d
from matplotlib import pyplot
import random


def create_points() -> list:
    points = []
    size = 100

    for i in range(0, size):
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        z = random.randint(0, 100)
        points.append([x, y, z])
        
    return points

def main() -> None:
    points = create_points()

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
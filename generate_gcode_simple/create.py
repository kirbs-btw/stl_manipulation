import numpy as np
from stl import mesh


def mid_part():
    cube = mesh.Mesh.from_file('C:/Users/Bastian/Desktop/stl_test/plane.stl')

    points = np.around(np.unique(cube.vectors.reshape([int(cube.vectors.size/3), 3]), axis=0), 2)

    for i in points:    
        print(i)

    # generate code for movement


def main():

    content = []
    


    with open('H:/Projekte/Projekte/Project 137/stl_test/generate_gcode_simple/top_gcode.txt') as f:
        top = f.readlines()

    with open('H:/Projekte/Projekte/Project 137/stl_test/generate_gcode_simple/end_gcode.txt') as f:
        end = f.readlines()

    file = open('H:/Projekte/Projekte/Project 137/stl_test/generate_gcode_simple/gcode.gcode', 'w+')

    for char in top:
        file.write(char)

    for char in content:
        file.write(char)

    for char in end:
        file.write(char)


if __name__ == '__main__':
    main()
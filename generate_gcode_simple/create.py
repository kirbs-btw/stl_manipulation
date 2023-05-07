import numpy as np
from stl import mesh


def slice():
    mov_points = []
    extrusion = []
    moves = []

    cube = mesh.Mesh.from_file('C:/Users/Bastian/Desktop/stl_test/plane.stl')

    points = np.around(np.unique(cube.vectors.reshape([int(cube.vectors.size/3), 3]), axis=0), 2)

    for i in points:    
        print(i)

    # generate code for movement

    # slice to 0.2mm layers
    # (sort by hight) insert layer move points
    # pick one point 
    # pick next by sorting the layer points with distance
    # go to next layer 

    # convert list to movements 
    for index, point in enumerate(mov_points):
        line = "G1 X{} Y{} E{}".format(point[0], point[1], extrusion[index])
        moves.append(line)

    
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
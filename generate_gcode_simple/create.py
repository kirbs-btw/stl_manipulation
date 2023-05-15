import numpy as np
from stl import mesh

def find_min_z(points) -> float:
    
    z_values = [i[2] for i in points]
    offset = min(z_values)

    return offset

def add_offset(points, offset) -> list:
    arr = []

    for i in points:
        arr.append([i[0], i[1], (i[2] - offset)])

    return arr

def add_dim(points, x, y, z) -> list:
    arr = []
    for point in points:
        point_x = point[0] * (x/2)
        point_y = point[1] * (y/2)
        point_z = point[2] * (z/2)
        arr.append([point_x, point_y, point_z])

    return arr

def add_bed_dim(points, bed_dim_x, bed_dim_y) -> list:
    arr = []

    for i in points:
        arr.append([i[0] + (bed_dim_x/2), i[1] + (bed_dim_y/2), i[2]])

    return arr

def sort_points_by_height(points):
    n = len(points)

    swapped = False
    
    for i in range(n-1):
        for j in range(0, n-i-1):
            if points[j][2] > points[j + 1][2]:
                swapped = True
                points[j], points[j + 1] = points[j + 1], points[j]
         
        if not swapped: 
            return

def slice():
    # dim
    x = 10
    y = 10 
    z = 10

    bed_dim_x = 200
    bed_dim_y = 200

    mov_points = []
    extrusion = []
    moves = []

    cube = mesh.Mesh.from_file('H:/Projekte/Projekte/Project 137/stl_test/cube.stl')

    points = np.around(np.unique(cube.vectors.reshape([int(cube.vectors.size/3), 3]), axis=0), 2)

    for i in points:    
        print(i)

    # position up with the smallest z 
    
    offset = find_min_z(points)
    points = add_offset(points, offset)

    # add obj real dimensions

    points = add_dim(points, x, y, z)

    # adjust for printbed size

    points = add_bed_dim(points, bed_dim_x, bed_dim_y)

    for i in points:
        print(i)

    # generate code for movement

    # slice to 0.2mm layers
    # (sort by hight) insert 
    sort_points_by_height(points)

    # layer move points

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
    slice()
import numpy as np
from stl import mesh
import math

def find_min_z(points) -> float:
    
    z_values = [i[2] for i in points]
    offset = min(z_values)

    return offset

def add_offset(points) -> list:
    offset = find_min_z(points)
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

def insert_layer_shifts(points) -> list:
    arr = []
    for i, j in enumerate(points):
        try:
            arr.append(points[i])
            if points[i][2] != points[i+1][2]:
                arr.append("shift")
        except:
            pass
    return arr

def generate_gcode(points) -> list:
    extrusion = calc_extrusion(calc_dist(points), 0.2)
    moves = []
    moves.append("G0 Z0")
    points_with_shift = insert_layer_shifts(points)
    max_int = len(points) - 1
    for index, point in enumerate(points_with_shift):
        if (index + 1) > max_int:
            break
        elif point == "shift":
            line = "G0 Z{}\n;LAYER:{}".format(points[index+1][2], index+1)
        else:
            line = "G1 X{} Y{} E{}".format(point[0], point[1], extrusion[index])
    
        moves.append(line)
    
    return moves

def calc_extrusion(dist, fac) -> list:
    arr = []
    
    for i in dist:
        arr.append((i*fac))
    
    added_arr = []
    prev_arr = 0

    for i in arr:
        prev_arr += i
        added_arr.append(prev_arr + i)

    return added_arr


def calc_dist(points) -> list:
    dist_arr = []
    max_int = len(points) - 1

    for index, point in enumerate(points):
        if (index + 1) > max_int:
            break
        point_a = points[index]
        point_b = points[index+1]
        
        a = (point_a[0] - point_b[0]) ** 2
        b = (point_a[1] - point_b[1]) ** 2
        c = (point_a[2] - point_b[2]) ** 2

        dist = math.sqrt(a + b + c)
        print(dist)
        dist_arr.append(dist)

    return dist_arr

def slice() -> list:
    # dim
    x = 2.5
    y = 2.5
    z = 2.5

    bed_dim_x = 200
    bed_dim_y = 200

    stl_file = 'H:/Projekte/Projekte/Project 137/stl_test/generate_gcode_simple/stl/AppleWatchDock.stl'
    # stl_file = 'H:/Projekte/Projekte/Project 137/stl_test/cube.stl'

    cube = mesh.Mesh.from_file(stl_file)
    # slice to 0.2mm layers

    # get points of mesh - relativ and not centert to printbed
    points = np.around(np.unique(cube.vectors.reshape([int(cube.vectors.size/3), 3]), axis=0), 2)

    # position up with the smallest z 
    points = add_offset(points)

    # add obj real dimensions
    points = add_dim(points, x, y, z)

    # adjust for printbed size
    points = add_bed_dim(points, bed_dim_x, bed_dim_y)

    # (sort by hight) insert 
    sort_points_by_height(points)

    # layer move points
    
    for i in points:
        print(i)

    # pick one point 
    # pick next by sorting the layer points with distance
    # go to next layer 

    # convert list to movements 
    moves = generate_gcode(points)

    for i in moves:
        print(i)
    
    return moves

def main():

    content = slice()
    
    with open('H:/Projekte/Projekte/Project 137/stl_test/generate_gcode_simple/top_gcode.txt') as f:
        top = f.readlines()

    with open('H:/Projekte/Projekte/Project 137/stl_test/generate_gcode_simple/end_gcode.txt') as f:
        end = f.readlines()

    file = open('H:/Projekte/Projekte/Project 137/stl_test/generate_gcode_simple/gcode.gcode', 'w+')

    for char in top:
        file.write(char)

    for char in content:
        file.write('\n{}'.format(char))

    for char in end:
        file.write(char)


if __name__ == '__main__':
    main()
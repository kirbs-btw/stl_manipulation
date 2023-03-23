import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

cube = mesh.Mesh.from_file('C:/Users/Bastian/Desktop/stl_test/plane.stl')
"""
get cube data to manipulate 
work with gcode to have nice finish 


VERTICE_COUNT = 8
data = np.zeros(VERTICE_COUNT, dtype=mesh.Mesh.dtype)
cube = mesh.Mesh(data, remove_empty_areas=False)
"""

fig = pyplot.figure()

ax = fig.add_subplot(projection='3d')

points = np.around(np.unique(cube.vectors.reshape([int(cube.vectors.size/3), 3]), axis=0), 2)

# change point depending on the distance to the center point

for i in points:    
    print(i)
    ax.scatter(i[0], i[1], i[2])

"""
for i in np.unique(cube.vectors, axis=0):    
    print(i)
    ax.scatter(i[0], i[1], i[2])
"""
"""
for i in np.unique(cube.normals, axis=0):    
    print(i)
    ax.scatter(i[0], i[1], i[2])
"""

pyplot.show()



points = np.around(np.unique(cube.vectors.reshape([int(cube.vectors.size/3), 3]), axis=0), 2)
print ("Points are", points.tolist())


"""
figure = pyplot.figure()
axes = figure.add_subplot(projection='3d')

axes.add_collection3d(mplot3d.art3d.Poly3DCollection(cube.vectors))

scale = cube.points.flatten()
axes.auto_scale_xyz(scale, scale, scale)

pyplot.show()
"""

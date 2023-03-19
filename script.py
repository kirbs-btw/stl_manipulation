import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

cube = mesh.Mesh.from_file('C:/Users/Bastian/Desktop/stl_test/cube.stl')
"""
VERTICE_COUNT = 8
data = np.zeros(VERTICE_COUNT, dtype=mesh.Mesh.dtype)
cube = mesh.Mesh(data, remove_empty_areas=False)
"""

points = np.around(np.unique(cube.vectors.reshape([int(cube.vectors.size/3), 3]), axis=0), 2)
print ("Points are", points.tolist())



figure = pyplot.figure()
axes = figure.add_subplot(projection='3d')

axes.add_collection3d(mplot3d.art3d.Poly3DCollection(cube.vectors))

scale = cube.points.flatten()
axes.auto_scale_xyz(scale, scale, scale)

pyplot.show()

print(cube.v0)

print("finish")
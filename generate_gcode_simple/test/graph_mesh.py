from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot
from mpl_toolkits.mplot3d import axes3d

# Create a new plot
fig = pyplot.figure()
ax = fig.add_subplot(projection='3d')

# Load the STL files and add the vectors to the plot
your_mesh = mesh.Mesh.from_file('H:/Projekte/Projekte/Project 137/stl_test/generate_gcode_simple/test/cube.stl')

# try to add a wireframe 
ax.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

# Auto scale to the mesh size
scale = your_mesh.points.flatten("F")


# Show the plot to the screen
pyplot.show()
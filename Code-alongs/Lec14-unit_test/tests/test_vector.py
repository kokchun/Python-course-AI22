import sys, os

print(__file__)

# we change directory to where this file is
os.chdir(os.path.dirname(__file__))

# we define a path that is up one step
# in this path we have vector.py and plotter.py and manual_testing.ipynb
path_to_vector_module = os.path.abspath("../")

sys.path.append(path_to_vector_module)
print(path_to_vector_module)

from vector import Vector



import sys, os

# here we work with paths and not change our own current working directory
root_path = os.path.dirname(__file__)
folder1_path = os.path.join(root_path, "folder1")
folder2_path = os.path.join(root_path, "folder2")

os.system("cls||clear")

print("="*100)
print(f"{root_path=}\n")

print(f"{folder1_path=}\n")

print("="*100)

# adding paths to sys.path could be an issue when dealing with large project
# as module names can clash, instead one can work with packages 
sys.path.append(folder1_path)
sys.path.append(folder2_path)

import module1, module2
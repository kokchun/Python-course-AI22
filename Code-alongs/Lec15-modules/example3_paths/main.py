import sys, os 

root_path = os.path.dirname(__file__)
path_folder1 = os.path.join(root_path, "folder1")
path_folder2 = os.path.join(root_path, "folder2")


os.system("cls||clear")
print("="*100)

print(root_path)

print()

print(path_folder1)

print("="*100)

sys.path.append(path_folder1)
sys.path.append(path_folder2)

import module1, module2

print(sys.path)
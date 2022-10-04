import os, sys

os.system("cls||clear")

print(f"{'='*30}main.py{'='*30}\n")

# code imported from another module is executed when imported
import module1

# note that __name__ is module1 when ran from outside of module1.py itself
# __name__ is __main__ when ran directly from the file

# the module object module1 is put into the globals() namespace
print("globals")
print(globals()["module1"])

print()

# all modules that are loaded is in sys.modules 
print("sys.modules")
print(sys.modules["module1"])


# note that it doesn't execute the module1, because module1 is already stored in sys.modules
import module1

print(f"\n{'='*30}end main.py{'='*26}\n")

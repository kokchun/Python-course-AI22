# import needs to be in top of file - better style
import sys

print("="*60)

# running main.py but the module name is __main__
# when running a file in starting point the name of the file will be renamed to __main__
print(f"Running main.py - module name {__name__}")

# import the modules - it runs the module
import module1

print("import module1 again")

del globals()["module1"]
# looked in the cache, don't need to reexecuted
import module1


""" print(module1)
module1.pprint_dict("main.globals", globals())

print(sys.path)

print()
print(sys.modules["module1"])

 """

print("="*60)


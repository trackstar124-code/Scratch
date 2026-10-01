"""
Demo: importing a function from another file WITHOUT triggering its
main(). Run this file directly to see it in action.
"""

import functions_advanced_demo

# we can use filter_outliers() here...
print(functions_advanced_demo.filter_outliers([5, 200, 40, -1]))

# ...but notice "main() result: ..." never printed above, even though
# functions_advanced_demo.py has a main() and an if __name__ == "__main__"
# block. That's because __name__ inside functions_advanced_demo.py is
# "functions_advanced_demo" when it's imported, not "__main__" -- so its
# guard skipped calling main() automatically.

print("import_demo.py finished")

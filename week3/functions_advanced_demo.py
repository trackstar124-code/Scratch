"""
Demo: function documentation, filtering, and the main-function pattern
for DS 2500
"""

# --- filter_outliers: optional parameters + avoiding built-in shadowing ---
def filter_outliers(values, min_threshold=0, max_threshold=100):
    """
    Filter a list of numeric values down to those within a range.

    Parameters
    ----------
    values : list of float
        The numbers to filter.
    min_threshold : float, optional
        The smallest value to keep, inclusive (default is 0).
    max_threshold : float, optional
        The largest value to keep, inclusive (default is 100).

    Returns
    -------
    list of float
        Only the values that fall within [min_threshold, max_threshold].
    """
    # NOTE: named min_threshold / max_threshold on purpose -- naming these
    # "min" and "max" would SHADOW Python's built-in min() and max()
    # functions for the rest of this function's scope, silently breaking
    # anything below that tries to actually call min()/max()
    filtered = []
    for value in values:
        if value >= min_threshold and value <= max_threshold:
            filtered.append(value)
    return filtered


# --- Trying it out ---
data = [-10, 5, 42, 99, 150, 0, 100, 73]

print(filter_outliers(data))                    # uses the defaults: 0 to 100
print(filter_outliers(data, min_threshold=10))  # override just one side
print(filter_outliers(data, max_threshold=50))  # override the other side
print(filter_outliers(data, -20, 200))          # positional overrides for both


# --- Docstring styles (comparison, not all meant to run) ---
# numpy-style (used above) -- Summary, Parameters, Returns as labeled
# sections. This is what the lecture recommends, and what tools like
# pdoc and Sphinx can parse automatically to build documentation
# websites from your code.

def numpy_style_example(x, y):
    """
    Add two numbers together.

    Parameters
    ----------
    x : int
        The first number.
    y : int
        The second number.

    Returns
    -------
    int
        The sum of x and y.
    """
    return x + y


# Google-style -- similar information, different formatting convention
def google_style_example(x, y):
    """Add two numbers together.

    Args:
        x (int): The first number.
        y (int): The second number.

    Returns:
        int: The sum of x and y.
    """
    return x + y


# a plain one-line docstring -- fine for very simple/obvious functions,
# but doesn't give a doc-generator tool enough to work with
def one_liner_example(x, y):
    """Add two numbers together."""
    return x + y


# --- The main-function pattern ---
# `main()` is just a regular function, by convention treated as the
# starting point of the program -- it calls whatever other functions
# are needed to get the actual work done, instead of loose code sitting
# at the top level of the file
def main():
    sample = [3, 88, -5, 60, 105]
    result = filter_outliers(sample, min_threshold=0, max_threshold=100)
    print("main() result:", result)


# --- The if __name__ == "__main__" idiom ---
# every Python file has a built-in __name__ variable. When you RUN this
# file directly (python3 functions_advanced_demo.py), __name__ is set to
# "__main__", so the block below executes and main() runs.
#
# but if some OTHER file does `import functions_advanced_demo`, __name__
# is set to "functions_advanced_demo" instead -- so this block is
# skipped, and main() does NOT run automatically. That lets this file be
# reused as a library of functions (filter_outliers, etc.) elsewhere,
# without triggering its own demo/test code every time it's imported.
if __name__ == "__main__":
    main()

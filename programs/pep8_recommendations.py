
# PEP 8 Recommendations for .py Files

import os
import sys

# Constants
MAX_SIZE = 100

# Class definitions
class MyClass:
    """A simple example class."""

    def __init__(self, name):
        self.name = name

    def greet(self):
        """Greet the user."""
        return f"Hello, {self.name}!"

# Function definitions
def my_function():
    """Summary of function.
    
    Extended description of function.
    
    Returns:
        int: Description of return value.
    """
    return 42

# Main code
if __name__ == "__main__":
    my_instance = MyClass("World")
    print(my_instance.greet())
    
    try:
        value = my_function()
        print(f"Function returned: {value}")
    except ValueError as e:
        print(e)

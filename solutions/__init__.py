import importlib
import pkgutil
import os

# Dictionary to store modules
days = {}

# Iterate over all modules in the current directory
for (_, day_name, _) in pkgutil.iter_modules([os.path.dirname(__file__)]):
    # Import the day
    day = importlib.import_module('.' + day_name, __package__)
    # Register the day in the dictionary
    days[day_name] = day

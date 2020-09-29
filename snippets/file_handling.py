import os
from pathlib import Path


# Get current working dir (old way):
print(os.getcwd())
# Python 3.6 and later preferred:
print(Path.cwd())


# When want to create a new dir in subpath
# makedirs instead of makedir

# print(os.makedirs("somepath/some_more_path"))

# Use the pathlib (if exist_ok is false will fail if exists) parents true creates all the subfolders
# Path("test_folder").mkdir(parents=True, exist_ok=True)


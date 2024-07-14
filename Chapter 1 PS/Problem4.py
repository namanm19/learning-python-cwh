import os

# Get the directory path you want to list
directory_path = "."

# List the contents of the directory
contents = os.listdir(directory_path)

# Print the contents
for item in contents:
    print(item)

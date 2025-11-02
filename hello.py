# Example variables representing a folder path and a filename.
folder = 'C:/users/Abraham'
file = 'report.csv'
# Using os.path.join is a more robust way to create file paths


# Split the folder path string into a list of components.
sfolder = folder.split('/')

# Create a dictionary by pairing keys with the values from the split folder path
# The zip() function pairs elements from two lists together.
keys = ["Disk", "User", "Name"]
path_dict = dict(zip(keys, sfolder))
print(f"Original dictionary: {path_dict}")

# Let's create a second list
sfolder2 = ['D:', 'backups', 'abraham_pc']
print(f"Second list of values: {sfolder2}")

# Now, let's update the dictionary using the same keys but the new list.
# This will OVERWRITE the values for each key.
# Loop through the keys and new values simultaneously to update the dictionary.
for key, value in zip(keys, sfolder2):
    path_dict[key] = value

print(f"Dictionary after update: {path_dict}")

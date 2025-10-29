folder = 'C:/users/Abraham'
file = 'report.csv'
# Using os.path.join is a more robust way to create file paths


sfolder = folder.split('/')

# Create a dictionary by pairing keys with the values from the split folder path
keys = ["Disk", "User", "Name"]
path_dict = dict(zip(keys, sfolder))
print(f"Original dictionary: {path_dict}")

# Let's create a second list
sfolder2 = ['D:', 'backups', 'abraham_pc']
print(f"Second list of values: {sfolder2}")

# Now, let's update the dictionary using the same keys but the new list.
# This will OVERWRITE the values for each key.
for key, value in zip(keys, sfolder2):
    path_dict[key] = value

print(f"Dictionary after update: {path_dict}")

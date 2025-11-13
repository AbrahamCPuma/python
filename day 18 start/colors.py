import colorgram
import os

# Get the absolute path to the directory where this script is located.
# __file__ is a special variable that holds the path to the current script.
script_dir = os.path.dirname(os.path.abspath(__file__))

# Join the script's directory path with the image filename to create a full, reliable path.
image_path = os.path.join(script_dir, 'image.jpg')

colors = colorgram.extract(image_path, 30)

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
print(rgb_colors)
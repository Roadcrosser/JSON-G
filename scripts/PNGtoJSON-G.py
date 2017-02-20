source = "demo.png" # Specify the proper filepath for this one

saveto = "demo.jsng"

indent = 4 # set to None to minimize filesize

from PIL import Image
import json

version = "1.0"

maxcolors = 2**24

def to_color_dict(color):
    return {
    "red" : color[0],
    "green" : color[1],
    "blue" : color[2],
    "alpha" : color[3],
    }

img = Image.open(source).convert("RGBA")

colormap = img.getcolors(maxcolors=maxcolors)

default_color = (0, 0, 0, 255)

if colormap:
    default_color = sorted(colormap, reverse=True)[0][1]

default_color_dict = to_color_dict(default_color)

pixels = []

data = img.load()

for x in range(0, img.width):
    for y in range(0, img.height):
        px = data[x, y]
        if default_color and default_color == px:
            continue
        pixels += [
        {
            "position" :
            {
                "x" : x,
                "y" : y
            },
            "color" : to_color_dict(px)
        }
        ]

img.close()

assembly = {
    "version" : version,
    "size" : {
        "width" : img.width,
        "height" : img.height
    },
    "transparency" : True,
    "layers" : [
        {
            "default_color" : default_color_dict,
            "pixels" : pixels
        }
    ]
}

with open(saveto, 'w') as out:
    json.dump(assembly, out, indent = indent)

print("Converted {} to {}!".format(source, saveto))

import argparse
from datetime import datetime
from PIL import Image
import json

def indentarg(s):
    try:            
        int(s)
    except:
        if s == "None":
            return
        else:
            raise argparse.ArgumentTypeError("Must be int or NoneType.") 

parser = argparse.ArgumentParser(description="Converts a PNG "
                    "(or other PIL-supported formats) image to JSON-G.")

parser.add_argument("input", help="Filepath for input. e.g.: image.png")
parser.add_argument("output",
                    nargs="?",
                    default=None,
                    help="Filepath to output the JSON-G. "
                    "Defaults to filename of input. e.g.: image.jsng")
parser.add_argument("-i",
                    "--indent",
                    default=4,
                    help="Indent to format the JSON-G file in. "
                    "Defaults to 4. Set to None to minimize filesize.",
                    type=indentarg)
parser.add_argument("-m",
                    "--maxcolors",
                    default=16777216,
                    help="The upper bound for the number of unique colors in the image. "
                    "Defaults to 16777216. If this is less than the number of unique "
                    "colors in the image, color-frequency detection will fail and "
                    "the default color of the image will fallback to RGB(0, 0, 0, 0).",
                    type=int)

args = parser.parse_args()

source = args.input

saveto = args.output

if not saveto:
    saveto = source
    index = source.rfind(".")
    if index >= 0:
        saveto = source[:index]
    saveto += ".jsng"

version = "1.0" # This encoder follows spec 1.0

def to_color_dict(color):
    return {
    "red" : color[0],
    "green" : color[1],
    "blue" : color[2],
    "alpha" : color[3],
    }

start = datetime.utcnow() # Collect time for benchmarks or whatever.

img = Image.open(source).convert("RGBA")

colormap = img.getcolors(maxcolors=args.maxcolors)

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

converted = datetime.utcnow()

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
    json.dump(assembly, out, indent = args.indent)

saved = datetime.utcnow()

print("Converted {} to {}!\n\nTime taken to convert: {}\nTime taken to save: {}\nTotal time taken: {}".format(
    source,
    saveto,
    converted - start,
    saved - converted,
    saved - start))

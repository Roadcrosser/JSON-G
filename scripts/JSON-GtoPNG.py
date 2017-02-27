import argparse
from datetime import datetime
from PIL import Image
import json
import os

parser = argparse.ArgumentParser(description="Converts a JSON-G image to PNG.")

parser.add_argument("input", help="Filepath for input. e.g.: image.jsng")
parser.add_argument("output",
                    nargs="?",
                    default=None,
                    help="Filepath to output the JSON-G. "
                    "Defaults to filename of input. e.g.: image.png")

args = parser.parse_args()

source = args.input

saveto = args.output

if not saveto:
    saveto = source
    index = source.rfind(".")
    if index >= 0:
        saveto = source[:index]
    saveto += ".png"

version = "1.0" # This decoder should only decode v1.0 to prevent future versions from potentially causing a corrupted output.

def from_color_dict(color):
    return (color["red"], color["green"], color["blue"], color["alpha"] if transparency else 255)

def resolve_color(dct):
    for c in ["default_color", "default_colour", "color", "colour"]:
        if c in dct:
            return dct[c]
    return {"red" : 0, "green" : 0, "blue" : 0, "alpha" : 255}

start = datetime.utcnow() # Collect time for benchmarks or whatever.

with open(source) as inp:
    jsng = json.load(inp)

if jsng["version"] != version:
    print("JSNG has invalid version!")
    exit()

transparency = jsng["transparency"]

size = (jsng["size"]["width"], jsng["size"]["height"])

base = Image.new("RGBA", size, (0, 0, 0, 0))

for l in jsng["layers"]:
    layer = Image.new("RGBA", size, from_color_dict(resolve_color(l)))
    for p in l["pixels"]:
        layer.putpixel((p["position"]["x"], p["position"]["y"]), from_color_dict(resolve_color(p)))
    base = Image.alpha_composite(base, layer)

converted = datetime.utcnow()

base.save(saveto)

base.close()

saved = datetime.utcnow()

in_size = os.stat(source).st_size
out_size = os.stat(saveto).st_size

print("Converted {} to {}!\n\nTime taken to convert: {}\nTime taken to save: {}\nTotal time taken: {}\n\nInput size: {} KB\nOutput size: {} KB\nMagnitude: {}".format(
    source,
    saveto,
    converted - start,
    saved - converted,
    saved - start,
    in_size/1000,
    out_size/1000,
    out_size/in_size))

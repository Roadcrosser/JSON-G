source = "demo.jsng" # Specify the proper filepath for this one

saveto = "demo.png"

from PIL import Image
import json

version = "1.0"

with open(source) as inp:
    jsng = json.load(inp)

if jsng["version"] != version:
    print("JSNG has invalid version!")
    exit()

transparency = jsng["transparency"]

size = (jsng["size"]["width"], jsng["size"]["height"])

def from_color_dict(color):
    return (color["red"], color["green"], color["blue"], color["alpha"] if transparency else 255)

def resolve_color(dct):
    for c in ["default_color", "default_colour", "color", "colour"]:
        if c in dct:
            return dct[c]
    return {"red" : 0, "green" : 0, "blue" : 0, "alpha" : 255}

base = Image.new("RGBA", size, (0, 0, 0, 0))

for l in jsng["layers"]:
    layer = Image.new("RGBA", size, from_color_dict(resolve_color(l)))
    for p in l["pixels"]:
        layer.putpixel((p["position"]["x"], p["position"]["y"]), from_color_dict(resolve_color(p)))
    base = Image.alpha_composite(base, layer)

base.save(saveto)

base.close()

print("Converted {} to {}!".format(source, saveto))

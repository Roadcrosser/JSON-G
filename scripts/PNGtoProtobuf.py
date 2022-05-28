import argparse
from datetime import datetime
from PIL import Image
import os
import image_pb2

parser = argparse.ArgumentParser(description="Converts a PNG "
                    "(or other PIL-supported formats) image to PRIMG.")

parser.add_argument("input", help="Filepath for input. e.g.: image.png")
parser.add_argument("output",
                    nargs="?",
                    default=None,
                    help="Filepath to output the PRIMG. "
                    "Defaults to filename of input. e.g.: image.primg")
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
    saveto += ".primg"

version = "1.0" # This encoder follows spec 1.0

def to_color_message(color):
    return image_pb2.Image.Color(
        red = color[0],
        green = color[1],
        blue = color[2],
        alpha = color[3]
    )

start = datetime.utcnow() # Collect time for benchmarks or whatever.

img = Image.open(source).convert("RGBA")

colormap = img.getcolors(maxcolors=args.maxcolors)

default_color = (0, 0, 0, 255)

if colormap:
    default_color = sorted(colormap, reverse=True)[0][1]

default_color_message = to_color_message(default_color)

data = img.load()

message = image_pb2.Image()
message.version = version
message.size.width = img.width
message.size.height = img.height
message.transparency = True

layer = image_pb2.Image.Layer(default_color = default_color_message)

for x in range(0, img.width):
    for y in range(0, img.height):
        px = data[x, y]
        if default_color and default_color == px:
            continue
        
        pixel = image_pb2.Image.Pixel(position=image_pb2.Image.Position(x=x, y=y), color=to_color_message(px))
        layer.pixels.append(pixel)

message.layers.append(layer)

img.close()

converted = datetime.utcnow()

with open(saveto, 'wb') as out:
    out.write(message.SerializeToString())

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

# JSON-G #

JSON-G (JSON-Graphics) is an extremely inefficient way to store raster image data, with transparency and layered support!


## Browsers that support JSON-G: ##
 - None!

## Here's a taste of what JSON-G can do! ##
```json
{
    "version": "1.0",
    "comment": "demo.jsng - a demo for JSON-G",
    "transparency": true,
    "size":
        {
            "width": 5,
            "height": 5
        },
    "layers" :
        [
            {
                "default_color" :
                    {
                        "red": 0,
                        "green": 0,
                        "blue": 0,
                        "alpha": 255
                    },
                "pixels" :
                    [
                        {
                            "position" :
                                {
                                    "x": 2,
                                    "y": 2
                                },
                            "color" :
                                {
                                    "red": 255,
                                    "green": 255,
                                    "blue": 255,
                                    "alpha": 255
                                },
                            "comment": "A nice white pixel."
                        }
                    ]
            }
        ]
}
```

This results in the following image, when converted to PNG:

![demo.jsong but in a png format](samples/demo.png)

...and here it is blown up, because that last one is far too small to look at and appreciate.

![demo.jsong but in a png format and scaled to 250x250](samples/demo_large.png)

## What else? ##

The rest of this repo contains specifications for how to read/write JSON-G, some sample JSON-G files as well as a PNG ⇌ JSON-G converter written in Python as a proof of concept.

There is also a [resources](resources.md) page showcasing JSON-G libraries created by others in various languages. If you make one, feel free to PR a link to it on that page!

## JSON-G sounds like J-song ##

I'd have called it `JSONP` if it hadn't already been [taken](https://en.wikipedia.org/wiki/JSONP), so `JSON-G` was the next best thing. I put a dash in between the `JSON` and `G` so people wouldn't pronounce it as J-song and hopefully avert another file-extension pronunciation war.

### So I can't call it J-song? ###

Do whatever you want tbh.

## What do people have to say about JSON-G? ##

> I am absolutely sorry for doing this
>
> — *HpslUU, inventor of JSON-G*

​
> Sounds like a waste
>
> — *Jake Heinz, some guy who works at Discord.*

​
> marvelous adding jsong brb
>
> — *Jaex, creator and lead developer of [ShareX](https://getsharex.com/)*

## Credits ##

Credit to [Gorialis](https://github.com/Gorialis) for helping me test the spec and my converters.

Also [HpslUU](https://github.com/HpslUU) who [gave me the whole idea](https://raw.githubusercontent.com/Roadcrosser/JSON-G/master/jsong-origin.png) for doing this anyway (and creating a GitHub account just so I could type this line).

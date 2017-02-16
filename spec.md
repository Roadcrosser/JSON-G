# Specification for the implementation of JSON-G #

For version `1.0`.

## Filetype ##

JSON-G officially uses `.jsng` as it's filetype although `.jsong` or just plain 'ol `.json` is fine too I guess.

## Basics ##

 - All fields are to be lowercase (except comments).

 - Unknown member names are ignored.

## Base Object ##

The base object has several members. They are:

 - **`version`** - *string* (Required)

   - This is the version of JSON-G used.

 - **`transparency`** - *boolean* (Required)

    - If this is set to false, all `alpha` fields are optional and ignored, being forced to `255`.

 - **`size`** - *object* (Required)

    - Contains an object with two members, `width` and `height`. Each maps to an integer, specifying the width and height of the image.

 - **`layers`** - *array* (Required)

    - Contains an array of [`layer`](#layers) objects.

## Layers ##

Layers are objects which contain the following members:

- **`default_color`** - *object*

    - Contains a [`color`](#color) object.
    - Aliases to `default_colour`.
    - If this field is not present, the default color defaults to `RGBA(0, 0, 0, 255)`.

- **`pixels`** - *array*

    - Contains an array of [`pixel`](#pixels) objects.

A layer will overlap the layer preceding it.

## Color ##

A color object has four members. All values are from `0` to `255`, following the RGBA scale.

- **`red`** - *number* (Required)
- **`blue`** - *number* (Required)
- **`green`** - *number* (Required)
- **`alpha`** - *number* (Required if `transparency` is `true`)

## Pixels ##

Pixels are objects which contain the following members:

- **`position`** - *object* (Required)

    - Contains an object with two members, `x` and `y`. Each maps to an integer, specifying the (zero-indexed) position of the pixel.

- **`color`** - *object* (Required)

    - Contains a [`color`](#color) object.
    - Aliases to `colour`.

If two pixels share the same position, the pixel that comes after will overwrite the first, and so on.

## Comments ##

Comment members can be inserted in any object, be it the base, layer, color or pixel. Comments are identified with the name `comment`, or any member that starts with two underscores (`__`).

While unknown member names can be used as comments, it is not recommended to do so, as it may affect backwards compatibility.

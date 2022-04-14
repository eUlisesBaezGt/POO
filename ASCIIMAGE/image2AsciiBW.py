import PIL.Image
from Colors import *

# ascii characters that we will be using
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]


# resize image with new width
def resize(img, new_width=125):
    width, height = img.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width)
    return img.resize((new_width, new_height))


# convert pixel2grayscale
def grayscale(img):
    return img.convert(
        "L"
    )  # grayscale single channel image. Just stores the Luminance.


# convert pixel2ascii
def pixels2ascii(img):
    pixels = img.getdata()
    characters = "".join(
        [ASCII_CHARS[pixel // 25] for pixel in pixels]
    )  # double slash can’t return fractional part of
    # the floating-point result
    return characters


def main(new_width=125):
    path = input("Enter the path to the img: ")
    # C:/Users/eubgo/Desktop/POO/ASCIIMAGE/Boba.jpg
    # C:/Users/eubgo/Desktop/POO/ASCIIMAGE/Chewie.jpg
    try:
        img = PIL.Image.open(path)
    except:
        print(
            Colors.Underlined
            + Colors.Bold
            + Colors.Red
            + "Error:\n"
            + "Could not open the image from:\n"
            + Colors.Blue
            + Colors.Underlined
            + Colors.Bold
            + path
            + Colors.ResetAll
        )
        return

    # image through process
    new_img_data = pixels2ascii(grayscale(resize(img)))
    n_pixels = len(new_img_data)

    # split string of chars into multiple strings of length equal to new width and create a list
    ascii_image = "\n".join(
        [new_img_data[i : (i + new_width)] for i in range(0, n_pixels, new_width)]
    )

    # show result in console
    print(ascii_image)

    # save result to file
    path_to_save = input("Enter the path to save the file: ")
    # C:/Users/eubgo/Desktop/POO/ASCIIMAGE/Boba.txt
    # C:/Users/eubgo/Desktop/POO/ASCIIMAGE/Chewie.txt
    try:
        with open(path_to_save, "w") as f:
            f.write(ascii_image)
    except:
        print(
            Colors.Underlined
            + Colors.Bold
            + Colors.Red
            + "Error:\n"
            + "Could not save the file to:\n"
            + Colors.Blue
            + Colors.Underlined
            + Colors.Bold
            + path_to_save
            + Colors.ResetAll
        )
        return

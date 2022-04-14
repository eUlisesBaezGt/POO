# from image2AsciiBW import *
from image2AsciiBW import *

if __name__ == "__main__":
    # Image to ASCII
    main()

#%%
import ascii_magic

art = ascii_magic.from_image_file(
    "C:/Users/eubgo/Desktop/POO/ASCIIMAGE/Chewie.jpg",
    columns=200,
    width_ratio=2,
    mode=ascii_magic.Modes.HTML,
)
ascii_magic.to_html_file("C:/Users/eubgo/Desktop/POO/ASCIIMAGE/Chewie.html", art)

art = ascii_magic.from_image_file(
    "C:/Users/eubgo/Desktop/POO/ASCIIMAGE/Boba.jpg",
    columns=200,
    width_ratio=2,
    mode=ascii_magic.Modes.HTML,
)
ascii_magic.to_html_file("C:/Users/eubgo/Desktop/POO/ASCIIMAGE/Boba.html", art)

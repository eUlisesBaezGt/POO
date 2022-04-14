# from image2AsciiBW import *
from ascii import *

if __name__ == '__main__':
    # Image to ASCII
    main()

#%%

import ascii_magic
my_art = ascii_magic.from_image_file('/home/eubgt/Desktop/POO/ASCIIMAGE/chewiePLUShan.jpg')
ascii_magic.to_terminal(my_art)
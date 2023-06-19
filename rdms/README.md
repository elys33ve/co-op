python and C scripts relating to images for the purpose of testing how images or
colors would show up on the front panel. There's some things I'd need to adjust
but since this was just to familiarize myself with how it works and I'll come
back to this later, i believe i'm moving on for the time being.


image_to_hex.py just takes an image and creates a txt file of the hex values for
each pixel.

show_test.c is just to test some things I was curious about but i may have
messed it up a bit so i'm not exactly sure what it does atm.

image_fb.c was for testing how best to take input from a txt file and convert
to 32 bit numbers to be used in write_fb.c

write_fb.c creates fb.bin from hex values provided for each pixel in an image
that will be shown on the front panel.

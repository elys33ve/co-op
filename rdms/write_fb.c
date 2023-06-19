// write a file that represents a raw framebuffer that could be dd'ed into an actual framebuffer.
// 1u lcds simple framebuffers are a8b8g8r8. the values written here are byte-reversed so they get dd'ed in
// correctly. alpha is ignored by the front panel

// (script to create fb.bin from hex values for pixels of an image)

/*
// compile and run to create the fb.bin file:
gcc -o write_fb write_fb.c && ./write_fb

// copy to the rdms:
scp fb.bin rdms@rdms-board:~/fb.bin

// on the RDMS, run this as root to copy it to the frame buffer
sudo dd if=./fb.bin of=/dev/fb0
sudo dd if=./fb.bin of=/dev/fb1
sudo dd if=./fb.bin of=/dev/fb2
sudo dd if=./fb.bin of=/dev/fb3
*/

#include <stdio.h>
#include <stdlib.h>

#define W 320
#define H 240

char data[(W*H*4)];


typedef struct Colors {
    int red, blue, green, purple;
} Colors;

Colors colors() {
    Colors c;
    c.red = 0x00FF0000;
    c.blue = 0x000000FF;
    c.green = 0x0000FF00;
    c.purple = 0x00FF00FF;
    
    return c;
}

///////////////////////////////////////////////////

// four_colors(c.blue, c.purple, c.red, c.green);
void four_colors(int top_left, int bottom_left, int top_right, int bottom_right) {
    int x, y, p, idx = 0;

    // write pixel data     (across > down)
    for (y=0; y<H; y++) {
        for (x=0; x<W; x++) {
            if (x<(W>>1)) { 
                if (y>(H>>1)) {     // left top
                    p = top_left;
                } else {            // left botton
                    p = bottom_left;
                }
            }
            else {
                if (y>(H>>1)) {     // right top
                    p = top_right;
                } else {            // right botton
                    p = bottom_right;
                }
            }
            data[idx++] = p;
            data[idx++] = p>>8;
            data[idx++] = p>>16;
            data[idx++] = p>>24;
        }
    }
}




// get bigass pixel values array (returns length of arr)
int get_hexarr(unsigned int *hexarr) {
    FILE *file;
    char hexstr[10];
    unsigned int hexval;
    int idx = 0;

    // get values from file into hexarr as int
    file = fopen("pixel_values.txt", "r");
    while(fgets(hexstr, 10, file)) {   
        hexval = (int)strtol(hexstr, NULL, 16);     // convert str to hex
        hexarr[idx] = hexval;                       // add to array
        idx++;
    }
    fclose(file);

    return idx;
}

///////////////////////////////////////////////////


int main() {
    FILE *fp;
    Colors c = colors();

    // open file
    fp = fopen("./fb.bin", "wb");
    if (!fp) {
        printf("Error opening file\n");
        exit(0);
    }

    ///////////////////
    unsigned int hexarr[307200], hexval;    // array for hexvals of img (i need to reajust the size bc panel is not this big)
    int len = get_hexarr(hexarr);
    int x, y, h_idx, b_idx, hex_color;

    h_idx = b_idx = 0;      // hexarr idx (4 bytes), data idx (1 byte)

    // write pixel data     (across > down)
    for (y=0; y<H; y++) {
        for (x=0; x<W; x++) {
            // pixel val from arr
            if (h_idx < len) {
                hex_color = hexarr[h_idx++];
            }
            // if hexarr out of range
            else {
                hex_color = 0x00FFFFF;      // white
            }

            // separate bytes and add to data
            data[b_idx++] = hex_color;
            data[b_idx++] = hex_color>>8;
            data[b_idx++] = hex_color>>16;
            data[b_idx++] = hex_color>>24;
        }
    }

    ///////////////////

    fwrite(data, sizeof(char), W*H*4, fp);
    fclose(fp);
    return 0;
}

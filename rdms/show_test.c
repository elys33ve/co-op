#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define W 16
#define H 12
char data[(W*H*4)];

/*  this script was just an attempt to print a little small scale diagram kinda thing
    to visualize the pixel values and things for the image (also to re-familiarize with
    simple bitwise operations in this context)
*/


// i dont feel like figuring out why math.h isnt working so
int log2ish(unsigned int n, int i) {
    int p = 1;
    for (int j=0; j<i; j++) { p = p * 2; }  // 2**i

    if (n <= p) { p = i; }
    else { p = log2ish(n, i+1); }

    return p;
}


// it kinda works a bit
void print_hex() {
    // print
    int idx = 0, zeros = 0, y, x, i;
    unsigned int d, d1, d2, d3, d4;
    for (y=0; y<H; y++) {
        for (x=0; x<W; x++) {
            d = d1 = d2 = d3 = d4 = 0;
            d1 = (data[idx++]<<0) & 0xFF; 
            d2 = (data[idx++]<<8) & 0xFF00;
            d3 = (data[idx++]<<16) & 0xFF0000;
            d4 = (data[idx++]<<24) & 0xFF000000;
            d = d1 | d2 | d3 | d4;

            zeros = (int)(8.0 - (log2ish(d, 1) / 4.0));
            for (i=0; i<zeros; i++) { printf("0"); }
            printf("%x ", d);
        }
        printf("\n");
    }
}



int main() {
    int x, y, p, i; 
    int idx = 0;

    // write pixel data     (across > down)
    for (y=0; y<H; y++) {
        for (x=0; x<W; x++) {

            if (x<(W>>1)) { 
                if (y>(H>>1)) {     // left bottom
                    p = 0x00FF0000;
                } else {            // left top
                    p = 0x000000FF;
                }
            }
            else {
                if (y>(H>>1)) {     // right bottom
                    p = 0x0000FF00;
                } else {            // right top
                    p = 0x00000000;
                }
            }
            data[idx++] = p;
            data[idx++] = p>>8;
            data[idx++] = p>>16;
            data[idx++] = p>>24;
        }
    }

    print_hex();

    return 0;
}

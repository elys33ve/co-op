#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*  C script i was using as a test for taking 8 char hex strings from an input
    text file and converting them to 32 bit numbers to store in a bigass array
*/

// take a hex string and convert it to a 32bit number (max 8 hex digits)

// str length function so it wont complain
int str_len(char str[]) {
    int len; 
    for (len=0; str[len] != '\0'; ++len);
    return len; 
}

// convert str of hex vals separated by space into arr of strs
// (only here bc i realized how unnecessary it was half way through)
void hex_arr(char file_line[]){
    char hexstr[9];
    int len, c_idx, l_idx, i;
    char null = '\0';

    len = strlen(file_line);
    
    // get individual strings for hex values
    c_idx = l_idx = 0;
    len = str_len(file_line);
    for (i=0; file_line[i] != null; i++) {
        // add chars to hexstr until space
        if (file_line[i] != ' '){
            hexstr[c_idx] = file_line[i];
            c_idx++;
        }
        else {
            hexstr[c_idx] = null;
            printf("%s\n", hexstr);
            c_idx = 0;
        }
    }

}



// get file length
int file_len(FILE *file){
    file = fopen("pixel_values.txt", "r");
    char line[10];
    int count = 0;

    while(fgets(line, 10, file)) { count++; }  
    fclose(file);
    
    return count;
}


// get bigass pixel values array (returns length of arr)
int get_hexarr(unsigned int *hexarr) {
    FILE *file;
    char hexstr[10];
    unsigned int hexval;
    int idx;

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


int main(){
    unsigned int hexarr[307200], hexval;
    int len = get_hexarr(hexarr);

  
    return 0;
}

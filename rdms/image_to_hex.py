from PIL import Image

# get hex color values for pixels in image

img = Image.open('beautiful.png')
pixels = img.load() 
width, height = img.size



def separate_space():
    file = open('pixel_values.txt', 'w')

    for y in range(height):   
        for x in range(width):  
            r, g, b, a = pixels[x, y]
            #print(x, y, f"#00{r:02x}{g:02x}{b:02x}")
            file.write(f"00{r:02x}{g:02x}{b:02x} ")
        file.write(f"\n")

    file.close()


def separate_newline():
    file = open('pixel_values.txt', 'w')

    count = 0
    for y in range(height):   
        for x in range(width):  
            r, g, b, a = pixels[x, y]
            file.write(f"00{r:02x}{g:02x}{b:02x}\n")
            count += 1
    
    print(x, y, count)
    file.close()



separate_newline()
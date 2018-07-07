from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
from main.TtfImageGenerator.values import *

# createdOn: 7 July, 2018
# bipinkh.github.io

def main():
    for key, value in fontFiles.items():
        custom_font =  ImageFont.truetype("../resources/ttf/"+key, font_size)
        font_image_folder = "../resources/font-images/"+key.lower().strip('.ttf')+"/"

        if not os.path.exists(font_image_folder):
            os.makedirs(font_image_folder)

        #draw image for each characters of each font
        count = 0
        for ch in value:
            ch = ch.strip()
            count += 1
            if (ch==''):
                continue
            im  =  Image.new ( "RGB", (width,height), back_ground_color )
            draw  =  ImageDraw.Draw ( im )
            draw.text ( (10,10), ch, font=custom_font, fill=font_color )
            im.save(font_image_folder+fileNames[count-1]+".jpg",'JPEG')


if __name__== "__main__":
  main()
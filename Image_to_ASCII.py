from PIL import Image, ImageDraw, ImageFont
import math
# Sotorkikoron: Python file & your image must be in the same directory.
# Darkest to lightest characters.
chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
charArray = list(chars)
charLength = len(charArray)
interval = charLength / 256

scaleFactor = 0.09

oneCharWidth = 10
oneCharHeight = 18


def getChar(inputInt):
    return charArray[math.floor(inputInt * interval)]


with open("Output.txt", "w") as text_file:
    # Open image file
    imj = Image.open("tumar_pic.jpg")

    # Load font
    fnt = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)

    # Resize image with correct aspect ratio
    width, height = imj.size
    im = imj.resize((int(scaleFactor * width), int(scaleFactor * height * (oneCharWidth / oneCharHeight))))
    width, height = im.size
    pix = im.load()

    # Create a new image for the output
    outputImage = Image.new('RGB', (oneCharWidth * width, oneCharHeight * height), color=(0, 0, 0))
    d = ImageDraw.Draw(outputImage)

    # Process each pixel and draw the ASCII art
    for i in range(height):
        for j in range(width):
            r, g, b = pix[j, i]
            # Convert to grayscale
            h = int(r * 0.2989 + g * 0.5870 + b * 0.1140)
            pix[j, i] = (h, h, h)
            # Write character to text file
            text_file.write(getChar(h))
            # Draw the character on the output image
            d.text((j * oneCharWidth, i * oneCharHeight), getChar(h), font=fnt, fill=(r, g, b))

        # End of line in the text file
        text_file.write('\n')

    # Save the output image
    outputImage.save('output.png')

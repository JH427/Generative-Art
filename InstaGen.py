#HEX INSTAGRAM POST IMAGE GENERATOR

from PIL import Image, ImageFont, ImageDraw

hexColor = '#420069'

textColor = '#ffffff'

img = Image.new('RGB', (250, 250), hexColor)

font = ImageFont.truetype('RobotoMono-Regular.ttf', 25)

imgEdit = ImageDraw.Draw(img)

imgEdit.text((0,0), hexColor, textColor, font=font)

img.save('test.png')

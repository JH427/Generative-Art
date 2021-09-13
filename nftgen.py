#HEX NFT GENERATOR

from PIL import Image

color = input('Enter a hex color (ex. #000000):')
pixel = Image.new('RGB', (1, 1), color)
original = Image.new('RGB', (250, 250), color)
fivehunnid = Image.new('RGB', (500, 500), color)

pixel.save('1//'+color+'.png')
original.save('250//'+color+'.png')
fivehunnid.save('500//'+color+'.png')



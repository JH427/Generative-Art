#HEX REMIX NFT GENERATOR

from PIL import Image

inner = '#420069'

outer = '#123456'

im1 = Image.new('RGB', (500, 500), outer)

im2 = Image.new('RGB', (250, 250), inner)

im1.paste(im2, (125,125))

im1.save('test.png')

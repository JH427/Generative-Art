#NFT ART GENERATOR

from PIL import Image
import random

allColorsNum = 16777215

baseColor = '#000000'

baseTuple = (500, 500)

def numToHex(n):
    return '#'+'%06x' % n

def randTuple(limit):
    a = random.randint(0, limit)
    b = random.randint(0, limit)
    return (a,b)

def genBox(dimension, color, point, im):
    img = Image.new('RGB', dimension, color)
    im.paste(img, point)

def genArt(n):
    im = Image.new('RGB', baseTuple, baseColor)
    for x in range(1000):
        genBox(randTuple(10), numToHex(random.randint(0,allColorsNum)),randTuple(500), im)
        
    im.save(n+'.png')

for x in range(100):
    genArt(str(x))

    


    



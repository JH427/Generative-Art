from PIL import Image, ImageFilter
import random

allColorsNum = 16777215

baseColor = '#000000'

baseTuple = (1584, 396)

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

def genPalette(n):
    palette = []
    for x in range(n):
        a = numToHex(random.randint(0,allColorsNum))
        palette.append(a)
    return palette

palette = ['#000000', '#BA0C2F', '#ffffff']
for i in range(20):
    baseImg = Image.new('RGB', baseTuple, baseColor)
    size = baseTuple
    palette = palette
    for x in range(11):
        n=35
        point = int((baseTuple[0]-size[0])/2)
        genBox(size, random.choice(palette),(point ,point),baseImg)
        size = (size[0]-n,size[1]-n)
    baseImg.save(str(i)+'.png')


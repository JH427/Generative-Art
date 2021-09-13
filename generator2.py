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

def genPalette(n):
    palette = []
    for x in range(n):
        a = numToHex(random.randint(0,allColorsNum))
        palette.append(a)
    return palette

#################

numbas = 20
for x in range(numbas):
    palette = genPalette(random.randint(1,10))
    baseImg = Image.new('RGB', baseTuple, baseColor)
    baseSize = baseTuple
    basePoint = (0,0)
    increment = random.randint(1,5)
    reductions = random.randint(1,int(baseSize[0]/2))
    minus = int(baseSize[0]/reductions)
    for x in range(reductions):
        #print(str(basePoint)+' '+str(baseSize))
        genBox(baseSize, random.choice(palette),basePoint, baseImg)
        basePoint = (basePoint[0]+increment, basePoint[1]+increment)
        baseSize = (baseSize[0]-minus,baseSize[1]-minus)
    baseImg.save(str(x)+'.png')


    
    
        

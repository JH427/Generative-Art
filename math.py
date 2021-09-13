baseSize = (10,10)

boxlimit = int(baseSize[0]/2)

minus = int(baseSize[0]/boxlimit)

inc = 1

point = (0,0)

size = baseSize

for x in range(boxlimit):
    print(str(point)+' '+str(size))
    point = (point[0]+inc, point[1]+inc)
    size = (size[0]-minus,size[1]-minus)
    



point1 =[]
point2 =[]

point1.append(int(input("点1のx座標=")))
point1.append(int(input("点1のy座標=")))
point2.append(int(input("点2のx座標=")))
point2.append(int(input("点2のy座標=")))

print([(point1[0]+point2[0])/2,(point1[1]+point2[1])/2])
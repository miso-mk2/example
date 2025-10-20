import math

teihen = int(input("直角三角形の底辺="))
takasa = int(input("直角三角形の高さ="))

print(f"斜辺の長さ={math.sqrt((teihen**2)+(takasa**2))}")
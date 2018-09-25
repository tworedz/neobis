from math import atan
import math
ab = int(input())
bc = int(input())
sol = atan(ab/bc)
ang = sol*180/math.pi
print(('{}°').format(round(ang)))

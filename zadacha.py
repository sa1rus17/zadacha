import math
a = float(input("введите число: "))


z1 = (1 - (2*math.sin(a)**2)) / (1 + (math.sin(a)*2))
print(z1)
z2 = (1 - math.tan(a)) / (1  + math.tan(a))
print(z2)

import math

v = 0
while v < 10:
    a = int(input("please enter the length of leg 1"))
    b = int(input("please enter the length of leg 2"))
    a_2 = a**2
    b_2 = b**2
    c_2 = a_2 + b_2
    c = math.sqrt(c_2)
    print(c)

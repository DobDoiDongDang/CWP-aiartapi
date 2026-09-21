#inlcude stdio.h
import math
numba = input("Give me a number: ")
if math.floor(float(numba)) != float(numba):
    print("This number is an dicimal.")
else:
    print("This number is an integer")

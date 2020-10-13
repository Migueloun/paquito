from random import random
from math import sqrt

if __name__ == "__main__":
    positivos = 0
    total = 12000000

    for i in range(0,total):
        x, y = random(), random()
        r = sqrt(x**2 + y**2)

        if r<=1:
            positivos += 1

    pi = 4*positivos/total
    
    print(pi)

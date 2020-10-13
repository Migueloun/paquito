import multiprocessing as mp
from random import random
from math import sqrt

def mini_pi(n):
    positivos = 0

    for i in range(0,n):
        x, y = random(), random()
        r = sqrt(x**2 + y**2)

        if r<=1:
            positivos += 1

    return positivos

if __name__ == "__main__":
    cores = int(mp.cpu_count()/2)
    positivos = 0
    total = 12000000

    segmentos = [int(total/cores) for i in range(cores)]

    with mp.Pool(processes=cores) as pool:
        positivos = pool.map(mini_pi, segmentos)

    pi = sum(positivos)*4.0/total
    print(pi)

import numpy as np

if __name__ == "__main__":
    
    #Dimensiones de la imagen
    N = 5
    M = N - 2
    
    A = np.random.randn(N, N)
    H = np.zeros((M,M))
    H[int(M/2)][int(M/2)] = 1.0
    
    edge = 
    for i in range(edge, N - edge):
        
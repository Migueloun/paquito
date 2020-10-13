import numpy as np

if __name__ == "__main__":
    
    N = 3
    
    A = np.random.randn(N, N)
    B = np.identity(N)
    C = np.zeros((N, N))
    
    for row in range(0, len(A)):
        
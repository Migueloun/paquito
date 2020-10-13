import numpy as np

if __name__ == "__main__":
    
    N = 256
    
    A = np.random.randn(N, N)
    B = np.identity(N)
    C = np.zeros((N, N))
    
    print(A)
    print(C)
    
    for row in range(0, len(A)):
        for col in range(0, N):
            for k in range(0, N):
                C[row][col] += A[row][k]*B[k][col]
                
    print(C)
import numpy as np
from multiprocessing import shared_memory, Process

if __name__ == "__main__":
    
    N = 3
    
    A = np.random.randn(N, N)
    B = np.identity(N)
    
    ptr = shared_memory.SharedMemory(name='C', create=True, size=A.nbytes)
    C = np.ndarray(B.shape, dtype=np.float64, buffer=ptr.buf)
    
    print(A)
    print(C)
    
    for row in range(0, len(A)):
        for col in range(0, N):
            for k in range(0, N):
                C[row][col] += A[row][k]*B[k][col]
                
    print(C)
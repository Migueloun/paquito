import numpy as np
from multiprocessing import shared_memory, Process

def matrix_multiply(row):
    
    for col in range(0, N, 1):
        for k in range(0, N, 1):
            C[row][col] += A[row][k]*B[k][col]
            
if __name__ == "__main__":
    
    N = 512
    
    A = np.random.randn(N, N)
    B = np.identity(N)
    
    ptr = shared_memory.SharedMemory(create=True, size=A.nbytes)
    C = np.ndarray(B.shape, dtype=np.float64, buffer=ptr.buf)
    
    print(A)
    print(C)
    
    jobs = []
    for row in range(0, N):
        p = Process(target=matrix_multiply, args=(row,))
        jobs.append(p)
        p.start()
        
    for p in jobs:
        p.join()
    
    """
    for row in range(0, len(A)):
        for col in range(0, N):
            for k in range(0, N):
                C[row][col] += A[row][k]*B[k][col]
                
    """
    print(C)
    
    ptr.unlink()
    ptr.close()
from numba import jit,cuda
import numpy as np
from timeit import default_timer as timer

def func(a):
    for i in range(100_000_000):
        a[i]+=1


@jit(target_backend='cuda')
def func_gpu(a):
    for i in range(100_000_000):
        a[i]+=1

if __name__ == '__main__':
    n = 100_000_000
    a = np.ones(n,dtype=np.float64)

    start = timer()
    func(a)
    print(f'funkcja CPU  czas wykonania: {timer()-start} s')

    start = timer()
    func_gpu(a)
    print(f'funkcja GPU  czas wykonania: {timer() - start} s')

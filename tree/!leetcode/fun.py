import numpy as np
import time
import numba
from numba import jit

# @jit(nopython=True)
def go_fast(a): # 首次调用时，函数被编译为机器代码
    trace = 0
    # 假设输入变量是numpy数组
    for i in range(a.shape[0]):   # Numba 擅长处理循环
        trace += np.tanh(a[i, i])  # numba喜欢numpy函数
    return a + trace # numba喜欢numpy广播

x = np.arange(100000000).reshape(10, 10000000)
start=time.time()
go_fast(x)
end=time.time()
print(end-start)
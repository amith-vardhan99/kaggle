import numpy as np
import pandas as pd
from math import *

class EncodeBinary():
    def bin_to_dec(self,num):
        n = num
        st = []
        ctr = 0
        while n>0:
            r = int(n % 2)
            n = int(n / 2)
            st.append(r)
        fin = st[::-1]
        return fin

    def unify_binary_length(self,arr):
        length = []
        for i in arr:
            length.append(len(i))
        max_len = max(length)
        fin = []
        for i in arr:
            if len(i)!=max_len:
                z = np.zeros(max_len-len(i))
                z = z.astype("int")
                t = list(z)
                fin.append((t+i))
            else:
                fin.append(i)
        return fin
    def column_names(name,col_num):
        lis = []
        for i in range(0,col_num):
            lis.append(name+"_"+str(col_num))
        return lis
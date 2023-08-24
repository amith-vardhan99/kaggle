import numpy as np
import pandas as pd
class EncodeBinary:
    def dec_to_bin(self,num):
        n = num
        st = []
        ctr = 0
        while n > 0:
            r = int(n % 2)
            n = int(n / 2)
            st.append(r)
        fin = st[::-1]
        return fin
    def max_len_bin(self,x,lt):
        ctr = len(x)
        u = np.zeros(lt-ctr)
        v = u.astype("int")
        t = list(v)
        f = t + x
        return f
    def column_names(self,nam,col_num):
        lis = []
        for i in range(0,col_num):
            t = nam+"_"+str(i)
            lis.append(t)
        return lis
    def binary_enc(self,x):
        bin_convert = lambda x: dec_to_bin(x)
        bin_list = list(map(bin_convert,x))
        len_of_each_ele = lambda x: len(x)
        max_len = max(list(map(len_of_each_ele,bin_list)))
        optimi_bin = lambda x: max_len_bin(x,max_len)
        bin_stabi = list(map(optimi_bin,bin_list))
        cols = column_names(x.name,max_len)
        df_num = pd.DataFrame(bin_stabi,columns=cols)
        return df_num
#%%

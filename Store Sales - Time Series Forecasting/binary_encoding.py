import numpy as np
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
        if ctr < lt:
            u = np.zeros(lt-ctr)
            v = u.astype("int")
            t = list(v)
            f = t + x
        else:
            f = x
        return f
    def column_names(self,nam,col_num):
        lis = []
        for i in range(0,col_num):
            t = nam+"_"+str(i)
            lis.append(t)
        return lis
#%%

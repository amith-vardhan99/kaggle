import numpy as np
class EncodeBinary:
    def dec_to_bin(num):
        n = num
        st = []
        ctr = 0
        while n > 0:
            r = int(n % 2)
            n = int(n / 2)
            st.append(r)
        fin = st[::-1]
        return fin
    def max_len_bin(x,lt):
        ctr = len(x)
        u = np.zeros(lt-ctr)
        v = u.astype("int")
        t = list(v)
        f = t + x
        return f
    def column_names(nam,col_num):
        lis = []
        for i in range(0,col_num):
            t = nam+"_"+str(i)
            lis.append(t)
        return lis
class Solution:
    def rearrange(self,arr):
        # code here
        p = []
        n = []
        l = len(arr)
        for num in arr:
            if num>=0:
                p.append(num)
            else:
                n.append(num)
        # print(p)
        # print(n)
        i = 0
        j = 0
        x = len(p)
        y = len(n)
        brr = []
        while(i<x and j<y):
            brr.append(p[i])
            brr.append(n[j])
            # print(brr)
            i += 1
            j += 1
        while(i<x):
            brr.append(p[i])
            i += 1
        while(j<y):
            brr.append(n[j])
            j += 1
        arr[:] = brr

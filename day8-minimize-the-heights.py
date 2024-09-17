class Solution:
    def getMinDiff(self, arr,k):
        # code here
        arr.sort()
        l = len(arr)
        if l==1:
            return 0
        smallest = arr[0]+k
        largest = arr[-1]-k
        mini = arr[-1]-arr[0]
        
        for i in range(l-1):
            h = max(largest,arr[i]+k)
            l = min(smallest,arr[i+1]-k)
            if l<0:
                continue
            mini = min(mini,h-l)
        return mini

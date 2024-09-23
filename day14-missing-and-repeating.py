class Solution:
    def findTwoElement(self,arr): 
        n = len(arr)
        duplicate = -1
        for i in range(n):
            index = abs(arr[i]) - 1
            if arr[index] < 0:
                duplicate = abs(arr[i])
            else:
                arr[index] = -arr[index]
    
        missing = -1
        for i in range(n):
            if arr[i] > 0:
                missing = i + 1
                break
    
        return (duplicate, missing)

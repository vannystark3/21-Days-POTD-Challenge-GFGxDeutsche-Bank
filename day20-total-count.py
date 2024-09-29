class Solution:
    def totalCount(self, k, arr):
        # code here
        total_count = 0
        for x in arr:
            total_count += (x + k - 1) // k
        return total_count

import heapq
class Solution:
    #Function to return the minimum cost of connecting the ropes.
    def minCost(self, arr):
        if not arr or len(arr)==1:
            return 0
        
        heapq.heapify(arr)
        total_cost = 0
        
        while len(arr) > 1:
            first = heapq.heappop(arr)
            second = heapq.heappop(arr)
            cost = first + second
            total_cost += cost
            heapq.heappush(arr, cost)
        
        return total_cost

from collections import defaultdict, deque

class Solution:
    def isCircle(self, arr):
        # code here
        if not arr:
            return 0
        
        outd = defaultdict(int)
        ind = defaultdict(int)
        graph = defaultdict(set)
        
        # print()
        for s in arr:
            start = s[0]
            end = s[-1]
            outd[start] += 1
            ind[end] += 1
            graph[start].add(end)
        
        edges = set(outd.keys()).union(set(ind.keys()))
        # print(edges)
        for char in edges:
            if(outd[char]!=ind[char]):
                return 0
        if not edges:
            return 1
        
        def bfs(start):
            visited = set()
            q = deque([start])
            # print(q)
            while q:
                node = q.popleft()
                if node in visited:
                    continue
                visited.add(node)
                for n in graph[node]:
                    if n not in visited:
                        q.append(n)
            return visited
            # print(node)
        
        # print(bfs(next(iter(edges))))
        visited_nodes = bfs(next(iter(edges)))
        if(visited_nodes==edges):
            return 1
        else:
            return 0

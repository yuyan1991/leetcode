class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for i in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        visit = [False] * n
        parent = [-1] * n
        longestChain = [0] * n
        longestChainNode = [-1] * n
        secondLongestChain = [0] * n
        parentLongestChain = [0] * n
        stack = [[-1, 0]] * n
        for i in range(n):
            if not visit[i]:
                stack[0] = [i, 0]
                stackSize = 1
                while stackSize > 0:
                    u, cur = stack[stackSize - 1]
                    visit[u] = True
                    newNodeFound = False
                    while cur < len(graph[u]):
                        v = graph[u][cur]
                        if not visit[v]:
                            newNodeFound = True
                            parent[v] = u
                            stack[stackSize - 1][1] = cur + 1
                            stack[stackSize] = [v, 0]
                            stackSize += 1
                            break
                        cur += 1
                    if newNodeFound:
                        continue
                    stackSize -= 1
                    if stackSize > 0:
                        u, v = stack[stackSize - 1][0], u
                        if longestChain[v] + 1 > longestChain[u]:
                            longestChain[u], secondLongestChain[u] = longestChain[v] + 1, longestChain[u]
                            longestChainNode[u] = v
                        elif longestChain[v] + 1 > secondLongestChain[u]:
                            secondLongestChain[u] = longestChain[v] + 1
        minimumHeight = 1 << 30
        ans = []
        visit = [False] * n
        for i in range(n):
            if not visit[i]:
                stack[0] = [i, 0]
                if longestChain[i] < minimumHeight:
                    minimumHeight = longestChain[i]
                    ans = []
                if longestChain[i] == minimumHeight:
                    ans.append(i)
                stackSize = 1
                while stackSize > 0:
                    u, cur = stack[stackSize - 1]
                    visit[u] = True
                    newNodeFound = False
                    while cur < len(graph[u]):
                        v = graph[u][cur]
                        if not visit[v]:
                            newNodeFound = True
                            if longestChainNode[u] == v:
                                parentLongestChain[v] = max(parentLongestChain[u], secondLongestChain[u]) + 1
                            else:
                                parentLongestChain[v] = max(parentLongestChain[u], longestChain[u]) + 1
                            height = max(parentLongestChain[v], longestChain[v])
                            if height < minimumHeight:
                                minimumHeight = height
                                ans = []
                            if minimumHeight == height:
                                ans.append(v)
                            stack[stackSize - 1][1] = cur + 1
                            stack[stackSize] = [v, 0]
                            stackSize += 1
                            break
                        cur += 1
                    if newNodeFound:
                        continue
                    stackSize -= 1
        return ans
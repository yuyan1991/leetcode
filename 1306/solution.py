class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        isArrived = [False for i in range(len(arr))]
        self.reach(arr, isArrived, start)
        for i, a in enumerate(arr):
            if isArrived[i] and a == 0:
                return True
        return False
    
    def reach(self, arr, isArrived, current):
        isArrived[current] = True
        if current - arr[current] >= 0 and not isArrived[current - arr[current]]:
            self.reach(arr, isArrived, current - arr[current])
        if current + arr[current] < len(arr) and not isArrived[current + arr[current]]:
            self.reach(arr, isArrived, current + arr[current])

import heapq
class Solution:
    def mergeKArrays(self, arr, K):
        merged = []
        heap = []

        for i in range(K):
            heapq.heappush(heap, (arr[i][0], i, 0))

        while heap:
            val, row, col = heapq.heappop(heap)
            merged.append(val)

            if col+1 < K:
                heapq.heappush(heap, (arr[row][col+1], row, col+1))

        return merged


K = 4
arr = [[1,2,3,4],[2,2,3,4],
         [5,5,6,6],[7,8,9,9]]

obj = Solution()
print(obj.mergeKArrays(arr, K))

class Solution(object):
    def maxDistToClosest(self, seats):
        prev, max_len = 0, 0
        
        for cur, seat in enumerate(seats):
            if seat:
                if seats[prev]:
                    max_len = max(max_len, (cur - prev) // 2)
                else:
                    max_len = max(max_len, (cur - prev))
                prev = cur
                
        if seats[prev]: 
            max_len = max(max_len, len(seats) - 1 - prev) 
                
        return max_len
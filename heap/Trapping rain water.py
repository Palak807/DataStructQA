class Solution(object):
    def trap(self, height):
        
        if not height:
            return None

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        ans = 0

        while l < r:
            if leftMax < rightMax :
                l += 1
                leftMax = max(leftMax, height[l])
                ans += leftMax - height[l]

            else :
                r -= 1
                rightMax = max(rightMax, height[r])
                ans += rightMax - height[r]
        
        return ans

obj = Solution()

height = [0,1,0,2,1,0,1,3,2,1,2,1]

print(obj.trap(height))
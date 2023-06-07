class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []
        
        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                if abs(asteroid) > stack[-1]:
                    stack.pop()
                    continue
                elif abs(asteroid) == stack[-1]:
                    stack.pop()
                break
            else:
                stack.append(asteroid)

        return stack



value = [10, 2, -5]
obj = Solution()
print(obj.asteroidCollision(value))

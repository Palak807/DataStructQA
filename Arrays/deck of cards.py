class Solution:
    def hasGroupsSizeX(self, deck) -> bool:
        
        freq = {}
        for num in deck:
            freq[num] = freq.get(num, 0) + 1
        
        values = list(freq.values())
        
        gcd_val = self.calculate_gcd(values)
        
        return gcd_val >= 2
    
    def calculate_gcd(self, nums):
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
    
        gcd_val = nums[0]
        for i in range(1, len(nums)):
            gcd_val = gcd(gcd_val, nums[i])
        
        return gcd_val

            
        
deck = [1,1,1,2,2,2,3,3,3]

obj = Solution()
print(obj.hasGroupsSizeX(deck))
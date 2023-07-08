class Solution(object):
    def maximumSwap(self, num):

        digits = list(str(num))
        
        mapper = {}

        for i in range(len(digits)):
            mapper[int(digits[i])] = i
        
        print(mapper)
        
        for k, digit in enumerate(digits):
            for j in range(9, int(digit), -1):
                if j in mapper and mapper[j] > k:
                    digits[k], digits[mapper[j]] = digits[mapper[j]], digits[k]
                    return int(''.join(digits))
        
        return num

obj = Solution()
print(obj.maximumSwap(2417))
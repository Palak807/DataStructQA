class Solution:
    def multiply(self, num1, num2):
        d1 = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        d2 = {v:k for k,v in d1.items()}
        n1 = sum([d1[c]*(10**i) for i,c in enumerate(num1[::-1])])
        n2 = sum([d1[c]*(10**i) for i,c in enumerate(num2[::-1])])
        n3, s = n1*n2, ''
        while n3:
            s = d2[n3%10] + s
            n3 = n3//10
        return s if s else '0'

obj = Solution()
print(obj.multiply("87","2"))
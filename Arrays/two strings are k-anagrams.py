class Solution:
    def areKAnagrams(self, str1, str2, k):
        mapper_1 = {}
        mapper_2 = {}
        counter = 0

        if len(str1) == len(str2):
            for i in range(len(str1)):
                mapper_1[str1[i]] = mapper_1.get(str1[i], 0) + 1

            for j in range(len(str2)):
                mapper_2[str2[j]] = mapper_2.get(str2[j], 0) + 1

            for key in mapper_1:
                if mapper_1[key] != mapper_2.get(key, 0):
                    counter += 1
            
            if counter <= k :
                return True

        return False

obj = Solution()
print(obj.areKAnagrams("xxxxyyzz", "xxxyysaz", 7))

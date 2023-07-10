class Solution(object):
    def pushDominoes(self, dominoes):

        temp = ''
        
        while dominoes != temp:
            temp = dominoes
            dominoes = dominoes.replace('R.L', '-')       
            dominoes = dominoes.replace('R.', 'RR')         
            dominoes = dominoes.replace('.L', 'LL')         

        return  dominoes.replace('-', 'R.L')             
    
obj = Solution()
dominoes = ".L.R...LR..L.."
print(obj.pushDominoes(dominoes))

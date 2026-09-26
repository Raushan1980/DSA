class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mul = 1
        sum = 0

        while n>0:
            place = n% 10
            mul = mul * place
            sum = sum+place
            n = n //10
        
        return mul-sum
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # x^ -n = 1/x^n
        def help(x,n):
            if x==0: return 0
            if n==0: return 1
            #these will be the base case
            
            #x * x^2* x^2 = x^5
            res = help(x,n//2)
            res =  res * res
            return x*res if n % 2 else res
            
            
        res = help(x,abs(n))
        return res if n >= 0 else 1/res

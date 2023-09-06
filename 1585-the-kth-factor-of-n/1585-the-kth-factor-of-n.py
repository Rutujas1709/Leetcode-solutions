class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        print(n)
        print(k)   
        temp = [] 
        for i in range(1, n + 1): 
            if n % i == 0:
                temp.append(i)
        if k <= len(temp):
            return temp[k - 1] 
        else:
            return -1  


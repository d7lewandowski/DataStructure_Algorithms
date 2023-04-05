# Problem discussion 

# Given N bulbs, either on (1) or off (0).
# Turing on ith bulbs causes all remaining bulbs on the right to flip.

# Purpose:
# Find the min number of switches to turn all the bulbs on.

# Constraints: 
# - 1 <= N <= 1e5
# - A[i] = {0, 1}



class Solution:

    def bulbs(self, A): # [0, 1, 0]
        
        cost = 0 

        for b in A:  
            if cost % 2 == 0: 
                b = b 
            else: 
                b = not b 

            if b % 2 == 1:
                continue
            else: 
                cost += 1 
        
        return cost


s = Solution()
print(s.bulbs([0,1,0]))
print(s.bulbs([0,1,0,1,0,0,0,1]))
print(s.bulbs([0,0,0,0,0,0]))
print(s.bulbs([1,1,1,1,1,1,1]))



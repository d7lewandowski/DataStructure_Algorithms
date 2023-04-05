# Problem discussion 

# Given an array of N integers.

# Find the hightest product by multiplying 3 elements.
# Constraints: 
# - N between 3 and 5e5


#  - Take the hightest 3 elements is not enought solution consider list of number: [-5,-5,-2,0,1,2,3] -> 1 * 2 * 3 < -5 * -5 * 3 

# So consider: lowest 2 and highest 1 and we compere result of 3 highest elements with lowest 2 and 1 hightest. 


class Solution:

    def maxp3(self, A):

        A = sorted(A)

        hi3 = A[-1] * A[-2] * A[-3]

        lo2hi1 = A[0] * A[1] * A[-1]


        return max(hi3, lo2hi1)




s = Solution()
print(s.maxp3([-5, -5, -2, 0, 1, 2, 3]))

print(s.maxp3([-5, -2, 0, 1, 2]))
print(s.maxp3([-10, -5, -2, 0, 1, 2, 3]))
print(s.maxp3([ 0, 1, 2, 3]))

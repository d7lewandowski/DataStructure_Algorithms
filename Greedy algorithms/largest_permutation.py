"""
Given an array A of a random permuation number from 1 to N.
Given B, the number of swaps in A that we can make.
"""

# Find the largest permuation possible

# Constraints
# - N between 1 and 1e6
# - B between 1 and 1e9


class Solution:

    def largest_permutation(self, A, B): # [2, 4, 3] 2

        i = 0 

        _max = len(A) # 3
        d = {x: i for i, x in enumerate(A)} #  {2: 0, 4: 1, 3: 2}
        print(A)

        print(d)

        while B and i < len(A):

            j = d[_max]

            if i == j:
                pass
            else:
                B -= 1
                A[i], A[j] = A[j], A[i]
                d[A[i]], d[A[j]] = d[A[j]], d[A[i]] 
            i += 1
            _max -= 1

        return A

#############################


s = Solution()
print(s.largest_permutation([2,4,3], 2))

print(s.largest_permutation([3,2,4,1,5], 3))

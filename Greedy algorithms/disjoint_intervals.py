# Given a list of intervals: [start, end].
# Find the length of the maximal set of mutually disjoint intervals.
# Constraints: 
# - 1 <= N <= 1e5
# - 1 <= A[i][0] <= A[i][1] <= 1e9



class Solution:
    
    # @param A: list of list of int
    # @return an int

    def solve(self, A):

        A.sort(key=lambda x: x[1])

        prev_s, prev_e = A[0]

        count = 1

        for s, e in A:

            if s <= prev_e:
                pass
            else:
                prev_s, prev_e = s, e
                count += 1

        return count 


s = Solution()
print(s.solve([[1,2], [3, 5], [7, 9]]))

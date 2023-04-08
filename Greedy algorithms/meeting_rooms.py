'''
Given a list of intervals: {s, e} for meetings.

Find the least number of meeting rooms required.

Constraints:
    - 1 <= N <= 1e5
    - 1 <= A[i][0] <= Ai[[1] <= 1e9]
'''

class Solution:
    # @param A: list of list of intergers 
    # @return an integer 


    def solve(self, A):

        data = []

        for s, e in A:
            data.append((s, +1))
            data.append((e, -1)) 
        
        data.sort()
        print(data) 

        curr = 0
        ans = 0

        for _, v in data:

            curr += v
            ans = max(ans, curr)

        return ans


s = Solution()
print(s.solve([[1,5], [2,6], [7,8]]))

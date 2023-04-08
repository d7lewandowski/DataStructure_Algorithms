'''
Seats

There is a row of empty (.)
and filles(x) seats.

Find the minimum number of moves
required to make the people sit toghter.

Constraints: 
    - 1 <= N <= 1e6
'''


class Solution:
    # @ param A: String
    # @ retrun an int

    def solve(self, A):
        MOD = 10000003

        crosses = [i for i, c in enumerate(A) if c == 'x']
        crosses = [(cross - 1) for i, cross in enumerate(crosses)]
        
        n = len(crosses)

        if n == 0:
            return 0

        ans = float('inf')

        # for segment_start in range(len(A)):
        segment_start = crosses[n // 2]   
        total = 0

        for cross in crosses:
                
            total += abs(cross - segment_start)

            total %= MOD


        ans = min(ans, total % MOD)
        return ans 


s = Solution()

print(s.solve('x..xx'))


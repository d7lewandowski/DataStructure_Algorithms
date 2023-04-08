'''
N kids sdand in a line, each 
having an integer rating. We 
distribute candies following:
    - Each kid gets at least 1 candy
    - Kinds with higher raitings than
    theri neighbours get more candies.

Find the minimum candies required.

Constraints:
    1 <= N <= 1e5
'''

class Solution:

    def solve(self, A):

        n = len(A)

        data = sorted((x, i) for i, x in enumerate(A))


        candies = [1] * n


        for _, i in data:

            if i > 0 and A[i] > A[i-1]:
                print(A[i - 1])
                candies[i] = max(candies[i], candies[i - 1] + 1)

            if i < n - 1 and A[i] > A[i + 1]:

                candies[i] = max(candies[i], candies[i+1] + 1)

        return sum(candies)

s = Solution()

print(s.solve([1, 2, 7, 4, 3, 3, 1]))

print(s.solve([1, 2, 7, 4]))

# 1. BULBS
Problem discussion 

Given N bulbs, either on (1) or off (0).
Turing on ith bulbs causes all remaining bulbs on the right to flip.

Purpose:
Find the min number of switches to turn all the bulbs on.

Constraints: 
 - 1 <= N <= 1e5
 - A[i] = {0, 1}

# 2. Disjoint intervals
Problem discussion

Given a list of intervals: [start, end].
Find the length of the maximal set of mutually disjoint intervals.
Constraints: 
 - 1 <= N <= 1e5
 - 1 <= A[i][0] <= A[i][1] <= 1e9

# 3. Highest product

Problem discussion 

Given an array of N integers.

Find the hightest product by multiplying 3 elements.
Constraints: 

- N between 3 and 5e5

- Take the hightest 3 elements is not enought solution consider list of number: [-5,-5,-2,0,1,2,3] -> 1 * 2 * 3 < -5 * -5 * 3 

So consider: lowest 2 and highest 1 and we compere result of 3 highest elements with lowest 2 and 1 hightest. 



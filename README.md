NQueens Problem with Solutions (recursively and iteratively)

# Data Structures, SOFE2715U
### Assignment #01

### Instructor: Dr. Shahryar Rahnamayan, PEng, SMIEEE

### Prepared by:
Samantha Husack (100617713)


### Due: 
Friday, February 9th 2018, before 11:59PM


## Problem Statement
Solve N-Queen problem using:
* An iterative method, and
* A recursive method
For N = 8 and N = 9

## N-Queen Problem
The Queen’s puzzle is the problem of placing N chess queens on a NXN chessboard so that no two queens threaten each other. Thus, the solution requires that no two queens share the same row, column or diagonal.

To find all possible solutions to this problem, a backtracking method is performed to calculate all possible solutions from all possible combinations. This method allows for every single solution to be found, although it is a very time-costing method. 


### a) PseudoCode for Recursive and Iterative Methods

### b) Programs and Comments
  i) Recursive : recusive_2.py
  ii) Iterative : iterative_nqueens.py

### c) All Solutions for N=8 & N=9

***N = 8***
Solution #1: [0, 4, 7, 5, 2, 6, 1, 3]
Solution #2: [0, 5, 7, 2, 6, 3, 1, 4]
Solution #3: [0, 6, 3, 5, 7, 1, 4, 2]
Solution #4: [0, 6, 4, 7, 1, 3, 5, 2]
Solution #5: [1, 3, 5, 7, 2, 0, 6, 4]
Solution #6: [1, 4, 6, 0, 2, 7, 5, 3]
Solution #7: [1, 4, 6, 3, 0, 7, 5, 2]
Solution #8: [1, 5, 0, 6, 3, 7, 2, 4]
Solution #9: [1, 5, 7, 2, 0, 3, 6, 4]
Solution #10: [1, 6, 2, 5, 7, 4, 0, 3]
Solution #11: [1, 6, 4, 7, 0, 3, 5, 2]
Solution #12: [1, 7, 5, 0, 2, 4, 6, 3]
Solution #13: [2, 0, 6, 4, 7, 1, 3, 5]
Solution #14: [2, 4, 1, 7, 0, 6, 3, 5]
Solution #15: [2, 4, 1, 7, 5, 3, 6, 0]
Solution #16: [2, 4, 6, 0, 3, 1, 7, 5]
Solution #17: [2, 4, 7, 3, 0, 6, 1, 5]
Solution #18: [2, 5, 1, 4, 7, 0, 6, 3]
Solution #19: [2, 5, 1, 6, 0, 3, 7, 4]
Solution #20: [2, 5, 1, 6, 4, 0, 7, 3]
Solution #21: [2, 5, 3, 0, 7, 4, 6, 1]
Solution #22: [2, 5, 3, 1, 7, 4, 6, 0]
Solution #23: [2, 5, 7, 0, 3, 6, 4, 1]
Solution #24: [2, 5, 7, 0, 4, 6, 1, 3]
Solution #25: [2, 5, 7, 1, 3, 0, 6, 4]
Solution #26: [2, 6, 1, 7, 4, 0, 3, 5]
Solution #27: [2, 6, 1, 7, 5, 3, 0, 4]
Solution #28: [2, 7, 3, 6, 0, 5, 1, 4]
Solution #29: [3, 0, 4, 7, 1, 6, 2, 5]
Solution #30: [3, 0, 4, 7, 5, 2, 6, 1]
Solution #31: [3, 1, 4, 7, 5, 0, 2, 6]
Solution #32: [3, 1, 6, 2, 5, 7, 0, 4]
Solution #33: [3, 1, 6, 2, 5, 7, 4, 0]
Solution #34: [3, 1, 6, 4, 0, 7, 5, 2]
Solution #35: [3, 1, 7, 4, 6, 0, 2, 5]
Solution #36: [3, 1, 7, 5, 0, 2, 4, 6]
Solution #37: [3, 5, 0, 4, 1, 7, 2, 6]
Solution #38: [3, 5, 7, 1, 6, 0, 2, 4]
Solution #39: [3, 5, 7, 2, 0, 6, 4, 1]
Solution #40: [3, 6, 0, 7, 4, 1, 5, 2]
Solution #41: [3, 6, 2, 7, 1, 4, 0, 5]
Solution #42: [3, 6, 4, 1, 5, 0, 2, 7]
Solution #43: [3, 6, 4, 2, 0, 5, 7, 1]
Solution #44: [3, 7, 0, 2, 5, 1, 6, 4]
Solution #45: [3, 7, 0, 4, 6, 1, 5, 2]
Solution #46: [3, 7, 4, 2, 0, 6, 1, 5]
Solution #47: [4, 0, 3, 5, 7, 1, 6, 2]
Solution #48: [4, 0, 7, 3, 1, 6, 2, 5]
Solution #49: [4, 0, 7, 5, 2, 6, 1, 3]
Solution #50: [4, 1, 3, 5, 7, 2, 0, 6]
Solution #51: [4, 1, 3, 6, 2, 7, 5, 0]
Solution #52: [4, 1, 5, 0, 6, 3, 7, 2]
Solution #53: [4, 1, 7, 0, 3, 6, 2, 5]
Solution #54: [4, 2, 0, 5, 7, 1, 3, 6]
Solution #55: [4, 2, 0, 6, 1, 7, 5, 3]
Solution #56: [4, 2, 7, 3, 6, 0, 5, 1]
Solution #57: [4, 6, 0, 2, 7, 5, 3, 1]
Solution #58: [4, 6, 0, 3, 1, 7, 5, 2]
Solution #59: [4, 6, 1, 3, 7, 0, 2, 5]
Solution #60: [4, 6, 1, 5, 2, 0, 3, 7]
Solution #61: [4, 6, 1, 5, 2, 0, 7, 3]
Solution #62: [4, 6, 3, 0, 2, 7, 5, 1]
Solution #63: [4, 7, 3, 0, 2, 5, 1, 6]
Solution #64: [4, 7, 3, 0, 6, 1, 5, 2]
Solution #65: [5, 0, 4, 1, 7, 2, 6, 3]
Solution #66: [5, 1, 6, 0, 2, 4, 7, 3]
Solution #67: [5, 1, 6, 0, 3, 7, 4, 2]
Solution #68: [5, 2, 0, 6, 4, 7, 1, 3]
Solution #69: [5, 2, 0, 7, 3, 1, 6, 4]
Solution #70: [5, 2, 0, 7, 4, 1, 3, 6]
Solution #71: [5, 2, 4, 6, 0, 3, 1, 7]
Solution #72: [5, 2, 4, 7, 0, 3, 1, 6]
Solution #73: [5, 2, 6, 1, 3, 7, 0, 4]
Solution #74: [5, 2, 6, 1, 7, 4, 0, 3]
Solution #75: [5, 2, 6, 3, 0, 7, 1, 4]
Solution #76: [5, 3, 0, 4, 7, 1, 6, 2]
Solution #77: [5, 3, 1, 7, 4, 6, 0, 2]
Solution #78: [5, 3, 6, 0, 2, 4, 1, 7]
Solution #79: [5, 3, 6, 0, 7, 1, 4, 2]
Solution #80: [5, 7, 1, 3, 0, 6, 4, 2]
Solution #81: [6, 0, 2, 7, 5, 3, 1, 4]
Solution #82: [6, 1, 3, 0, 7, 4, 2, 5]
Solution #83: [6, 1, 5, 2, 0, 3, 7, 4]
Solution #84: [6, 2, 0, 5, 7, 4, 1, 3]
Solution #85: [6, 2, 7, 1, 4, 0, 5, 3]
Solution #86: [6, 3, 1, 4, 7, 0, 2, 5]
Solution #87: [6, 3, 1, 7, 5, 0, 2, 4]
Solution #88: [6, 4, 2, 0, 5, 7, 1, 3]
Solution #89: [7, 1, 3, 0, 6, 4, 2, 5]
Solution #90: [7, 1, 4, 2, 0, 6, 3, 5]
Solution #91: [7, 2, 0, 5, 1, 4, 6, 3]
Solution #92: [7, 3, 0, 2, 5, 1, 6, 4]

***N = 9***

### d) Running-Time Comparison

Method | Finding 1st Solution, N = 8 |Finding all solutions, N = 8 |Finding 1st Solution, N = 9 |Finding all solutions, N = 9 |
------------ |------------ |------------ |------------ |------------ |
*Iterative* | 0.002976s | 0.043715s | 0.0011823s | 0.1013936s|
*Recursivce* | 0.002738s | 0.016604s | 0.0010993s | 0.0894477s|

### e)

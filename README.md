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
*PseudoCode for both methods can be found in the file : https://github.com/booklover98/nqueens/blob/master/nqueens_pseudocode.md

### b) Programs and Comments
 * i) Recursive : recusive_2.py
 * ii) Iterative : iterative_nqueens.py

### c) All Solutions for N=8 & N=9
*Can be found for both methods, both N values in the file in repository : https://github.com/booklover98/nqueens/nqueens_solutions.md

### d) Running-Time Comparison

Method | Finding 1st Solution, N = 8 |Finding all solutions, N = 8 |Finding 1st Solution, N = 9 |Finding all solutions, N = 9 |
------------ |------------ |------------ |------------ |------------ |
*Iterative* | 0.002976s | 0.043715s | 0.0011823s | 0.1013936s|
*Recursivce* | 0.002738s | 0.016604s | 0.0010993s | 0.0894477s|

### e)

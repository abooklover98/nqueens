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
*PseudoCode for both methods can be found in the file within repository: https://github.com/booklover98/nqueens/blob/master/nqueens_pseudocode.md

### b) Programs and Comments
 * i) Recursive : recusive_2.py
 * ii) Iterative : iterative_nqueens.py

### c) All Solutions for N=8 & N=9
*Can be found for both methods, both N values in the file within repository: https://github.com/booklover98/nqueens/blob/master/nqueens_solutions.pdf

### d) Running-Time Comparison

Method | Finding 1st Solution, N = 8 |Finding all solutions, N = 8 |Finding 1st Solution, N = 9 |Finding all solutions, N = 9 |
------------ |------------ |------------ |------------ |------------ |
*Iterative* | 2.976 ms | 27.663 ms | 1.1823 ms | 111.2372 ms|
*Recursive* | 2.738 ms | 16.604 ms | 1.0993 ms | 089.4477 ms|

### e) Discussion on Reported Running Times
Within the confines of this assignment, we had to write and execute two programs, one using an iterative method, the second using a recusive method to solve the N-Queens Problem for a board of 8x8 and 9x9. Doing an analysis of the running times for both programs, we can see that depending on the size of the board, a different method might be better, or faster, at solving all solutions.

For my iterative method solution, I used backtracking and looping to speed up the process, this allows for fast running time when working with smaller numbers, as can be seen by the results. Although not faster than the recusive method, it competes agressivly, with all solutions found on a 9x9 board, found within 25 ms of the recusive method. 



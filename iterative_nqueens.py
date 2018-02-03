#N-Queens problem Iterative Backtracking
#Iterative solution- Samantha Husack
#January 2018

import time #import the time library to calculate function run-time
# this library will allow me to calculate how long it takes my algorithm to calculate 
# how long each solution is found after the clock starts.

Reveal = True #Create workable space, where user can use code more than once.

while Reveal: #while this is true, rerun the code.

    class Board: #Create a Class, so that a new board is created every new play,
    #New Class for each board recreates a new game and reruns the code from scratch.

        def __init__(self, n_size): #Initialization of variables
            self.N = n_size #Size of the board, as input from user
            self.counter = 1 #creates a counter that allows to count ##of solutions

        def safe_queen(self, row, col): #Function to find out if queen is safe
            for r, c, in enumerate(self.queens): #goes through all elements in queens
                if r == row or c == col or abs (row-r) == abs (col-c): #checks if safe
                        #checks column, row and diagonals
                    return False #if not safe, return false
            return True #means queen is safe!

        def board_print(self): #this function prints a completed solution
            print ("Solution #%d:" % (self.counter), self.queens)
            """
            #Slower printing method, showing full-board with solution
            for row in range(self.N): #for each row of the board
                line = [' - '] * self.N #define no queen spot
                if row < len(self.queens): #if spot is sol spot, print Q
                    line[self.queens[row]] = ' Q '
                print(''.join(line)) #otherwise print .
            """
            end_time = time.time()
            time_temp = str(end_time - start_time)
            print("--------------- %0.00009s seconds ---" % (time_temp))
            self.counter+=1 #add 1 to counter for next solution.
            print () #print an empty line.

        def solution(self): #find solutions for given board
            self.queens = [] #array for queens positions
            col = row = 0 #initiate row and col to 0
            while True: #While there are still possible solutions
                while col < self.N and not self.safe_queen(row, col): 
                    #while the column is smaller than given board size, and not a solution
                    col += 1 #aughment col value
                if col < self.N: #if the col is smaller than board size
                    self.queens.append(col) #add column
                    if row + 1 >= self.N: #increase row size by 1, if greater/= then N
                        self.board_print() #print solution for board
                        self.queens.pop() #pop the last queen and try new spot
                        col = self.N #resete col value to n
                    else: #otherwise, increase row size and try new columns
                        row += 1
                        col = 0
                if col >= self.N: #if col is greater/equal to than n
                    # not possible to place a queen in this row anymore
                    if row == 0: #when row is == 0,
                        return # all combinations were tried
                    col = self.queens.pop() + 1 #pop the last queen and retry!
                    row -= 1 #go back one row

    board_size = int(input("Enter Board Size: ")) #get board size from user as int input
    q = Board(board_size) #create new board with board_size
    start_time = time.time()
    q.solution() #find solution

    if input("Calculate another board? [y/n]") == "n": #ask if user wants to go again
        Reveal = False #quit program



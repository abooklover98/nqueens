    
##  NQueens Solution - Recursive
import time   #import time library to calculate function run-time
Reveal = True #Create workable space, where user can use program more than once

while Reveal:   #while this is true, continue to rerun program
        
    def safe_queen(queen, col): #determine if queen is safe using queen array and column value
        for i in range(col): #for each number in range of column
            if queen[i] == queen[col] or col-i == abs(queen[col]-queen[i]): #check against already placed queens
                return False #if is true, not safe -- return False
        return True #queen is safe

    def solution(queens, col): #find all solutions for n-queens
        if col == n: #if column number is equal to n-size, solution found :)
            global counter
            counter +=1 #increase counter val for solutions
            print ('Solution #', counter, ': ', queens) #print solution as row indexes in col
            end_time = time.time() 
            time_temp = str(end_time - start_time)
            print("--------------- %0.00009s seconds ---" % (time_temp)) #print run-time up to that solution
            print()
            return
        
        for i in range(n): #for values from 0 -> n
            queen[col] = i #assign a val to col value in queens array
            if safe_queen(queen, col): #if safe. continue
                solution(queen, col+1) #recursive function, rerun!

    n = int(input("Enter Board Size: ")) #get board n from user as int input
    counter = 0 #start counter at 0
    queen = n*[0] #create array of size n
    start_time = time.time() #start time now
    solution(queen, 0) #find solutions

    if input("Calculate another board? [y/n]") == "n": #ask if user wants to go again
        Reveal = False #quit program

    
##  ghjftgvh
import time    
Reveal = True

while Reveal:    
        
    def safe_queen(queen, col):
        for i in range(col):
            if queen[i] == queen[col] or col-i == abs(queen[col]-queen[i]):
                return False
        return True

    def solution(queens, col):
        if col == n:
            global counter    
            counter +=1
            print ('Solution #', counter, ': ', queens)
            end_time = time.time()
            time_temp = str(end_time - start_time)
            print("--------------- %0.00009s seconds ---" % (time_temp))
            print()
            return
        
        for i in range(n):
            queen[col] = i
            if safe_queen(queen, col):
                solution(queen, col+1)

    n = int(input("Enter Board Size: ")) #get board n from user as int input
    counter = 0
    queen = n*[0]
    start_time = time.time()
    solution(queen, 0)

    if input("Calculate another board? [y/n]") == "n": #ask if user wants to go again
        Reveal = False #quit program

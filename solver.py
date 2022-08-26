import time

#board listing which positions are in which squares
square_board = [
    [0,0,0,1,1,1,2,2,2],
    [0,0,0,1,1,1,2,2,2],
    [0,0,0,1,1,1,2,2,2],
    [3,3,3,4,4,4,5,5,5],
    [3,3,3,4,4,4,5,5,5],
    [3,3,3,4,4,4,5,5,5],
    [6,6,6,7,7,7,8,8,8],
    [6,6,6,7,7,7,8,8,8],
    [6,6,6,7,7,7,8,8,8]]

#where in the board does each coloumn fill
def coloumns(board):

    c0 = [board[0][0],board[1][0],board[2][0],
    board[3][0],board[4][0],board[5][0],
    board[6][0],board[7][0],board[8][0]]
    c1 = [board[0][1],board[1][1],board[2][1],
    board[3][1],board[4][1],board[5][1],
    board[6][1],board[7][1],board[8][1]]
    c2 = [board[0][2],board[1][2],board[2][2],
    board[3][2],board[4][2],board[5][2],
    board[6][2],board[7][2],board[8][2]]
    c3 = [board[0][3],board[1][3],board[2][3],
    board[3][3],board[4][3],board[5][3],
    board[6][3],board[7][3],board[8][3]]
    c4 = [board[0][4],board[1][4],board[2][4],
    board[3][4],board[4][4],board[5][4],
    board[6][4],board[7][4],board[8][4]]
    c5 = [board[0][5],board[1][5],board[2][5],
    board[3][5],board[4][5],board[5][5],
    board[6][5],board[7][5],board[8][5]]
    c6 = [board[0][6],board[1][6],board[2][6],
    board[3][6],board[4][6],board[5][6],
    board[6][6],board[7][6],board[8][6]]
    c7 = [board[0][7],board[1][7],board[2][7],
    board[3][7],board[4][7],board[5][7],
    board[6][7],board[7][7],board[8][7]]
    c8 = [board[0][8],board[1][8],board[2][8],
    board[3][8],board[4][8],board[5][8],
    board[6][8],board[7][8],board[8][8]]

    return c0,c1,c2,c3,c4,c5,c6,c7,c8

#where in the board does each square fill
def which_square(board):

    s0 = [board[0][0],board[0][1],board[0][2],
    board[1][0],board[1][1],board[1][2],
    board[2][0],board[2][1],board[2][2]]

    s1 = [board[0][3],board[0][4],board[0][5],
    board[1][3],board[1][4],board[1][5],
    board[2][3],board[2][4],board[2][5]]

    s2 = [board[0][6],board[0][7],board[0][8],
    board[1][6],board[1][7],board[1][8],
    board[2][6],board[2][7],board[2][8]]

    s3 = [board[3][0],board[3][1],board[3][2],
    board[4][0],board[4][1],board[4][2],
    board[5][0],board[5][1],board[5][2]]

    s4 = [board[3][3],board[3][4],board[3][5],
    board[4][3],board[4][4],board[4][5],
    board[5][3],board[5][4],board[5][5]]

    s5= [board[3][6],board[3][7],board[3][8],
    board[4][6],board[4][7],board[4][8],
    board[5][6],board[5][7],board[5][8]]

    s6 = [board[6][0],board[6][1],board[6][2],
    board[7][0],board[7][1],board[7][2],
    board[8][0],board[8][1],board[8][2]]

    s7 = [board[6][3],board[6][4],board[6][5],
    board[7][3],board[7][4],board[7][5],
    board[8][3],board[8][4],board[8][5]]

    s8 = [board[6][6],board[6][7],board[6][8],
    board[7][6],board[7][7],board[7][8],
    board[8][6],board[8][7],board[8][8]]

    return s0,s1,s2,s3,s4,s5,s6,s7,s8

#find the first value in board that is unassigned
def find_unassigned(board):
    
    for i in range(len(board)):
            row = board[i]
            for j in range(len(row)):
                number = row[j]
                if number == 0:
                    square_indice = square_board[i][j]
                    return i,j,square_indice
                    
            #else:
                #continue
            

    return None

#check if a number can be placed in the board following the rules
def is_valid(board,number,row,coloumn,square):
    if (number not in row and number not in coloumn 
            and number not in square):
            return True
    return False


def solve_sudoku(board):
    find = find_unassigned(board)
    
    if find ==None:
        return True
      
       
    else:    
        i = find[0]
        j = find[1]
        square_indice = find[2]
        
        row = board[i]
        coloumn = coloumns(board)[j]
        square = which_square(board)[square_indice]

        #try numbers in place
        for k in range(1,10):   
            number = k
               
            #is the number safe?
            if is_valid(board,number,row,coloumn,square) == True:
                board[i][j] = number
                
                if solve_sudoku(board) ==True:
                    return True 
                    
                        
                else:              
                    board[i][j] = 0

            
        
    return False

                        

def main():
    

    board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]]

    solve_sudoku(board)

    print(*board, sep = "\n")

main()


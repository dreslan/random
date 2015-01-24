##########################################################
# A function that verifies Sudoku solutions
##########################################################
# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.
#
# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.
#
# A valid sudoku square satisfies these
# two properties:
#
#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.
#
#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.
#
# You may assume the the input is square and contains at
# least one row and column.
"""
correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
"""
    
def check_sudoku(game):
    #check rows, then transpose and use the same code
    if check_rows(game):
        game = transpose(game)
        if check_rows(game):
            return True
    return False

def check_rows(game):
    #assume game is a square, check the length, which is also the largest number
    n = len(game[0])
    number=1
    for row in game:
        while number <= n:
            if number not in row:
                return False
            number += 1
        #reset number
        number = 1
    #we made it here, it means each row passed
    return True

def transpose(game):
    n = len(game[0])
    game_transpose = build_list(n)
    row_index = 0
    column_index = 0
    while row_index < n:
        while column_index < n:
            game_transpose[column_index][row_index] = game[row_index][column_index]
            column_index += 1
        row_index += 1
        #reset column index
        column_index = 0
    return game_transpose

def build_list(n):
    list = []
    i = 0
    #adds n rows with no elements
    while i < n:
        j = 0
        #add a row
        list.append([])
        #populate the row
        while j < n:
            list[i].append(0)
            j += 1
        i += 1
    return list

"""
Check:
print check_sudoku(incorrect)
#>>> False

print check_sudoku(correct)
#>>> True

print check_sudoku(incorrect2)
#>>> False

print check_sudoku(incorrect3)
#>>> False

print check_sudoku(incorrect4)
#>>> False

print check_sudoku(incorrect5)
#>>> False
"""
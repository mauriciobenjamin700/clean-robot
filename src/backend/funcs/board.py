from src.backend.constants.main import (
    OBSTACLE,
    TRASH
)
from src.backend.funcs.position import(
    generate_position,
    place
)

def show_board(board: list[list[int]]):
    """
    print the board
    """
    print("-"*30)
    coluns, lines = len(board[0]), len(board)

    for line in range(lines):
        for column in range(coluns):
            print(board[line][column], end=" ")

        print("\n")



def generate_board(lines:int, columns:int) -> list[list]:
    
    board = [[TRASH for i in range(0,columns,1)] for j in range(0,lines,1)]
    
    return board

def generate_obstacles(board:list[list], num_blocks:int) -> bool:
    
    height = len(board)
    width = len(board[0])
    
    if num_blocks > width * height:
        return False
    
    for _ in range(0,num_blocks,1):
        
        x, y = generate_position(board)
        
        while not place(board, x, y, 'obstacle'):
            x, y = generate_position(board)

    return True

def remove_obstacles(board:list[list]):
    
    for line in range(len(board)):
        for column in range(len(board[0])):
            if board[line][column] == OBSTACLE:
                board[line][column] = TRASH
    


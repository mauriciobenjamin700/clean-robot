from src.backend.constants.main import (
    OBSTACLE,
    TRASH
)
from src.backend.funcs.position import(
    generate_position,
    place
)


def generate_board(lines:int, columns:int) -> list[list]:
    
    board = [[TRASH for i in range(0,columns,1)] for j in range(0,lines,1)]
    
    return board

def generate_obstacles(board:list[list], num_blocks:int) -> bool:
    
    width = len(board)
    height = len(board[0])
    
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
    

def get_board_sizes(board: list[list[int]]) -> tuple[int,int]:
    """
    return x, y
    """
    return (len(board[0]), len(board))
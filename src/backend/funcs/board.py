from src.backend.constants.main import TRASH
from src.backend.funcs.position import(
    generate_position,
    place
)


def generate_board(lines:int, columns:int) -> list[list]:
    
    board = [[TRASH for i in range(0,columns,1)] for j in range(0,lines,1)]
    
    return board

def generate_obstacles(board:list[list], num_blocks:int) -> None:
    
    width = len(board)
    height = len(board[0])
    
    if num_blocks > width * height:
        raise ValueError("Número de obstáculos maior que o número de posições do tabuleiro")
    
    for _ in range(0,num_blocks,1):
        
        x, y = generate_position(board)
        
        while not place(board, x, y, 'obstacle'):
            x, y = generate_position(board)

def board_size(board: list[list[int]]) -> tuple[int, int]:
    """
    return the size of the board in x (width), y[height] coordinates
    """
    return len(board[0]), len(board)
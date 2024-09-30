from src.backend.constants.main import TRASH
from src.backend.funcs.position import(
    generate_position,
    place
)


def generate_board(m:int, n:int) -> list[list]:
    
    board = [[TRASH for i in range(0,n,1)] for j in range(0,m,1)]
    
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
    Retorna uma tupla com a quantidade de linhas e colunas

    - Args:
        - board: list[list[int]] -> Tabuleiro
    
    - Return:
        - tuple[int, int]: Tupla com a quantidade de linhas e colunas
    """
    return len(board), len(board[0])
"""
- generate_position: Gera uma posição aleatória no tabuleiro.
- place: Coloca um robô ou obstáculo no tabuleiro.
- get_robot_position: Retorna a posição do robô no tabuleiro.
- remove_robot: Remove o robo do tabuleiro
- gerenate_random_number: Gera um número aleatório.

"""
from typing import Literal


from src.backend.constants.main import (
    OBSTACLE,
    ROBOT,
    CLEAN,
    TRASH,
    MOVES
)
from src.backend.funcs.base import gerenate_random_number


def generate_position(board:list[list]) -> tuple[int, int]:
    """
    Gerar uma posição aleatória no tabuleiro.
    """
    width = len(board)
    height = len(board[0])
    
    x = gerenate_random_number(0, width - 1)
    y = gerenate_random_number(0, height - 1)
    
    return x, y


def in_board(board:list[list], x:int, y:int) -> bool:
    """
    Verifica se a posição está dentro do tabuleiro.
    """
    width = len(board)
    height = len(board[0])
    
    return 0 <= x < width and 0 <= y < height

    
def place(board:list[list], x:int, y:int, type: Literal["obstacle", "robot"]) -> bool:
    """
    Coloca um robô ou obstáculo no tabuleiro.
    """
    width = len(board)
    height = len(board[0])
    
    result = True
    
    if not in_board(board, x,y): # Checando se a posição é válida
        result = False
    
    elif board[x][y] == OBSTACLE:
        result = False
        
    else:
        if type == "robot":
            board[x][y] = ROBOT
        elif type == "obstacle":
            board[x][y] = OBSTACLE
        else:
            raise ValueError("Tipo inválido")
    return result


def get_robot_position(board:list[list]) -> tuple[int, int]:
    """
    obtem a posição do robo
    """
    width = len(board)
    height = len(board[0])
    
    for i in range(0,width,1):
        for j in range(0,height,1):
            if board[i][j] == ROBOT:
                return i, j
            
    raise ValueError("Robô não encontrado")


def remove_robot(board:list[list[int]]) -> bool:
    """
    remove o robo
    """
    try:
        robot = get_robot_position(board)

        board[robot[0]][robot[1]] = TRASH

        return True
    
    except:
        return False

def can_move(board:list[list[int]], x:int, y:int) -> bool:
    """
    Chack se pode mover
    """

    if not in_board(board,x,y): # Checando se a posição é válida
        return False
    
    elif board[x][y] == OBSTACLE:
        return  False
    
    return True

def move(board:list[list], x:int, y:int, direction: Literal["up", "down", "right", "left"]) -> bool:
    """
    Tenta mover o robo e caso falhe, retorna False
    """
    
    result = True
    
    oldx = x
    oldy = y
    
    if direction == "up":
        x -= 1
    elif direction == "down":
        x += 1
    elif direction == "right":
        y += 1
    elif direction == "left":
        y -= 1
    else:
        return False


    if not can_move(board, x, y):
        return False

    else:
        board[x][y] = ROBOT
        board[oldx][oldy] = CLEAN
        
    return result

def new_robot_positon(robot: tuple[int, int], direction: tuple[int, int]) -> tuple[int, int]:
    """
    Cacula a nova posição do robo dado um movimento
    """
    return robot[0] + direction[0], robot[1] + direction[1]

def make_move(board):
    """
    Realiza o movimento do robo para a primeira direção possível
    """
    robot = get_robot_position(board)

    for direcion, position in MOVES.items():
        
        x, y =new_robot_positon(robot, position)

        if can_move(board, x, y):
            move(board, robot[0], robot[1], direcion)
            return True

def can_clean(board: list[list[int]], x:int, y:int) -> bool:
    """
    Calcula se as novas coordenadas (x, y) estão dentro dos limites do tabuleiro, não são obstáculos e não estão limpas.
    """
    if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] != OBSTACLE and board[x][y] != CLEAN and board[x][y] != ROBOT:
        return True
    return False

def clean(board: list[list[int]], x:int, y:int) -> None:
    """
    Limpa a célula atual
    """
    board[x][y] = CLEAN
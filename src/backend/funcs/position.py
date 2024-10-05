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

    - Args:
      - board:Tabuleiro
      - x:: line index
      - y:: column index
    """
    lines = len(board)
    columns = len(board[0])
    
    return 0 <= x < lines and 0 <= y < columns

    
def place(board:list[list], x:int, y:int, type: Literal["obstacle", "robot"]) -> bool:
    """
    Coloca um robô ou obstáculo no tabuleiro.
    """
    
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

def has_space(board:list[list]) -> bool:
    """
    Verifica se ainda há espaço no tabuleiro
    """
    for line in board:
        for item in line:
            if item == TRASH:
                return True
    return False

def place_robot(board:list[list]) -> bool:
    """
    Coloca o robo no tabuleiro
    """

    if not has_space(board):
        return False

    while True:
        x, y = generate_position(board)

        if place(board, x, y, "robot"):
            break

    return True

def get_robot_position(board:list[list]) -> tuple[int, int]:
    """
    obtem a posição do robo
    """
    lines = len(board)
    columns = len(board[0])
    
    for l in range(0,lines,1):
        for c in range(0,columns,1):
            if board[l][c] == ROBOT:
                return l, c
            
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

    - Args:
        - board:: list[list[int]]: Tabuleiro
        - x::int: posicao na linha
        - y:: int: posicao na coluna
    """

    if not in_board(board,x,y): # Checando se a posição é válida
        return False
    
    elif board[x][y] == OBSTACLE:
        return  False
    
    elif board[x][y] == ROBOT:
        return False
    
    return True

def get_direction(robot: tuple[int, int], x: int, y: int) -> Literal['right', 'left', 'down', 'up', 'invalid']:
    """
    Retorna a direção para movimentar

    - Args:
      - x: int: Altura
      - y: int: Largura
    """

    robot_x, robot_y = robot

    if robot_x == x:
        if robot_y == y:
            return "invalid"
        elif robot_y < y:
            return "right"
        elif robot_y > y:
            return "left"
    elif robot_y == y:
        if robot_x < x:
            return "down"
        elif robot_x > x:
            return "up"

    print(f"Robo: {robot_x} and {robot_y}\nx = {x} and y = {y}")
    return "invalid"

def move(board:list[list], x:int, y:int, direction: Literal["up", "down", "right", "left"]) -> bool:
    """
    Tenta mover o robo e caso falhe, retorna False

    - Args:
      - board:: list[list[int]]: Tabuleiro
      - x::int : Posição X do Robô
      - y::int : Posição Y do Robô
      - direction::str: Direção para mover o robo

    """
    if direction in MOVES.keys():
            
        
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

        if can_move(board, x, y):
            print("movi")
            board[x][y] = ROBOT
            board[oldx][oldy] = CLEAN
            return True
            
    else:
        print("Direção inválida")
        return False

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

    item = board[x][y] 


    if in_board(board, x,y) and item != OBSTACLE and item != ROBOT:
        return True
    return False

def clean(board: list[list[int]], x:int, y:int) -> None:
    """
    Limpa a célula atual
    """
    board[x][y] = CLEAN

def is_clean(board: list[list[int]], x:int, y:int):
    """
    Verifica se a célula atual está limpa
    """
    return board[x][y] == CLEAN
"""
- generate_position: Gera uma posição aleatória no tabuleiro.
- place: Coloca um robô ou obstáculo no tabuleiro.
- get_robot_position: Retorna a posição do robô no tabuleiro.
- remove_robot: Remove o robo do tabuleiro
- gerenate_random_number: Gera um número aleatório.

"""
from collections import deque
from typing import Callable, Literal


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

def get_board_sizes(board: list[list[int]]) -> tuple[int,int]:
    """
    return x, y
    """
    return (len(board[0]), len(board))


def in_board(board: list[list[int]], position: tuple[int,int]) -> bool:
    """
    return True if the position is in the board
    """
    width, height = get_board_sizes(board)
    x, y = position

    return 0 <= x < width and 0 <= y < height

def is_valid_position(board: list[list[int]], position: tuple[int,int]) -> bool:
    """
    return True if the position is valid
    """

    if not position:
        return False
    
    if in_board(board, position):
        x, y = position
        if board[y][x] != OBSTACLE and board[y][x] != ROBOT:
            return True
    return False

def generate_moves(board: list[list[int]]) -> list[tuple[int,int]]:
    """
    return a list of valid moves [up, down, left, right] in tuple format (x, y)
    """
    robot = get_robot(board)

    moves = []

    for name in MOVES.keys():
        new_position = new_robot_position(robot, name)

        if is_valid_position(board, new_position):
            moves.append(new_position)

    return moves

def stack_movies(stack:list, movies: list[tuple[int]], visited: set) -> list:
    """
    add movies to the stack
    """
    movies.reverse()

    for move in movies:
        if move not in stack and (not move in visited):
            stack.insert(0, move)

    return stack

def get_next_move(stack: list) -> tuple[int, int] | None:
    """
    return the next move
    """
    move = None
    if len(stack) > 0:
        move = stack.pop(0)
    return move

    
def place(board:list[list], x:int, y:int, type: Literal["obstacle", "robot"]) -> bool:
    """
    Coloca um robô ou obstáculo no tabuleiro.
    """
    
    result = True
    
    if not in_board(board, (x,y)): # Checando se a posição é válida
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

def get_robot(board: list[list[int]])-> tuple[int,int]:
    """
    return the position x,y of the robot
    """

    width, height = get_board_sizes(board)

    for line in range(height):

        for column in range(width):

            if board[line][column] == ROBOT:
                return (column, line)
            
    raise ValueError("Robot not found")


def remove_robot(board:list[list[int]]) -> bool:
    """
    remove o robo
    """
    try:
        robot = get_robot(board)

        board[robot[0]][robot[1]] = TRASH

        return True
    
    except:
        return False

def new_robot_position(robot: tuple[int,int], direction: str) -> tuple[int,int]:
    """
    return the new x, y position of the robot
    """
    x, y = robot
    dx, dy = MOVES[direction]

    return (x + dx, y + dy)

def can_move(board: list[list[int]], position: tuple[int,int]) -> bool:
    """
    return True if the robot can move
    """

    if is_valid_position(board, position):

        valid_positions = generate_moves(board)
        for option in valid_positions:
            if position == option:
                return True


    return False

def bfs(board: list[list[int]], start: tuple[int, int], goal: tuple[int, int]):
    """
    Realiza uma busca em largura para encontrar o caminho do robô para o local que ele tem que ir
    """
    
    valid_directions = [MOVES["up"], MOVES["down"], MOVES["left"], MOVES["right"]]  # cima, baixo, esquerda, direita
    queue = deque([(start, [start])])  # fila de (posição atual, caminho até aqui)
    local_visited = set([start])

    while queue:
        current, path = queue.popleft()
        if current == goal:
            path.pop(0)
            return path

        for direction in valid_directions:
            next_row, next_col = current[0] + direction[0], current[1] + direction[1]

            if is_valid_position(board, (next_row, next_col)) and (next_row, next_col) not in local_visited:
                local_visited.add((next_row, next_col))
                queue.append(((next_row, next_col), path + [(next_row, next_col)]))

    return []  # se não houver caminho


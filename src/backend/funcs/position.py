from typing import Literal


from src.backend.constants.main import (
    OBSTACLE,
    ROBOT,
    VOID
)
from src.backend.funcs.base import gerenate_random_number


def generate_position(board:list[list]) -> tuple[int, int]:
        
        width = len(board)
        height = len(board[0])
        
        x = gerenate_random_number(0, width - 1)
        y = gerenate_random_number(0, height - 1)
        
        return x, y
    
def place(board:list[list], x:int, y:int, type: Literal["obstacle", "robot"]) -> bool:
    
    width = len(board)
    height = len(board[0])
    
    result = True
    
    if x < 0 or x >= width or y < 0 or y >= height: # Checando se a posição é válida
        print("\nPosição inválida")
        result = False
    
    elif board[x][y] == OBSTACLE:
        print("\nJá existe um obstáculo nessa posição")
        result = False
        
    else:
        if type == "robot":
            board[x][y] = ROBOT
            print("\nRobô colocado com sucesso")
        elif type == "obstacle":
            board[x][y] = OBSTACLE
            print("\nObstáculo colocado com sucesso")
        else:
            raise ValueError("Tipo inválido")
    return result

def get_robot_position(board:list[list]) -> tuple[int, int]:
    
    width = len(board)
    height = len(board[0])
    
    for i in range(0,width,1):
        for j in range(0,height,1):
            if board[i][j] == ROBOT:
                return i, j
            
    raise ValueError("Robô não encontrado")


def move(board:list[list], x:int, y:int, direction: Literal["up", "down", "right", "left"]) -> bool:
    
    width = len(board)
    height = len(board[0])
    
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
        raise print("Direção inválida")
    
    if x < 0 or x >= width or y < 0 or y >= height: # Checando se a posição é válida
        print("\nPosição inválida")
        result = False
    
    elif board[x][y] == OBSTACLE:
        print("\nJá existe um obstáculo nessa posição")
        result = False
        
    else:
        board[x][y] = ROBOT
        board[oldx][oldy] = VOID
        print("\nRobô movido com sucesso")
        
    return result
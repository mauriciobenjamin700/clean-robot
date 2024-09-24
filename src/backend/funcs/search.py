from src.backend.constants.main import(
    CLEAN,
    TRASH,
    OBSTACLE,
    ROBOT,
    MOVES
)
from src.backend.old import show_board
from src.backend.funcs.position import can_clean

def deep_search_clean(board:list[list[int]], x:int, y:int):
    """
    Busca em profundidade (Deep Search First)

    - Args:
        - board:: list[list[int]]: tabuleiro
        - x:: int: posição x do robô
        - y:: int: posição y do robô

    - Returns:
        - None

    """
    stack = [(x, y)] # Pilha com a posição inicial do robo
    visited = set() # Rastreando as celulas visitasdas
    
    while stack: # Rastreando enquanto houver celulas na pilha

        cell_x, cell_y = stack.pop() # Remove a célula do topo da pilha e armazena suas coordenadas em cx e cy.
        
        if not ((cell_x, cell_y) in visited): # Se a célula não foi visitada, visitar.

            visited.add((cell_x, cell_y)) # Adiciona a célula atual ao conjunto de visitados.
            
            
            board[cell_x][cell_y] = CLEAN # Limpa a célula atual
            show_board(board)
            
            for direction_x, direction_y in MOVES.values(): # Para cada movimento possível (cima, baixo, esquerda, direita), calcula as novas coordenadas (new_position_x, new_position_y). Se as novas coordenadas estão dentro dos limites do tabuleiro, não são obstáculos e não estão limpas, adiciona-as à pilha para exploração futura.
                new_position_x, new_position_y = cell_x + direction_x, cell_y + direction_y
                
                if can_clean(board,new_position_x, new_position_y):
                    stack.append((new_position_x, new_position_y))
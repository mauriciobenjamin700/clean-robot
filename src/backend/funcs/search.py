from src.backend.constants.main import(
    CLEAN,
    TRASH,
    OBSTACLE,
    ROBOT
)
from src.backend.old import show_board

def dfs_clean(board, x, y):
    """
    Busca em profundidade
    """
    stack = [(x, y)] # Pilha com a posição inicial do robo
    visited = set() # Rastreando as celulas visitasdas
    
    while stack: # Rastreando enquanto houver celulas na pilha

        cx, cy = stack.pop() # Remove a célula do topo da pilha e armazena suas coordenadas em cx e cy.
        
        if (cx, cy) in visited: # Se a célula já foi visitada, pula para a próxima iteração do loop.
            continue
        
        visited.add((cx, cy)) # Adiciona a célula atual ao conjunto de visitados.
        
        # Limpa a célula atual
        board[cx][cy] = CLEAN 
        show_board(board)
        
        # Movimentos possíveis: up, down, left, right
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] != OBSTACLE and board[nx][ny] != CLEAN: #Para cada movimento possível (cima, baixo, esquerda, direita), calcula as novas coordenadas (nx, ny). Se as novas coordenadas estão dentro dos limites do tabuleiro, não são obstáculos e não estão limpas, adiciona-as à pilha para exploração futura.
                stack.append((nx, ny))
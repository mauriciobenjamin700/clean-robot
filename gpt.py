from collections import deque

def bfs(board: list[list[int]], start: tuple[int, int], goal: tuple[int, int]):
    """
    Realiza uma busca em largura para encontrar o caminho do robô para o local que ele tem que ir
    """

    rows, cols = len(board), len(board[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # cima, baixo, esquerda, direita
    queue = deque([(start, [start])])  # fila de (posição atual, caminho até aqui)
    visited = set([start])

    while queue:
        current, path = queue.popleft()
        if current == goal:
            path.pop(0)
            return path

        for direction in directions:

            next_row, next_col = current[0] + direction[0], current[1] + direction[1]

            if 0 <= next_row < rows and 0 <= next_col < cols and (next_row, next_col) not in visited:

                visited.add((next_row, next_col))

                queue.append(((next_row, next_col), path + [(next_row, next_col)]))

    return []  # se não houver caminho

# Matriz do tabuleiro
board = [
    [7, 1, 1, 7],
    [1, 7, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 8]
]

# Posição inicial do robô (3, 3) e posição objetivo (1, 1)
start = (3, 3)
goal = (1, 1)

# Encontrar o caminho
path = bfs(board, start, goal)

# Exibir o caminho
print("Caminho do robô:", path)
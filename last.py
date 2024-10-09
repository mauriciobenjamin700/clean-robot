from collections import deque
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

from src.backend.funcs.position import place_robot
from src.backend.funcs.board import generate_board, generate_obstacles

OBSTACLE = 7
ROBOT = 8
CLEAN = 0
TRASH = 1

LINES = 4
COLUMNS = 4

NUM_OBSTACLES = 2

board = generate_board(LINES, COLUMNS)

generate_obstacles(board, NUM_OBSTACLES)

place_robot(board)

"""board = [
    [7, 1, 1, 7],
    [1, 7, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 8]
]"""

directions = {
    "up": (0, -1),
    "down": (0, 1),
    "left": (-1, 0),
    "right": (1, 0)
}

visited = set([])



# Funções auxiliares de manipulação de tabuleiro e movimento do robô

def get_board_sizes(board: list[list[int]]) -> tuple[int, int]:
    """Retorna as dimensões do tabuleiro."""
    return (len(board[0]), len(board))

def get_robot(board: list[list[int]]) -> tuple[int, int]:
    """Retorna a posição (x, y) do robô no tabuleiro."""
    width, height = get_board_sizes(board)
    for line in range(height):
        for column in range(width):
            if board[line][column] == ROBOT:
                return (column, line)
    raise ValueError("Robot not found")

def stack_movies(stack:list, movies: list[tuple[int]]) -> list:
    """
    add movies to the stack
    """
    movies.reverse()
    global visited

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

def new_robot_position(robot: tuple[int, int], direction: str) -> tuple[int, int]:
    """Calcula a nova posição do robô a partir da direção."""
    global directions
    x, y = robot
    dx, dy = directions[direction]
    return (x + dx, y + dy)

def in_board(board: list[list[int]], position: tuple[int, int]) -> bool:
    """Verifica se a posição está dentro dos limites do tabuleiro."""
    width, height = get_board_sizes(board)
    x, y = position
    return 0 <= x < width and 0 <= y < height

def is_valid_position(board: list[list[int]], position: tuple[int, int]) -> bool:
    """Verifica se a posição é válida para o robô."""
    if not position:
        return False
    if in_board(board, position):
        x, y = position
        if board[y][x] != OBSTACLE and board[y][x] != ROBOT:
            return True
    return False

def generate_moves(board: list[list[int]]) -> list[tuple[int, int]]:
    """Gera uma lista de movimentos válidos."""
    global directions
    robot = get_robot(board)
    moves = []
    for name in directions.keys():
        new_position = new_robot_position(robot, name)
        if is_valid_position(board, new_position):
            moves.append(new_position)
    return moves

def bfs(board: list[list[int]], start: tuple[int, int], goal: tuple[int, int]):
    """Busca em largura (BFS) para encontrar o caminho até o destino."""
    valid_directions = [directions["up"], directions["down"], directions["left"], directions["right"]]
    queue = deque([(start, [start])])
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
    return []

def plot_board(board: list[list[int]], ax) -> None:
    """
    Plota o tabuleiro com o esquema de cores usando valores numéricos.
    
    """
    

    color_mapping = {
        CLEAN: 0,      # Limpo -> branco
        TRASH: 1,      # Lixo -> preto
        OBSTACLE: 2,   # Obstáculo -> vermelho
        ROBOT: 3       # Robô -> verde
    }
    
    # Convertendo o tabuleiro em valores numéricos
    numeric_board = np.array([[color_mapping[cell] for cell in row] for row in board])
    
    # Criando um colormap com as cores corretas
    cmap = colors.ListedColormap(['white', 'black', 'red', 'green'])
    
    # Plotando o tabuleiro com o colormap
    ax.clear()
    ax.imshow(numeric_board, cmap=cmap)
    ax.set_xticks(np.arange(-0.5, len(board[0]), 1), minor=True)
    ax.set_yticks(np.arange(-0.5, len(board), 1), minor=True)
    ax.grid(which='minor', color='black', linestyle='-', linewidth=2)
    ax.tick_params(which="both", bottom=False, left=False, labelbottom=False, labelleft=False)


def move_robot(board: list[list[int]], new_position: tuple[int, int], ax) -> list[list[int]]:
    """
    Move o robô para uma nova posição e atualiza o gráfico a cada passo.
    """
    global visited
    visited.add(new_position)
    if is_valid_position(board, new_position):
        x, y = new_position
        robot_x, robot_y = get_robot(board)

        if can_move(board, new_position):
            board[robot_y][robot_x] = CLEAN
            board[y][x] = ROBOT
            plot_board(board, ax)
            plt.pause(0.5)
        else:
            path = bfs(board, (robot_x, robot_y), new_position)
            print(f"Teleportei indo de {robot_x, robot_y} para {new_position} via {path}")
            for position in path:
                robot_x, robot_y = get_robot(board)
                x, y = position
                board[robot_y][robot_x] = CLEAN
                board[y][x] = ROBOT
                plot_board(board, ax)
                plt.pause(0.5)
    return board

# Configuração da animação

stack = [get_robot(board)]
fig, ax = plt.subplots()

# Inicializa o tabuleiro
plot_board(board, ax)

# Loop de movimentação
while len(stack) > 0:
    next_move = get_next_move(stack)
    board = move_robot(board, next_move, ax)
    moves = generate_moves(board)
    stack = stack_movies(stack, moves)

# Exibir a animação finalizada
plt.show()
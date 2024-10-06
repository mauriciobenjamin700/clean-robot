from collections import deque


OBSTACLE = 7
ROBOT = 8
CLEAN = 0
TRASH = 1


board = [
    [7,1,1,7],
    [1,7,1,1],
    [1,1,1,1],
    [1,1,1,8]
]

directions = {
    "up": (0, -1),
    "down": (0, 1),
    "left": (-1, 0),
    "right": (1, 0)
}

visited = set([])

def show_board(board: list[list[int]]):
    """
    print the board
    """
    for line in board:
        for column in line:
            print(column, end=" ")

def get_board_sizes(board: list[list[int]]) -> tuple[int,int]:
    """
    return x, y
    """
    return (len(board[0]), len(board))

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

def new_robot_position(robot: tuple[int,int], direction: str) -> tuple[int,int]:
    """
    return the new x, y position of the robot
    """
    global directions
    x, y = robot
    dx, dy = directions[direction]

    return (x + dx, y + dy)

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
    
    if in_board(board, position):
        x, y = position
        return board[x][y] != OBSTACLE and board[x][y] != ROBOT
    
    return False

def generate_moves(board: list[list[int]], robot: tuple[int,int]) -> list[tuple[int,int]]:
    """
    return a list of valid moves [up, down, left, right] in tuple format (x, y)
    """
    global directions

    moves = []

    for name in directions.keys():
        print(name)
        new_position = new_robot_position(robot, name)

        if is_valid_position(board, new_position):
            moves.append(new_position)

    return moves

def stack_movies(stack:list, movies: list[tuple[int]]) -> list:
    """
    add movies to the stack
    """
    movies.reverse()
    for move in movies:
        if move not in stack:
            stack.insert(0, move)

    return stack

def get_next_move(stack: list) -> tuple[int, int]:
    """
    return the next move
    """
    return stack.pop(0)

def can_move(board: list[list[int]], position: tuple[int,int]) -> bool:
    """
    return True if the robot can move
    """

    robot = get_robot(board)

    if is_valid_position(board, position):

        valid_positions = generate_moves(board, robot)
        for option in valid_positions:
            if position == option:
                return True


    return False

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

def move_robot(board: list[list[int]], new_position: tuple[int,int] ) -> list[list[int]]:
    """
    move the robot to the new position
    """
    x, y = new_position
    robot_x, robot_y = get_robot(board)

    if is_valid_position(board, new_position):

        if can_move(board, new_position):
            board[robot_x][robot_y] = CLEAN
            board[x][y] = ROBOT
            print(show_board(board))
        else:
            path = bfs(board, (robot_x, robot_y), new_position)

            for position in path:
                x, y = position
                board[robot_x][robot_y] = CLEAN
                board[x][y] = ROBOT
                robot_x, robot_y = x, y
                print(show_board(board))
                    

    return board


stack = [get_robot(board)]

while len(stack) > 0:
    robot = stack.pop(0)
    moves = generate_moves(board, robot)
    stack = stack_movies(stack, moves)
    move_robot(board, get_next_move(stack))


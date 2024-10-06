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
    print("-"*30)
    coluns, lines = get_board_sizes(board)

    for line in range(lines):
        for column in range(coluns):
            print(board[line][column], end=" ")

        print("\n")

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
    global directions

    robot = get_robot(board)

    moves = []

    for name in directions.keys():
        new_position = new_robot_position(robot, name)

        if is_valid_position(board, new_position):
            moves.append(new_position)

    return moves

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

def bfs(board: list[list[int]], start: tuple[int, int], goal: tuple[int, int]):
    """
    Realiza uma busca em largura para encontrar o caminho do robô para o local que ele tem que ir
    """
    
    valid_directions = [directions["up"], directions["down"], directions["left"], directions["right"]]  # cima, baixo, esquerda, direita
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


def move_robot(board: list[list[int]], new_position: tuple[int,int] ) -> list[list[int]]:
    """
    move the robot to the new position
    """
    global visited
    visited.add(new_position)
    if is_valid_position(board, new_position):

        x, y = new_position
        robot_x, robot_y = get_robot(board)

        if can_move(board, new_position):
            board[robot_y][robot_x] = CLEAN
            board[y][x] = ROBOT
            show_board(board)
        else:
            path = bfs(board, (robot_x, robot_y), new_position)

            for position in path:
                robot_x, robot_y = get_robot(board)
                x, y = position
                board[robot_y][robot_x] = CLEAN
                board[y][x] = ROBOT
                show_board(board)

        

                    

    return board


stack = [get_robot(board)]

while len(stack) > 0:
    next = get_next_move(stack)
    board = move_robot(board, next)
    moves = generate_moves(board)
    stack = stack_movies(stack, moves)
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

def generate_moves(board: list[list[int]], robot: tuple[int,int]) -> list[str]:
    """
    return a list of valid moves
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


stack = [(2,3)]

stack = stack_movies(stack, [(3,1), (2,2)])

print(get_next_move(stack))
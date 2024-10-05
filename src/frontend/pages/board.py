from cProfile import label
from typing import Literal
from customtkinter import(
    CTk,
    CTkFrame,
    CTkLabel
)



from src.backend.funcs.board import(
    board_size
)
from src.backend.constants.main import(
    CLEAN,
    TRASH,
    OBSTACLE,
    ROBOT
)
from src.frontend.styles.frame import configs_central as configs


def Board(app: CTk,frame_to_build: CTkFrame, matrix: list[list[int]]):

    x, y = board_size(matrix)

    frame_width = configs["width"] // x
    frame_height = configs["height"] // y

    frames = []

    for line in range(y):
        frames_in_line = []
        for column in range(x):
            color = _choice_color(matrix[line][column])
            square = CTkFrame(frame_to_build, width=frame_width, height=frame_height, fg_color=color, border_width=2, border_color="white")
            square.grid(row=line, column=column)
            frames_in_line.append(square)

        frames.append(frames_in_line)

    
    app.frames_in_board = frames

    app.button_left.configure(text="Cancelar")
    app.button_right.configure(text="Gerar Obstáculos")

    app.label_width.configure(text="Quantidade")

    app.label_height.pack_forget()
    app.entry_height.pack_forget()
    #app.right_menu.place_forget()

def _refrash_board(app: CTk, matrix: list[list[int]]):
    for line in range(len(matrix)):
        for column in range(len(matrix[0])):
            color = _choice_color(matrix[line][column])
            app.frames_in_board[line][column].configure(fg_color=color)

def _choice_color(value: int) -> Literal['white', 'black', 'red', 'green']:

    if value == CLEAN:
        color = 'white'
    elif value == TRASH:
        color = 'black'
    elif value == OBSTACLE:
        color = 'red'
    elif value == ROBOT:
        color = 'green'
    else:
        color = 'blue'

    return color

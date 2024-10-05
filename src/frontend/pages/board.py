from customtkinter import(
    CTk,
    CTkFrame
)
from typing import Literal
from tkinter.messagebox import showinfo


from src.backend.funcs.board import(
    board_size,
    generate_obstacles
)
from src.backend.funcs.position import(
    place_robot
)
from src.backend.constants.main import(
    CLEAN,
    TRASH,
    OBSTACLE,
    ROBOT
)
from src.frontend.styles.frame import configs_central as configs


def Board(app: CTk):
    matrix = app.matrix
    x, y = board_size(matrix)

    frame_width = configs["width"] // x
    frame_height = configs["height"] // y

    frames = []

    for line in range(y):
        frames_in_line = []
        for column in range(x):
            color = _choice_color(matrix[line][column])
            square = CTkFrame(app.main_frame, width=frame_width, height=frame_height, fg_color=color, border_width=2, border_color="white")
            square.grid(row=line, column=column)
            frames_in_line.append(square)

        frames.append(frames_in_line)

    
    app.frames_in_board = frames

    app.button_left.configure(text="Cancelar")
    app.button_right.configure(text="Gerar Obstáculos")

    app.label_width.configure(text="Quantidade")
    app.entry_width.delete(0, "end")
    app.entry_width.insert(0, '0')


    app.label_height.pack_forget()
    app.entry_height.pack_forget()
    #app.right_menu.place_forget()


def Obstacles(app: CTk, num_obstacles: int):
    
    if generate_obstacles(app.matrix, num_obstacles):
        _refrash_board(app, app.matrix)
        app.button_right.configure(text="Gerar Robô")

        app.label_width.pack_forget()
        app.entry_width.pack_forget()
    else:
        showinfo("Erro", "Número de obstáculos maior que o tamanho do tabuleiro")

def Robot(app):
    if place_robot(app.matrix):
        _refrash_board(app, app.matrix)
        app.button_right.configure(text="Iniciar Limpeza")
        app.label_width.configure(text="Tempo Limite")
        app.label_width.pack()
        app.entry_width.delete(0, "end")
        app.entry_width.insert(0, '0')
        app.entry_width.pack()
    else:
        showinfo("Erro", "Não foi possível colocar o robô no tabuleiro")
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

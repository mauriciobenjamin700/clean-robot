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
    can_clean,
    can_move,
    get_direction,
    get_robot_position,
    in_board,
    move,
    place_robot
)
from src.backend.constants.main import(
    CLEAN,
    MOVES,
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
        app.label_height.configure(text="Tempo Atual: 0")
        app.label_height.pack()
    else:
        showinfo("Erro", "Não foi possível colocar o robô no tabuleiro")

def Start(app: CTk, time_limit: int):

    app.time = time_limit
    DFS(app)


def DFS(app: CTk):
    stack = [get_robot_position(app.matrix)]  # stacka e formato de Pilha com a posição inicial do robô e tudo que ele conhece até agora
    visited = set()  # Células visitadas

    def next_move():
        print(f"Pilha: {stack}\nVisitados: {visited}")
        if len(stack) > 0:  # Checar se a pilha não está vazia
            cell_x, cell_y = stack.pop()  # Obter a próxima célula a ser visitada

            if in_board(app.matrix, cell_x, cell_y):  # Checar se a célula está dentro do tabuleiro

                if (cell_x, cell_y) not in visited:  # Checar se a célula já foi visitada, caso não tenha sido, vamos visitá-la
                    visited.add((cell_x, cell_y))  # Adicionar a célula atual ao conjunto de visitados

                if can_clean(app.matrix, cell_x, cell_y):

                    x, y = get_robot_position(app.matrix)
                    direction = get_direction((x, y), cell_x, cell_y)
                    print(direction)
                    if move(app.matrix, x, y, direction):
                        print(f"Linha 119: {app.matrix}")
                        
                    _refrash_board(app, app.matrix)
                else:
                    print(f"Já foi Visitada: X:{cell_x}, Y:{cell_y}")
                

            else:
                print(f"Fora do Tabuleiro: X: {cell_x}, Y: {cell_y}")


            for direction_x, direction_y in MOVES.values():  # Percorrer as direções possíveis

                new_position_x, new_position_y = cell_x + direction_x, cell_y + direction_y

                if in_board(app.matrix, new_position_x, new_position_y) and (new_position_x, new_position_y) not in visited:  # Se a direção for válida (Estiver dentro do tabuleiro)
                    if can_move(app.matrix, new_position_x, new_position_y):
                        stack.append((new_position_x, new_position_y))

            app.time -=1
            app.label_height.configure(text=f"Tempo Atual: {app.time}")

            if app.time < 0:
                showinfo("Fim", "Tempo esgotado")
                return
            app.after(1000, next_move)  # Atraso antes do próximo movimento

        else:
            print("Pilha vazia, finalizando a limpeza.")

    next_move()  # Iniciar o loop de movimentos
    print("Finalizei")



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

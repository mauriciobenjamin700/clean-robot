from customtkinter import CTkFrame
from tkinter.messagebox import showwarning

from src.frontend.components.entry import Entry
from src.frontend.components.board import BorderFrame, generate_chess_board
from src.frontend.styles.colors.page import SCREEN


from src.backend.funcs.position import (
    place,
    generate_position,
    get_robot_position
)

class RobotScreen(CTkFrame):
    def __init__(self, master, border:list[list[int]] = None):
        super().__init__(master)

        self.master = master
        self.board = border
        self.configure(fg_color=SCREEN)
        if not self.board:
            self.board = generate_chess_board()
        
        #border = None
        self.central_frame = BorderFrame(self, "Voltar", "Gerar Robô",self.board)
        self.central_frame.pack()
        
        self.central_frame.button_right.bind("<Button-1>", self.add_robot)


    def add_robot(self, event=None):

        while True:

            try:
                get_robot_position(self.board)
                showwarning("Atenção", "Já existe um robô no tabuleiro")
                break
            except:

                x,y = generate_position(self.board)

                if place(self.board, x, y, "robot"):

                    break

        self.central_frame.inner_frame.regenerate_board(self.board)
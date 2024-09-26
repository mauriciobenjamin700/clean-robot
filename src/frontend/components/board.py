from customtkinter import CTkFrame, CTkLabel

from src.frontend.styles.colors.page import SCREEN, WINDOW
from src.frontend.styles.configs.size import CENTRAL_FRAME_HEIGHT, CENTRAL_FRAME_WIDTH, INTERNAL_FRAME_HEIGHT, INTERNAL_FRAME_WIDTH
from src.frontend.components.button import Button

def generate_chess_board():
    board = []
    for i in range(8):
        row = []
        for j in range(8):
            if (i + j) % 2 == 0:
                row.append(1)  # Branco
            else:
                row.append(0)  # Preto
        board.append(row)
    return board

# Classe para exibir o tabuleiro de xadrez
class ChessBoardFrame(CTkFrame):
    def __init__(self, master, board):
        super().__init__(master, width=INTERNAL_FRAME_WIDTH, height=INTERNAL_FRAME_HEIGHT, fg_color=SCREEN)
        self.board = board
        self.create_board()

    def create_board(self):
        for i in range(8):
            self.grid_rowconfigure(i, weight=1)
            for j in range(8):
                self.grid_columnconfigure(j, weight=1)
                color = "white" if self.board[i][j] == 1 else "black"
                cell = CTkLabel(self, text="", fg_color=color)
                cell.grid(row=i, column=j, padx=1, pady=1, sticky="nsew")

class BorderFrame(CTkFrame):
    def __init__(self, master=None, name_button_left: str = "Button 1", name_button_right: str = "Button 2", border: list = generate_chess_board()):
        super().__init__(master, width=CENTRAL_FRAME_WIDTH, height=CENTRAL_FRAME_HEIGHT)

        # Desativar a propagação do tamanho
        self.pack_propagate(False)

        self.configure(fg_color=WINDOW)

        # Create inner frame
        self.inner_frame = ChessBoardFrame(self, border)
        self.inner_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Create button frame to hold buttons
        self.frame_button = CTkFrame(self, fg_color=WINDOW)
        self.frame_button.pack(expand=True)

        # Create buttons inside button frame
        self.button_left = Button(self.frame_button, text=name_button_left)
        self.button_left.pack(side="left", padx=10, pady=10)

        self.button_right = Button(self.frame_button, text=name_button_right)
        self.button_right.pack(side="left", padx=10, pady=10)
from customtkinter import CTkFrame, CTkLabel

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
        super().__init__(master)
        self.board = board
        self.create_board()

    def create_board(self):
        for i in range(8):
            for j in range(8):
                color = "white" if self.board[i][j] == 1 else "black"
                cell = CTkLabel(self, text="", width=40, height=40, fg_color=color)
                cell.grid(row=i, column=j, padx=1, pady=1)
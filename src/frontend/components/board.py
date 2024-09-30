from customtkinter import CTkFrame, CTkLabel, CTkImage
from PIL import Image, ImageTk
from tkinter import PhotoImage

from src.frontend.styles.colors.page import SCREEN, WINDOW
from src.frontend.styles.configs.size import CENTRAL_FRAME_HEIGHT, CENTRAL_FRAME_WIDTH, INTERNAL_FRAME_HEIGHT, INTERNAL_FRAME_WIDTH
from src.frontend.components.button import Button


from src.backend.constants.main import(
    CLEAN,
    TRASH,
    OBSTACLE,
    ROBOT
)


def generate_chess_board(lines:int=8, columns=8):
    board = []
    for i in range(lines):
        row = []
        for j in range(columns):
            if (i + j) % 2 == 0:
                row.append(0)  # Preto
            else:
                row.append(1)  # Branco
        board.append(row)
    return board

# Classe para exibir o tabuleiro de xadrez
class ChessBoardFrame(CTkFrame):
    def __init__(self, master, board):
        super().__init__(master, width=INTERNAL_FRAME_WIDTH, height=INTERNAL_FRAME_HEIGHT, fg_color=SCREEN)
        self.obstacle = Image.open("images/obstacle.png")
        self.robot = Image.open("images/robot.png")
        self.list_of_labels = []
        self.create_board(board)

    def create_board(self, board):
        
        self.board = board

        lines = len(board)

        columns = len(board[0])

        for i in range(lines):

            array = []

            self.grid_rowconfigure(i, weight=1)

            for j in range(columns):

                self.grid_columnconfigure(j, weight=1)

                cell = self._choice_item(board[i][j], board)

                cell.grid(row=i, column=j, padx=1, pady=1, sticky="nsew")

                array.append(cell)
            
            self.list_of_labels.append(array)

    
    def get_label(self, x, y):
        if 0 <= x < len(self.list_of_labels) and 0 <= y < len(self.list_of_labels[0]):
            return self.list_of_labels[x][y]
        else:
            raise IndexError(f"Coordenadas fora dos limites: ({x}, {y})")


    def regenerate_board(self, new_board):
        # Destruir o tabuleiro atual
        for widget in self.winfo_children():
            widget.destroy()
        

        # Criar o novo tabuleiro
        self.create_board(new_board)


    def _choice_color(self, item: int) -> str:
        if item == CLEAN:
            return "white"
        elif item == TRASH:
            return "black"
        elif item == OBSTACLE:
            return "red"
        elif item == ROBOT:
            return "green"
        else:
            return "blue"
        

    def _choice_item(self, item: int, board: list[list[int]]) -> CTkLabel:
        width = self.winfo_width() // len(board[0])  # Largura da label
        height = self.winfo_height() // len(board)   # Altura da label

        color = self._choice_color(item)

        style = CTkLabel(self, text="", fg_color=color, width=width, height=height)

        return style
class BorderFrame(CTkFrame):
    def __init__(self, master=None, name_button_left: str = "Button 1", name_button_right: str = "Button 2", board: list = generate_chess_board()):
        super().__init__(master, width=CENTRAL_FRAME_WIDTH, height=CENTRAL_FRAME_HEIGHT)

        # Desativar a propagação do tamanho
        self.pack_propagate(False)

        self.configure(fg_color=WINDOW)

        # Create inner frame
        self.inner_frame = ChessBoardFrame(self, board)
        self.inner_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Create button frame to hold buttons
        self.frame_button = CTkFrame(self, fg_color=WINDOW)
        self.frame_button.pack(expand=True)

        # Create buttons inside button frame
        self.button_left = Button(self.frame_button, text=name_button_left)
        self.button_left.pack(side="left", padx=10, pady=10)

        self.button_right = Button(self.frame_button, text=name_button_right)
        self.button_right.pack(side="left", padx=10, pady=10)
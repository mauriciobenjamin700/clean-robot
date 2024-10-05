from operator import ge
from customtkinter import CTk
from tkinter.messagebox import(
    showinfo,
    showwarning,
    showerror
)


from src.frontend.styles.page import configs
from src.frontend.configs.position import align_center
from src.frontend.pages.home import HomePage
from src.frontend.pages.board import (
    Board,
    Obstacles,
    Robot
)
from src.backend.funcs.position import remove_robot
from src.backend.funcs.board import (
    generate_board,
    remove_obstacles
)

class App(CTk):
    def __init__(self):
        super().__init__()

        self.title("Clean Robot")

        width, height = self.winfo_screenwidth(), self.winfo_screenheight()

        x,y = align_center(width, height, configs["width"], configs["height"])

        self.geometry(f"{configs['width']}x{configs['height']}+{x}+{y}")

        self.configure(fg_color=configs["fg_color"])

        HomePage(self)

        self.button_right.configure(command=self._home_to_board)
        self.button_left.configure(command=self._exit)

    def _exit(self):
        self.destroy()

    def _home_to_board(self, event=None):
        width, height = self.entry_width.get(), self.entry_height.get()

        if width.isnumeric() and height.isnumeric():
            width = int(width)
            height = int(height)
            if width > 0 and height > 0:
                self.matrix = generate_board(height, width)
                showinfo("Informação", "Tabuleiro Gerado com Sucesso")
                Board(self)
                self.button_left.configure(command=self._board_to_home)
                self.button_right.configure(command=self._place_obstacles)
            else:
                showerror("Erro", "Os valores devem ser maiores que 0")
        else:
            showerror("Erro", "Os valores devem ser numéricos")

    def _board_to_home(self, event=None):
        HomePage(self)
        self.button_right.configure(command=self._home_to_board)
        self.button_left.configure(command=self._exit)

    def _place_obstacles(self, event=None):
        num_obstacles:str = self.entry_width.get()

        if num_obstacles.isnumeric():
            num_obstacles = int(num_obstacles)
            if num_obstacles >= 0:
                Obstacles(self, num_obstacles)
                self.button_left.configure(command=self._remove_obstacles)
                self.button_right.configure(command=self._place_robot)
            else:
                showerror("Erro", "O valor deve ser positivo")
        else:
            showerror("Erro", "O valor deve ser numérico")

    def _remove_obstacles(self, event=None):
        remove_obstacles(self.matrix)
        Board(self)
        self.button_left.configure(command=self._board_to_home)
        self.button_right.configure(command=self._place_obstacles)
        self.label_width.pack()
        self.entry_width.pack()


    def _place_robot(self, event=None):
        Robot(self)
        self.button_left.configure(command=self._remove_robot)
        self.button_right.configure(command=self._start_cleaning)

    def _remove_robot(self, event=None):
        remove_robot(self.matrix)
        self._place_obstacles()

    def _start_cleaning(self, event=None):
        time_limit:str = self.entry_width.get()
        if time_limit.isnumeric():
            time_limit = int(time_limit)
            if time_limit > 0:
                self._clean()
            else:
                showerror("Erro", "O tempo limite deve ser maior que 0")
        else:
            showerror("Erro", "O tempo limite deve ser numérico")
    

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
from src.frontend.pages.board import Board

from src.backend.funcs.board import generate_board

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

    def _home_to_board(self):
        width, height = self.entry_width.get(), self.entry_height.get()
        print(f"width: {width}, height: {height}")

        if width.isnumeric() and height.isnumeric():
            width = int(width)
            height = int(height)
            if width > 0 and height > 0:
                self.matrix = generate_board(height, width)
                Board(self, self.main_frame, self.matrix)
            else:
                showerror("Erro", "Os valores devem ser maiores que 0")
        else:
            showerror("Erro", "Os valores devem ser numéricos")

    def _exit(self):
        self.destroy()

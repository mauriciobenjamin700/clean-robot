from customtkinter import CTk, CTkFrame


from tkinter.messagebox import (
    showinfo,
    showerror,
    showwarning
)
from src.frontend.styles.colors.entry import PLACEHOLDER
from src.frontend.components.div import CentralFrame
from src.frontend.components.entry import Entry
from src.frontend.styles.colors.page import SCREEN
from src.frontend.pages.home import HomeScreen
from src.frontend.pages.board import BoardScreen

from src.frontend.styles.configs.position import (
    center_window,
    align_frame_center,
    align_frame_right
)

class App(CTk):
    def __init__(self):
        super().__init__()

        self.title("My APP")

        self.configure(fg_color=SCREEN)

        center_window(self)

        self.resizable(False, False)

        self.home = HomeScreen(self)

        self._show_screen(self.home)

        #self.home.pack(expand=True, fill="both")

        #align_frame_center(self, self.home.central_frame)

        #align_frame_center(self, self.central_frame)


        # Bind click event to the root window
        self.bind("<Button-1>", self.on_click)

        self.home.central_frame.button_left.bind("<Button-1>", self._exit)
        self.home.central_frame.button_right.bind("<Button-1>", self.home_to_board)


    def home_to_board(self, event):
        width = self.home.entry_WIDTH.get()
        height = self.home.entry_HEIGHT.get()


        if not width or not height:
            showerror("Erro", "Preencha todos os campos")

        elif not self._valid_numbers(width):
            showwarning("Aviso", "Insira apenas números inteiros na largura")

        elif not self._valid_numbers(height):
            showwarning("Aviso", "Insira apenas números inteiros na altura")

        else:
            self.board = BoardScreen(self)
            self._show_screen(self.board)
            self._forget_screen(self.home)
            align_frame_right(self, self.board.entry_frame)
            align_frame_center(self, self.board.central_frame)
            self.board.central_frame.button_left.bind("<Button-1>", self.board_to_home)

    def board_to_home(self, event):
        self._show_screen(self.home)
        self._forget_screen(self.board)
        align_frame_center(self, self.home.central_frame)
        self.home.central_frame.button_right.bind("<Button-1>", self.home_to_board)            


    def on_click(self, event):
        # Set focus to the root window when clicking outside the entry
        if event.widget == self:
            self.focus_set()

    def _show_screen(self, screen):
        screen.pack(expand=True, fill="both")
        align_frame_center(self, screen.central_frame)
        screen.tkraise()

    def _forget_screen(self, screen):
        screen.forget()

    def _valid_numbers(self, input:str) -> bool:

        if input.isnumeric():
            value = int(input)

            if value > 0:
            
                return True
        
        return False
    

    def _exit(self, event):
        self.quit()
        self.destroy()



if __name__ == "__main__":
    app = App()
    app.mainloop()
    #self.overrideredirect(True)
    #self.update_idletasks()
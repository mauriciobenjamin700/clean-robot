from customtkinter import CTk, CTkFrame


from tkinter.messagebox import (
    showinfo,
    showerror,
    showwarning
)
from src.frontend.components.div import CentralFrame
from src.frontend.components.entry import Entry
from src.frontend.styles.colors.page import SCREEN
from src.frontend.pages.home import HomeScreen

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

        self.home.central_frame.button_right.bind("<Button-1>", self.board_screen)

    def board_screen(self, event):
        width = self.home.entry_WIDTH.get()
        height = self.home.entry_HEIGHT.get()

        if width and height:
            showinfo("Info", f"Width: {width}, Height: {height}")
        else:
            showerror("Aviso","Invalid input")

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



if __name__ == "__main__":
    app = App()
    app.mainloop()
    #self.overrideredirect(True)
    #self.update_idletasks()
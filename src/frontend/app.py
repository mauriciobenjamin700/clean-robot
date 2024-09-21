from customtkinter import CTk, CTkFrame


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

        self.central_frame = CentralFrame(self)

        self.central_frame.pack()
        
        self.update_idletasks()
        
        align_frame_center(self, self.central_frame)

        self.entry_frame = CTkFrame(self, fg_color=SCREEN)
        self.entry_frame.pack(side="right", anchor="e", padx=10, pady=10)

        self.entry_WIDTH = Entry(self.entry_frame, placeholder_text="Linhas")
        self.entry_WIDTH.pack(padx=10, pady=5)

        self.entry_HEIGHT = Entry(self.entry_frame, placeholder_text="Colun")
        self.entry_HEIGHT.pack(padx=10, pady=5)


        # Bind click event to the root window
        self.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        # Set focus to the root window when clicking outside the entry
        if event.widget == self:
            self.focus_set()


if __name__ == "__main__":
    app = App()
    app.mainloop()
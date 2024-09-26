# home_screen.py
from customtkinter import CTkFrame



from src.frontend.components.div import CentralFrame
from src.frontend.components.entry import Entry
from src.frontend.styles.colors.page import SCREEN
from src.frontend.styles.configs.position import center_window, align_frame_center

class BoardScreen(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.configure(fg_color=SCREEN)

        self.central_frame = CentralFrame(self)
        self.central_frame.pack()
        
        self.entry_frame = CTkFrame(self, fg_color=SCREEN)
        self.entry_frame.pack(side="right", anchor="e", padx=10, pady=10)

        self.entry_quantity = Entry(self.entry_frame, placeholder_text="Quantidade")
        self.entry_quantity.pack(padx=10, pady=5)





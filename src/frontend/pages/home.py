# home_screen.py
from customtkinter import CTkFrame, CTkLabel



from src.frontend.components.div import CentralFrame
from src.frontend.components.entry import Entry
from src.frontend.styles.colors.label import TEXT, TEXT_STYLE
from src.frontend.styles.colors.page import SCREEN
from src.frontend.styles.configs.position import (
    center_window, 
    align_frame_center
)

class HomeScreen(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.configure(fg_color=SCREEN)

        self.central_frame = CentralFrame(self, "Sair", "Gerar Tabuleiro")
        self.central_frame.pack()
        
        self.entry_frame = CTkFrame(self, fg_color=SCREEN)
        self.entry_frame.pack(side="right", anchor="e", padx=10, pady=10)

        self.label_WIDTH = CTkLabel(self.entry_frame,text="Linhas", fg_color=SCREEN, text_color=TEXT, font=TEXT_STYLE)
        self.label_WIDTH.pack(padx=10, pady=5)
        
        self.entry_WIDTH = Entry(self.entry_frame, placeholder_text="Digite aqui")
        self.entry_WIDTH.pack(padx=10, pady=5)

        self.label_HEIGHT = CTkLabel(self.entry_frame,text="Colunas", fg_color=SCREEN, text_color=TEXT, font=TEXT_STYLE)
        self.label_HEIGHT.pack(padx=10, pady=5)

        self.entry_HEIGHT = Entry(self.entry_frame, placeholder_text="Digite aqui")
        self.entry_HEIGHT.pack(padx=10, pady=5)

        self.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        if event.widget == self:
            self.focus_set()



from customtkinter import CTkFrame


from src.frontend.components.entry import Entry
from src.frontend.components.board import BorderFrame, generate_chess_board
from src.frontend.styles.colors.page import SCREEN


class BoardScreen(CTkFrame):
    def __init__(self, master, border:list[list[int]] = None):
        super().__init__(master)

        self.master = master
        self.configure(fg_color=SCREEN)
        if not border:
            border = generate_chess_board()
        
        #border = None
        self.central_frame = BorderFrame(self, "Voltar", "Gerar Obstáculos",border)
        self.central_frame.pack()
        
        self.entry_frame = CTkFrame(self, fg_color=SCREEN)
        self.entry_frame.pack(side="right", anchor="e", padx=10, pady=10)

        self.entry_quantity = Entry(self.entry_frame, placeholder_text="Quantidade")
        self.entry_quantity.pack(padx=10, pady=5)





import customtkinter as ctk
from numpy import pad

from src.frontend.styles.colors.page import WINDOW
from src.frontend.styles.configs.size import(
    CENTRAL_FRAME_WIDTH,
    CENTRAL_FRAME_HEIGHT,
    INTERNAL_FRAME_WIDTH,
    INTERNAL_FRAME_HEIGHT,
)
from src.frontend.styles.configs.position import(
    align_frame_center
)
from src.frontend.components.button import Button
class CentralFrame(ctk.CTkFrame):
    def __init__(self, master=None, name_button_left: str = "Button 1", name_button_right: str = "Button 2",border_frame: ctk.CTkFrame = None):
        super().__init__(master, width=CENTRAL_FRAME_WIDTH, height=CENTRAL_FRAME_HEIGHT)


        # Desativar a propagação do tamanho
        self.pack_propagate(False)

        self.configure(fg_color=WINDOW)

        # Create inner frame
        if not border_frame:
            self.inner_frame = ctk.CTkFrame(self, width=INTERNAL_FRAME_WIDTH, height=INTERNAL_FRAME_HEIGHT)
        else: self.inner_frame = border_frame
        
        self.inner_frame.pack(expand=True,fill="both", padx=10, pady=10)

        #align_frame_center(self, self.inner_frame)

        # Create button frame to hold buttons
        self.frame_button = ctk.CTkFrame(self, fg_color=WINDOW)
        self.frame_button.pack(expand=True)

        # Create buttons inside button frame
        self.button_left = Button(self.frame_button, text=name_button_left)
        self.button_left.pack(side="left", padx=10, pady=10)

        self.button_right = Button(self.frame_button, text=name_button_right)
        self.button_right.pack(side="left", padx=10, pady=10)

        self.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        if event.widget == self:
            self.focus_set()
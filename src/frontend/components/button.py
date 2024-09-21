from customtkinter import CTkButton



from src.frontend.styles.colors.button import(
    BACKGROUND,
    TEXT_COLOR,
    TEXT_STYLE,
    HOVER_COLOR,
    BODER_RADIUS,
    BORDER_COLOR,
    BORDER_WIDTH
)
from src.frontend.styles.configs.size import(
    BUTTON_WIDTH,
    BUTTON_HEIGHT
)

class Button(CTkButton):
    def __init__(
            self, 
            master=None,
            text:str="Button", 
            **kwargs
        ):
        super().__init__(
            master, 
            **kwargs)
        

        self.configure(
            font=TEXT_STYLE,  # Corrigido para 'font'
            width=BUTTON_WIDTH,  # Largura em pixels
            height=BUTTON_HEIGHT,  # Altura em pixels
            fg_color=BACKGROUND,
            text_color=TEXT_COLOR,
            corner_radius=BODER_RADIUS,
            hover_color=HOVER_COLOR,
            border_color=BORDER_COLOR,
            border_width=BORDER_WIDTH,
            text=text
        )
        #self.pack(padx=10, pady=10)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        pass
    """
    self.configure(
            fg_color="black",
            text_color="white"
        )
    """

    def on_leave(self, event):
        pass
        """
        self.configure(
            fg_color="white",
            text_color="black"
        )
        """
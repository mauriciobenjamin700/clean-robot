from customtkinter import (
    CTkButton,
    CTkFrame
)



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


def Button(master: CTkFrame, text: str = "Button") -> CTkButton:
    return CTkButton(
        master, 
        text=text, 
        fg_color=BACKGROUND, 
        text_color=TEXT_COLOR, 
        font=TEXT_STYLE, 
        corner_radius=BODER_RADIUS, 
        hover_color=HOVER_COLOR, 
        border_color=BORDER_COLOR, 
        border_width=BORDER_WIDTH, 
        width=BUTTON_WIDTH, 
        height=BUTTON_HEIGHT
    )

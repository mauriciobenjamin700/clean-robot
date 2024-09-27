from customtkinter import (
    CTkLabel,
    CTkFrame
)



from src.frontend.styles.colors.page import(
    SCREEN
)
from src.frontend.styles.colors.label import(
    TEXT,
    TEXT_STYLE
)

def Label(master:CTkFrame, text: str) -> CTkLabel:
    return CTkLabel(master,text=text, fg_color=SCREEN, text_color=TEXT, font=TEXT_STYLE)
from customtkinter import (
    CTkLabel,
    CTkFrame
)


from src.frontend.styles.label import config


def Label(master:CTkFrame, text: str) -> CTkLabel:
    return CTkLabel(master,text=text, **config)
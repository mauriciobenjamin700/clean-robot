from customtkinter import (
    CTk,    
    CTkFrame
)


from src.frontend.styles.frame import configs_right as configs

def RightFrame(parent: CTk):
    return CTkFrame(parent, **configs)
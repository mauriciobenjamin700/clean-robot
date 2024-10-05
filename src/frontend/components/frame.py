from customtkinter import (
    CTk,    
    CTkFrame
)


from src.frontend.styles.frame import configs_right as configs

def RightFrame(parent: CTk) -> CTkFrame:
    frame =  CTkFrame(parent, **configs)
    frame.pack_propagate(False)
    frame.grid_propagate(False)
    return frame
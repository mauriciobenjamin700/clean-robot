from customtkinter import (
    CTk,    
    CTkFrame
)


from src.frontend.styles.frame import (
    configs_right as right,
    configs_botton as botton
)

def RightFrame(parent: CTk) -> CTkFrame:
    frame =  CTkFrame(parent, **right)
    frame.pack_propagate(False)
    frame.grid_propagate(False)
    return frame

def BottonFrame(parent: CTk) -> CTkFrame:
    frame =  CTkFrame(parent, **botton)
    frame.pack_propagate(False)
    frame.grid_propagate(False)
    return frame
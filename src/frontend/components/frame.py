from customtkinter import CTkFrame

from src.frontend.styles.frame import configs_central

def Frame(master: CTkFrame) -> CTkFrame:
    return CTkFrame(master=master,**configs_central)
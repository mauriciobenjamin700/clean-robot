from customtkinter import CTkEntry


from src.frontend.styles.entry import config


def Entry(master=None, placeholder_text=None) -> CTkEntry:
    return CTkEntry(master, placeholder_text=placeholder_text, **config)
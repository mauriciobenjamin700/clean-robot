from customtkinter import CTkEntry


from src.frontend.styles.entry import config


def Entry(master=None, placeholder_text=None) -> CTkEntry:
    entry =  CTkEntry(master, placeholder_text=placeholder_text, **config)
    entry.insert(0, '0')
    return entry
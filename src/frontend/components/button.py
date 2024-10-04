from customtkinter import (
    CTkButton,
    CTkFrame
)


from src.frontend.styles.button import configs



def Button(master: CTkFrame, text: str = "Button") -> CTkButton:
    
    return CTkButton(
        master, 
        text=text, 
        **configs
    )

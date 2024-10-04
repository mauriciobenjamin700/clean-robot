from customtkinter import (
    CTk,
    CTkFrame,
    CTkLabel,
    CTkButton,
    CTkEntry
)


from src.frontend.styles.frame import configs_central as configs
from src.frontend.configs.position import (
    align_center,
    align_right
)
from src.frontend.components.button import Button
from src.frontend.components.label import Label
from src.frontend.components.entry import Entry

def HomePage(app: CTk):

    app.update_idletasks()

    frame = CTkFrame(app, **configs)
    x,y = align_center(app.winfo_width(), app.winfo_height(), configs["width"], configs["height"])
    frame.place(x=x, y=y)

    # Frame do menu à direita
    right_menu_width = 200  # Defina a largura do menu à direita
    right_menu_height = app.winfo_height()  # Altura do menu à direita igual à altura da aplicação
    right_menu = CTkFrame(app, width=right_menu_width, height=right_menu_height)
    right_x, right_y = align_right(app.winfo_width(), app.winfo_height(), right_menu_width, right_menu_height)
    right_menu.place(x=right_x, y=right_y)

    # Adicionando widgets ao frame do menu à direita
    label1 = Label(right_menu, text="Label 1")
    entry1 = Entry(right_menu)
    label2 = Label(right_menu, text="Label 2")
    entry2 = Entry(right_menu)

    label1.grid(row=0, column=0, padx=10, pady=5)
    entry1.grid(row=1, column=0, padx=10, pady=5)
    label2.grid(row=2, column=0, padx=10, pady=5)
    entry2.grid(row=3, column=0, padx=10, pady=5)



    app.main_frame = frame

from customtkinter import (
    CTk,
    CTkFrame,
    CTkLabel,
    CTkButton,
    CTkEntry
)


from src.frontend.styles.frame import (
    configs_central as configs,
    configs_right,
    configs_botton
)
from src.frontend.configs.position import (
    align_botton,
    align_center,
    align_right
)
from src.frontend.components.button import Button
from src.frontend.components.label import Label
from src.frontend.components.entry import Entry
from src.frontend.components.frame import BottonFrame, RightFrame

def HomePage(app: CTk):

    app.update_idletasks()

    frame = CTkFrame(app, **configs)
    x,y = align_center(app.winfo_width(), app.winfo_height(), configs["width"], configs["height"])
    frame.place(x=x, y=0)


    right_menu = RightFrame(app)
    #right_menu.configure(fg_color="red")
    
    right_x, right_y = align_right(app.winfo_width(), app.winfo_height(),configs_right["width"], configs_right["height"])

    right_menu.place(x=right_x-15, y=right_y)
    
    label_width = Label(right_menu, text="Largura")
    label_width.pack(fill=None, padx=10, pady=5)

    entry_width = Entry(right_menu)
    entry_width.pack(fill=None, padx=10, pady=5)

    label_height = Label(right_menu, text="Altura")
    label_height.pack(fill=None, padx=10, pady=5)

    entry_height = Entry(right_menu)
    entry_height.pack(fill=None, padx=10, pady=5)

    buttons = BottonFrame(app)
    buttons_x, buttons_y = align_botton(app.winfo_width(), app.winfo_height(),configs_botton["width"], configs_botton["height"])

    buttons.place(x=buttons_x, y=buttons_y-20)
    #buttons.configure(fg_color="red")

    button_left = Button(buttons, text="Cancelar")
    button_left.pack(side="left", padx=10, pady=5)

    button_right = Button(buttons, text="Gerar Tabuleiro")
    button_right.pack(side="right", padx=10, pady=5)

    app.main_frame = frame
    app.right_menu = right_menu
    app.buttons = buttons

from customtkinter import (
    CTk,
    CTkFrame,
    CTkLabel,
    CTkButton,
    CTkEntry
)


from src.frontend.styles.frame import (
    configs_central as configs,
    configs_right
)
from src.frontend.configs.position import (
    align_center,
    align_right
)
from src.frontend.components.button import Button
from src.frontend.components.label import Label
from src.frontend.components.entry import Entry
from src.frontend.components.frame import RightFrame

def HomePage(app: CTk):

    app.update_idletasks()

    frame = CTkFrame(app, **configs)
    x,y = align_center(app.winfo_width(), app.winfo_height(), configs["width"], configs["height"])
    frame.place(x=x, y=y)


    right_menu = RightFrame(app)
    #right_menu.configure(fg_color="red")
    
    right_x, right_y = align_right(app.winfo_width(), app.winfo_height(),configs_right["width"], configs_right["height"])
    right_menu.place(x=right_x, y=right_y)

    #right_menu.pack_propagate(False)
    #right_menu.grid_propagate(False)
    
    label_width = Label(right_menu, text="Largura")
    label_width.pack(fill='x', padx=10, pady=5)
    entry_width = Entry(right_menu)
    entry_width.pack(fill='x', padx=10, pady=5)
    label_height = Label(right_menu, text="Altura")
    label_height.pack(fill='x', padx=10, pady=5)
    entry_height = Entry(right_menu)
    entry_height.pack(fill='x', padx=10, pady=5)


    app.main_frame = frame
    app.right_menu = right_menu


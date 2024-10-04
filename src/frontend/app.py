from customtkinter import CTk


from src.frontend.styles.page import configs
from src.frontend.configs.position import align_center
from src.frontend.pages.home import HomePage

class App(CTk):
    def __init__(self):
        super().__init__()

        self.title("Clean Robot")

        width, height = self.winfo_screenwidth(), self.winfo_screenheight()

        x,y = align_center(width, height, configs["width"], configs["height"])

        self.geometry(f"{configs['width']}x{configs['height']}+{x}+{y}")

        self.configure(fg_color=configs["fg_color"])

        HomePage(self)

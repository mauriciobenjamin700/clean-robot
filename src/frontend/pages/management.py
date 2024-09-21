# management.py
from customtkinter import CTkFrame
from src.frontend.styles.configs.position import align_frame_center

class PageManager(CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.pages = {}
        self.current_page = None

    def add_page(self, page_name, page_class):
        page = page_class(self)
        self.pages[page_name] = page
        page.pack_forget()  # Inicialmente, esconda a página

    def show_page(self, page_name):
        if self.current_page:
            self.pages[self.current_page].pack_forget()  # Esconda a página atual
        self.pages[page_name].pack(fill="both", expand=True)  # Mostre a nova página
        self.current_page = page_name
        align_frame_center(self.master, self.pages[page_name])  # Alinhe a nova página
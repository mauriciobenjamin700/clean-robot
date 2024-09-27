from customtkinter import CTk


from tkinter.messagebox import (
    showinfo,
    showerror,
    showwarning
)

from src.backend.funcs.board import (
    generate_board, 
    generate_obstacles
)
from src.frontend.pages.home import HomeScreen
from src.frontend.pages.board import BoardScreen
from src.frontend.pages.robot import RobotScreen
from src.frontend.styles.colors.page import SCREEN
from src.frontend.styles.configs.position import (
    center_window,
    align_frame_center,
    align_frame_right
)


from src.backend.funcs.position import remove_robot

class App(CTk):
    def __init__(self):
        super().__init__()

        self.title("My APP")

        self.configure(fg_color=SCREEN)

        center_window(self)

        self.resizable(False, False)

        self.home = HomeScreen(self)

        self._show_screen(self.home)

        #self.home.pack(expand=True, fill="both")

        #align_frame_center(self, self.home.central_frame)

        #align_frame_center(self, self.central_frame)


        # Bind click event to the root window
        self.bind("<Button-1>", self.on_click)

        self.home.central_frame.button_left.bind("<Button-1>", self._exit)
        self.home.central_frame.button_right.bind("<Button-1>", self.home_to_board)


    def home_to_board(self, event):
        width = self.home.entry_WIDTH.get()
        height = self.home.entry_HEIGHT.get()


        if not width or not height:
            showerror("Erro", "Preencha todos os campos")

        elif not self._valid_numbers(width):
            showwarning("Aviso", "Insira apenas números inteiros na largura")

        elif not self._valid_numbers(height):
            showwarning("Aviso", "Insira apenas números inteiros na altura")

        else:
            try:
                if hasattr(self, 'board_screen'):
                    self.board_screen.destroy()
            except Exception as e:
                print(f"Erro ao destruir o tabuleiro: {e}")
           
            try:
                self.board = generate_board(int(width), int(height))
                self.board_screen = BoardScreen(self, self.board)
                self._show_screen(self.board_screen)
                self._forget_screen(self.home)
                align_frame_right(self, self.board_screen.entry_frame)
                align_frame_center(self, self.board_screen.central_frame)
                self.board_screen.central_frame.button_left.bind("<Button-1>", self.board_to_home)
                self.board_screen.central_frame.button_right.bind("<Button-1>", self.place_obstacles)
            except Exception as e:
                print(f"Erro ao gerar ou exibir o novo tabuleiro: {e}")

    def board_to_home(self, event):
        self._show_screen(self.home)
        self._forget_screen(self.board_screen)
        align_frame_center(self, self.home.central_frame)
        self.home.central_frame.button_right.bind("<Button-1>", self.home_to_board)       

    def place_obstacles(self, event):
        # Place obstacles in the board
        num_obstacles = self.board_screen.entry_quantity.get().strip()

        if not num_obstacles:
            showerror("Erro", "Informe pelo menos um obstáculo")
        else:
            try:
                num_obstacles = int(num_obstacles)
                if num_obstacles > 0:
                    generate_obstacles(self.board, num_obstacles)
                    self.board_screen.central_frame.inner_frame.regenerate_board(self.board)
                    self.boarder_to_robot()  # Transitar para a tela do robô
                else:
                    showerror("Erro", "Número de obstáculos inválido")
            except ValueError:
                showerror("Erro", "Número de obstáculos inválido")

    def boarder_to_robot(self):
        # Método para transitar para a tela do robô
        self.robot_screen = RobotScreen(self, self.board)
        self.robot_screen.pack(fill="both", expand=True)
        self.board_screen.pack_forget()


    def robot_to_board(self, event):
        self._show_screen(self.board_screen)
        self._forget_screen(self.robot_screen)
        align_frame_center(self, self.board_screen.central_frame)
        self.board_screen.central_frame.button_right.bind("<Button-1>", self.board_to_robot)
        self.board_screen.central_frame.button_right.configure(text="Gerar Robô")

    


    def on_click(self, event):
        # Set focus to the root window when clicking outside the entry
        if event.widget == self:
            self.focus_set()

    def _show_screen(self, screen):
        screen.pack(expand=True, fill="both")
        align_frame_center(self, screen.central_frame)
        screen.tkraise()

    def _forget_screen(self, screen):
        screen.forget()

    def _valid_numbers(self, input:str) -> bool:

        if input.isnumeric():
            value = int(input)

            if value > 0:
            
                return True
        
        return False
    

    def _exit(self, event):
        self.quit()
        self.destroy()



if __name__ == "__main__":
    app = App()
    app.mainloop()
    #self.overrideredirect(True)
    #self.update_idletasks()
from customtkinter import (
    CTkFrame,
    CTkLabel
)
from time import sleep


from src.frontend.components.entry import Entry
from src.frontend.components.label import Label
from src.frontend.components.board import BorderFrame, generate_chess_board
from src.frontend.styles.colors.page import SCREEN
from src.frontend.styles.configs.position import center_window, align_frame_center


from src.backend.funcs.position import (
    get_robot_position,
    make_move
)

class BoardScreen(CTkFrame):
    def __init__(self, master, border:list[list[int]] = None):
        super().__init__(master)

        self.master = master
        self.configure(fg_color=SCREEN)
        if not border:
            border = generate_chess_board()
        
        #border = None
        self.central_frame = BorderFrame(self, "Voltar", "Gerar Obstáculos",border)
        self.central_frame.pack()
        
        self.right_frame = CTkFrame(self, fg_color=SCREEN)
        self.right_frame.pack(side="right", anchor="e", padx=10, pady=10)

        self.entry_time_limit = Entry(self.right_frame, placeholder_text="Tempo Limite")
        self.entry_time_limit.pack(padx=10, pady=5)

        self.label_time_current = Label(self.right_frame, text="Tempo Atual: 0")



"""

    def start_cleaning(self, event):
        # Exemplo de movimentação do robô para a posição (5, 5)
        robot = get_robot_position(self.board)
        if make_move(self.board,robot):
            print("irei mover")
            label = self.central_frame.inner_frame.get_label(robot[0], robot[1])
            self.animate_movement(label)


    def animate_movement(self, label:CTkLabel):
        # Exemplo simples de animação com delay
        start_x, start_y = 0, 0  # Posição inicial
        end_x, end_y = 100, 100  # Posição final

        steps = 10
        delta_x = (end_x - start_x) / steps
        delta_y = (end_y - start_y) / steps

        for _ in range(steps):
            start_x += delta_x
            start_y += delta_y
            label.place(x=start_x, y=start_y)
            self.update()  # Atualiza a interface
            sleep(0.1)  # Delay para simular a animação

        print("Animando movimentação do robô...")
"""
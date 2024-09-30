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
    can_clean,
    clean,
    get_robot_position,
    in_board,
    make_move
)
from src.backend.constants.main import MOVES

class CleaningScreen(CTkFrame):
    def __init__(self, master, border:list[list[int]] = None):
        super().__init__(master)

        self.master = master
        self.configure(fg_color=SCREEN)
        if not border:
            border = generate_chess_board()
        else:
            self.board = border
        #border = None
        self.central_frame = BorderFrame(self, "Voltar", "Iniciar Limpeza",border)
        self.central_frame.pack()
        
        self.right_frame = CTkFrame(self, fg_color=SCREEN)
        self.right_frame.pack(side="right", anchor="e", padx=10, pady=10)

        self.entry_time_limit = Entry(self.right_frame, placeholder_text="Tempo Limite")
        self.entry_time_limit.pack(padx=10, pady=5)

        self.time_current = 0
        self.label_time_current = Label(self.right_frame, text=f"Tempo Atual: {self.time_current}")
        self.label_time_current.pack(padx=10, pady=5)



    def start_cleaning(self, event=None):
        # Exemplo de movimentação do robô para a posição (5, 5)
        self.time_current = 0
        self.deep_search_clean()

    def animate_movement(self, robot: tuple[int, int], end_x: int, end_y: int):
        # Exemplo simples de animação com delay
        start_x, start_y = robot
        #robot_x = start_x
        #robot_y = start_y

        #steps = 10
        #delta_x = (end_x - start_x) / steps
        #delta_y = (end_y - start_y) / steps

        robot_label = self.central_frame.inner_frame.get_label(start_x, start_y)
        target_label = self.central_frame.inner_frame.get_label(end_x, end_y)

        if start_x != end_x or start_y != end_y:
            # for _ in range(steps):
            #     robot_x += delta_x
            #     robot_y += delta_y
            #     robot_label.place(x=robot_x, y=robot_y)
            #     self.update()  # Atualiza a interface
            #     sleep(0.1)  # Delay para simular a animação

            # Trocar as labels de posição
            robot_label.grid(row=end_y, column=end_x)
            target_label.grid(row=start_y, column=start_x)

            # Atualizar a célula de origem para o estado correto

            labels = self.central_frame.inner_frame.list_of_labels

            if not in_board(self.board, start_x, start_y):
                print(f"start_x: {start_x} > {len(labels[0])}, start_y: {start_y} > {len(labels)}")
            else:
                labels[start_y][start_x] = target_label

            if  in_board(self.board, end_x, end_y):
                labels[end_y][end_x] = robot_label
            else:
                print(f"end_x: {end_x} > {len(labels[0])}, end_y: {end_y} > {len(labels)}")

            # Reposicionar a label do robô no centro da célula de destino
            #robot_label.place(x=0, y=0)
            # Usar after() em vez de sleep
            self.time_current+=1
            self.label_time_current.configure(text=f"Tempo Atual: {self.time_current}")
            self.after(1000, self.update)  # Delay de 1 segundo entre as atualizações


    def deep_search_clean(self):
        stack = [get_robot_position(self.board)]  # Pilha com a posição inicial do robô
        visited = set()  # Células visitadas

        def next_move():
            if stack:
                cell_x, cell_y = stack.pop()

                if (cell_x, cell_y) not in visited:
                    visited.add((cell_x, cell_y))

                    if can_clean(self.board, cell_x, cell_y):
                        clean(self.board, cell_x, cell_y)
                        self.animate_movement(get_robot_position(self.board), cell_x, cell_y)

                    for direction_x, direction_y in MOVES.values():
                        new_position_x, new_position_y = cell_x + direction_x, cell_y + direction_y
                        if in_board(self.board, new_position_x, new_position_y) :
                            if can_clean(self.board, new_position_x, new_position_y):
                                stack.append((new_position_x, new_position_y))

                    self.after(500, next_move)  # Atraso de 500ms antes do próximo movimento

        next_move()  # Iniciar o loop de movimentos
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

        self.label_time_current = Label(self.right_frame, text="Tempo Atual: 0")
        self.label_time_current.pack(padx=10, pady=5)



    def start_cleaning(self, event=None):
        # Exemplo de movimentação do robô para a posição (5, 5)
        self.deep_search_clean()

    def animate_movement(self, robot: tuple[int, int], end_x: int, end_y: int):
        # Exemplo simples de animação com delay

        start_x, start_y = robot
        robot_x = start_x
        robot_y = start_y

        steps = 10
        delta_x = (end_x - start_x) / steps
        delta_y = (end_y - start_y) / steps

        robot_label = self.central_frame.inner_frame.get_label(start_x, start_y)
        target_label = self.central_frame.inner_frame.get_label(end_x, end_y)

        if start_x != end_x or start_y != end_y:
            for _ in range(steps):
                robot_x += delta_x
                robot_y += delta_y
                robot_label.place(x=robot_x, y=robot_y)
                self.update()  # Atualiza a interface
                sleep(0.1)  # Delay para simular a animação

            # Trocar as labels de posição
            robot_label.grid(row=end_y, column=end_x)
            target_label.grid(row=start_y, column=start_x)


    def deep_search_clean(self):
        """
        Busca em profundidade (Deep Search First)

        - Args:
            - board:: list[list[int]]: tabuleiro
            - x:: int: posição x do robô
            - y:: int: posição y do robô

        - Returns:
            - None

        """
        stack = [get_robot_position(self.board)] # Pilha com a posição inicial do robo
        print(f"Stack == {stack}")
        visited = set() # Rastreando as celulas visitasdas
        
        while stack: # Rastreando enquanto houver celulas na pilha

            cell_x, cell_y = stack.pop() # Remove a célula do topo da pilha e armazena suas coordenadas em cx e cy.
            
            if not ((cell_x, cell_y) in visited): # Se a célula não foi visitada, visitar.

                visited.add((cell_x, cell_y)) # Adiciona a célula atual ao conjunto de visitados.
                
                if can_clean(self.board, cell_x, cell_y): # Verifica se a célula atual pode ser limpa
                    
                    clean(self.board, cell_x, cell_y) # Limpa a célula atual.
                    
                    self.animate_movement(
                        get_robot_position(self.board),
                        cell_x,
                        cell_y,
                    )
                
                for direction_x, direction_y in MOVES.values(): # Para cada movimento possível (cima, baixo, esquerda, direita), calcula as novas coordenadas (new_position_x, new_position_y). Se as novas coordenadas estão dentro dos limites do tabuleiro, não são obstáculos e não estão limpas, adiciona-as à pilha para exploração futura.
                    new_position_x, new_position_y = cell_x + direction_x, cell_y + direction_y
                    
                    if can_clean(self.board,new_position_x, new_position_y):
                        stack.append((new_position_x, new_position_y))

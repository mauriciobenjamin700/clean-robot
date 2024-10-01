from customtkinter import (
    CTkFrame,
)



from src.frontend.components.entry import Entry
from src.frontend.components.label import Label
from src.frontend.components.board import BorderFrame, generate_chess_board
from src.frontend.styles.colors.page import SCREEN


from src.backend.funcs.position import (
    can_clean,
    can_move,
    get_robot_position,
    in_board,
    move,
    get_direction
)
from src.backend.funcs.board import board_size
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
        self.DFS()

    def animate_movement(self):
        """
        Animação de movimento ao trocar de lugar uma peça
        """
        column, line = board_size(self.board)
        for x in range(0, column,1):
            for y in range(0, line,1):

                if in_board(self.board, x, y):
                    color = self.central_frame.inner_frame._choice_color(self.board[x][y])
                    self.central_frame.inner_frame.list_of_labels[x][y].configure(fg_color=color)

        print(f"Boarder: {self.board}")
        self.time_current+=1
        self.label_time_current.configure(text=f"Tempo Atual: {self.time_current}")
        self.after(1000, self.update)  # Delay de 1 segundo entre as atualizações

    def DFS(self):
        stack = [get_robot_position(self.board)]  # stacka e formato de Pilha com a posição inicial do robô e tudo que ele conhece até agora
        visited = set()  # Células visitadas

        def next_move():
            print(f"Pilha: {stack}\nVisitados: {visited}")
            if len(stack) > 0:  # Checar se a pilha não está vazia
                cell_x, cell_y = stack.pop()  # Obter a próxima célula a ser visitada

                if in_board(self.board, cell_x, cell_y):  # Checar se a célula está dentro do tabuleiro

                    if (cell_x, cell_y) not in visited:  # Checar se a célula já foi visitada, caso não tenha sido, vamos visitá-la
                        visited.add((cell_x, cell_y))  # Adicionar a célula atual ao conjunto de visitados

                    if can_clean(self.board, cell_x, cell_y):

                        y, x = get_robot_position(self.board)
                        direction = get_direction((x, y), cell_x, cell_y)
                        print(direction)
                        if move(self.board, x, y, direction):
                            print(f"Linha 119: {self.board}")
                            
                        self.animate_movement()
                    else:
                        print(f"Já foi Visitada: X:{cell_x}, Y:{cell_y}")
                    

                else:
                    print(f"Fora do Tabuleiro: X: {cell_x}, Y: {cell_y}")


                for direction_x, direction_y in MOVES.values():  # Percorrer as direções possíveis

                    new_position_x, new_position_y = cell_x + direction_x, cell_y + direction_y

                    if in_board(self.board, new_position_x, new_position_y) and (new_position_x, new_position_y) not in visited:  # Se a direção for válida (Estiver dentro do tabuleiro)
                        if can_move(self.board, new_position_x, new_position_y):
                            stack.append((new_position_x, new_position_y))
                self.after(1000, next_move)  # Atraso antes do próximo movimento
            else:
                print("Pilha vazia, finalizando a limpeza.")

        next_move()  # Iniciar o loop de movimentos
        print("Finalizei")


 
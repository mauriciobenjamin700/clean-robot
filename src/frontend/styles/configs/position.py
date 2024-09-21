from customtkinter import (
    CTk,
    CTkFrame
)


from src.frontend.styles.configs.size import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT
)


def center_window(frame: CTk):
    """
    Alinha um APP no centro da tela
    - Args:
        - frame:: CTk: Frame a ser alinhado
    - Return:
        - None
    """
    screen_width = frame.winfo_screenwidth()
    screen_height = frame.winfo_screenheight()

    # Calculate position x and y coordinates
    position_x = (screen_width // 2) - (SCREEN_WIDTH // 2)
    position_y = (screen_height // 2) - (SCREEN_HEIGHT // 2)

    # Set the geometry of the window
    frame.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}+{position_x}+{position_y}")

def align_frame_center(master:CTk, frame: CTkFrame, offset_x=0, offset_y=0):
    """
    Alinha um frame no centro de um master

    - Args:
        - master:: CTk: Frame principal
        - frame:: CTkFrame: Frame a ser alinhado
        - offset_x:: float: Offset em relação ao eixo x
        - offset_y:: float: Offset em relação ao eixo y
    
    - Returns:
        - None

    """
    master.update_idletasks()
    frame_width = frame.winfo_width()
    frame_height = frame.winfo_height()
    master_width = master.winfo_width()
    master_height = master.winfo_height()
    position_x = (master_width // 2) - (frame_width // 2) + int(master_width * offset_x)
    position_y = (master_height // 2) - (frame_height // 2) + int(master_height * offset_y)
    frame.place(x=position_x, y=position_y)

def align_frame_top(master:CTk, frame: CTkFrame, offset_x=0, offset_y=0):
    """
    Alinha um frame no topo de um master

    - Args:
        - master:: CTk: Frame principal
        - frame:: CTkFrame: Frame a ser alinhado
        - offset_x:: float: Offset em relação ao eixo x
        - offset_y:: float: Offset em relação ao eixo y

    - Returns:
        - None
    """
    master.update_idletasks()
    frame_width = frame.winfo_width()
    master_width = master.winfo_width()
    master_height = master.winfo_height()
    position_x = (master_width // 2) - (frame_width // 2) + int(master_width * offset_x)
    position_y = int(master_height * offset_y)
    frame.place(x=position_x, y=position_y)

def align_frame_bottom(master:CTk, frame: CTkFrame, offset_x=0, offset_y=0):
    """
    Alinha um frame na base de um master
    - Args:
        - master:: CTk: Frame principal
        - frame:: CTkFrame: Frame a ser alinhado
        - offset_x:: float: Offset em relação ao eixo x
        - offset_y:: float: Offset em relação ao eixo y

    - Return:
        - None
    """
    master.update_idletasks()
    frame_width = frame.winfo_width()
    frame_height = frame.winfo_height()
    master_width = master.winfo_width()
    master_height = master.winfo_height()
    position_x = (master_width // 2) - (frame_width // 2) + int(master_width * offset_x)
    position_y = master_height - frame_height + int(master_height * offset_y)
    frame.place(x=position_x, y=position_y)

def align_frame_left(master:CTk, frame: CTkFrame, offset_x=0, offset_y=0):
    """
    Alinha um frame na esquerda de um master
    - Args:
        - master:: CTk: Frame principal
        - frame:: CTkFrame: Frame a ser alinhado
        - offset_x:: float: Offset em relação ao eixo x
        - offset_y:: float: Offset em relação ao eixo y

    - Return:
        - None
    """
    master.update_idletasks()
    frame_height = frame.winfo_height()
    master_width = master.winfo_width()
    master_height = master.winfo_height()
    position_x = int(master_width * offset_x)
    position_y = (master_height // 2) - (frame_height // 2) + int(master_height * offset_y)
    frame.place(x=position_x, y=position_y)

def align_frame_right(master:CTk, frame: CTkFrame, offset_x=0, offset_y=0):
    """
    Alinha um frame na direita de um master
    - Args:
        - master:: CTk: Frame principal
        - frame:: CTkFrame: Frame a ser alinhado
        - offset_x:: float: Offset em relação ao eixo x
        - offset_y:: float: Offset em relação ao eixo y

    - Return:
        - None
    """
    master.update_idletasks()
    frame_width = frame.winfo_width()
    frame_height = frame.winfo_height()
    master_width = master.winfo_width()
    master_height = master.winfo_height()
    position_x = master_width - frame_width + int(master_width * offset_x)
    position_y = (master_height // 2) - (frame_height // 2) + int(master_height * offset_y)
    frame.place(x=position_x, y=position_y)
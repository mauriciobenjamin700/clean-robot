import flet as ft
from typing import Literal

def position_widget(widget, horizontal_alignment: Literal[
    "center",
    "left",
    "right",
    "top",
    "bottom"
    ],
    vertical_alignment: Literal[
    "center",
    "left",
    "right",
    "top",
    "bottom"
    ]
) -> ft.Container:
    
    alignments = {
        'bottom_right': ft.alignment.center,
        'left': ft.alignment.center_left,
        'right': ft.alignment.center_right,
        'top': ft.alignment.top_center,
        'bottom': ft.alignment.bottom_center,
        'top_left': ft.alignment.top_left,
        'top_right': ft.alignment.top_right,
        'bottom_left': ft.alignment.bottom_left,
        'bottom_right': ft.alignment.bottom_right,
        'center_left': ft.alignment.center_left,
        'center_right': ft.alignment.center_right
    }

    horizontal = alignments.get(horizontal_alignment, ft.alignment.center)
    vertical = alignments.get(vertical_alignment, ft.alignment.center)

    return ft.Container(
        content=widget,
        alignment=ft.alignment.Alignment(horizontal.x, vertical.y)
    )

if __name__ == '__main__':
        
    # Exemplo de uso
    def main(page: ft.Page):
        widget = ft.Text("Hello, Flet!")
        positioned_widget = position_widget(widget, 'top_left', 'center')
        page.add(positioned_widget)

    ft.app(target=main)
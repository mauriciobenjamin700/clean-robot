from flet import (
    alignment,
    ElevatedButton
)
from typing import Callable


from src.frontend.styles.colors.button import(
    BACKGROUND,
    TEXT
)

class Button(ElevatedButton):
    def __init__(
        self, 
        bind: Callable = None,
        text: str = "button",
        align: str = None,
        x: float = None,
        y: float = None
        ):
        
        super().__init__(
            text=text,
            color=TEXT,
            bgcolor=BACKGROUND,
            on_click=bind,
            adaptive=True,
        )
    
        # Configurar alinhamento e posição
        if align:
            self.alignment = self.get_alignment(align)
        if x is not None:
            self.left = x
        if y is not None:
            self.top = y
            
    def get_alignment(self, align: str) -> alignment.Alignment:
        alignments = {
        "left": alignment.top_left,
        "right": alignment.top_right,
        "top": alignment.top_center,
        "bottom": alignment.bottom_center,
        "center": alignment.center,
    }
        return alignments.get(align, alignment.center)

    """
    - Args:
        - text: str | None = None,
        - icon: str | None = None,
        - icon_color: str | None = None,
        - color: str | None = None,
        - bgcolor: str | None = None,
        - content: Control | None = None,
        - elevation: OptionalNumber = None,
        - style: ButtonStyle | None = None,
        - autofocus: bool | None = None,
        - clip_behavior: ClipBehavior | None = None,
        - url: str | None = None,
        - url_target: UrlTarget | None = None,
        - on_click: OptionalControlEventCallable = None,
        - on_long_press: OptionalControlEventCallable = None,
        - on_hover: OptionalControlEventCallable = None,
        - on_focus: OptionalControlEventCallable = None,
        - on_blur: OptionalControlEventCallable = None,
        -  ref: Ref | None = None,
        -  key: str | None = None,
        -  width: OptionalNumber = None,
        -  height: OptionalNumber = None,
        - left: OptionalNumber = None,
        - top: OptionalNumber = None,
        - right: OptionalNumber = None,
        - bottom: OptionalNumber = None,
        - expand: bool | int | None = None,
        - expand_loose: bool | None = None,
        - col: ResponsiveNumber | None = None,
        - opacity: OptionalNumber = None,
        - rotate: RotateValue = None,
        - scale: ScaleValue = None,
        - offset: OffsetValue = None,
        - aspect_ratio: OptionalNumber = None,
        - animate_opacity: AnimationValue = None,
        - animate_size: AnimationValue = None,
        - animate_position: AnimationValue = None,
        - animate_rotation: AnimationValue = None,
        - animate_scale: AnimationValue = None,
        - animate_offset: AnimationValue = None,
        - on_animation_end: OptionalControlEventCallable = None,
        - tooltip: TooltipValue = None,
        - visible: bool | None = None,
        - disabled: bool | None = None,
        - data: Any = None,
        - adaptive: bool | None = None
        
    - Return:
        - ElevatedButton
    """
    
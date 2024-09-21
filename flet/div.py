from flet import Container, BoxShape


class Div(Container):
    def __init__(self):
        super().__init__(
            padding=10,
            margin=10,
            border_radius=16,
            border_width=1,
            border_color="#000000",
            shape=BoxShape("RECTANGLE")
        )
        
        
        
        
"""
- content: Control | None = None, 
- padding: PaddingValue = None, 
- margin: MarginValue = None, 
- alignment: Alignment | None = None, 
- bgcolor: str | None = None, 
- gradient: Gradient | None = None, 
- blend_mode: BlendMode | None = None, 
- border: Border | None = None, 
- border_radius: BorderRadiusValue = None, 
- image_src: str | None = None, 
- image_src_base64: str | None = None, 
- image_repeat: ImageRepeat | None = None, 
- image_fit: ImageFit | None = None, 
- image_opacity: OptionalNumber = None, shape: 
- BoxShape | None = None, 
- clip_behavior: ClipBehavior | None = None, 
- ink: bool | None = None, 
- image: DecorationImage | None = None, 
- ink_color: str | None = None, 
- animate: AnimationValue = None, 
- blur:
"""
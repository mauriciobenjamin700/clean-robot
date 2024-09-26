from customtkinter import (
    CTkFrame,
    CTkEntry
)

from src.frontend.styles.configs.size import (
    ENTRY_JUSTIFY,
    ENTRY_WIDTH,
    ENTRY_HEIGHT
)
from src.frontend.styles.colors.entry import(
    BACKGROUND,
    TEXT_COLOR,
    TEXT_STYLE,
    BODER_RADIUS,
    BORDER_COLOR,
    BORDER_WIDTH,
    PLACEHOLDER,
)


class Entry(CTkEntry):
    def __init__(
            self, 
            master=None,
            placeholder_text: str = "Placeholder",
            **kwargs
        ):
        super().__init__(
            master,
            fg_color=BACKGROUND,
            text_color=PLACEHOLDER,  # Inicialmente, a cor do texto é a cor do placeholder
            font=TEXT_STYLE,
            corner_radius=BODER_RADIUS,
            border_color=BORDER_COLOR,
            border_width=BORDER_WIDTH,
            justify=ENTRY_JUSTIFY,
            height=ENTRY_HEIGHT,
            width=ENTRY_WIDTH,
            placeholder_text=placeholder_text,
            **kwargs
        )

        self.placeholder = placeholder_text

        # Bind events
        self.bind("<FocusIn>", self._on_focus_in)
        self.bind("<FocusOut>", self._on_focus_out)

    def get(self) -> str:
        value = super().get().strip()

        if not value or len(value) == 0:
            value = self.placeholder

        return value

            
    def get_int(self):
        value = self.get()

        if value.isnumeric():
            value.replace(" ", "").replace(",", ".")
            if "." in value:
                return float(value)
            else:
                return int(value)
        else:
            raise ValueError("Insira números")

    def _on_focus_in(self, event):
        value = self.get()
        if value == self.placeholder:
            self.delete(0, "end")
            self.configure(text_color=TEXT_COLOR)  # Ajuste a cor do texto para a cor normal

    def _on_focus_out(self, event):
        if self.get() == self.placeholder:
            self.delete(0, "end")
            self.insert(0, self._placeholder_text)
            self.configure(text_color=PLACEHOLDER)  # Ajuste a cor do texto para a cor do placeholder

    def clean(self):
        self.delete(0, "end")
        self.insert(0, self.placeholder)
        self.configure(text_color=PLACEHOLDER)  # Ajuste a cor do texto para a cor do placeholder
        self.refrash()


    def refrash(self):
        self.update_idletasks()
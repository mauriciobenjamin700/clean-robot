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
            placeholder_text:str="Placeholder",
            **kwargs
        ):
        super().__init__(
            master,
            fg_color=BACKGROUND,
            text_color=TEXT_COLOR,
            font=TEXT_STYLE,
            corner_radius=BODER_RADIUS,
            border_color=BORDER_COLOR,
            border_width=BORDER_WIDTH,
            placeholder_text_color=PLACEHOLDER,
            justify=ENTRY_JUSTIFY,
            height=ENTRY_HEIGHT,
            width=ENTRY_WIDTH,
            **kwargs
        )

        # Set placeholder text
        #self.placeholder_text = kwargs.get("placeholder_text", "")
        self._placeholder_text = placeholder_text
        self.insert(0, self._placeholder_text)

        # Bind events
        self.bind("<FocusIn>", self._on_focus_in)
        self.bind("<FocusOut>", self._on_focus_out)

    def _on_focus_in(self, event):
        if self.get() == self._placeholder_text:
            self.delete(0, "end")

    def _on_focus_out(self, event):
        if self.get() == "":
            self.insert(0, self._placeholder_text)

from flet import (
    Page,
    SafeArea,
    Text
)


from src.frontend.components.button import Button

def Home(page: Page):
    page.add(SafeArea(Text("Welcome to the Home Page")))
    page.add(SafeArea(Button()))
from flet import (
    alignment,
    Page,
    SafeArea,
    Stack,
    Text,
    Row,
    MainAxisAlignment
)


from src.frontend.components.button import Button

def Home(page: Page):
    page.add(SafeArea(Text("Welcome to the Home Page")))
    page.add(
        Row(
            [
                Button(text="Go to Home", bind=lambda e: print("Button clicked"))
            ]
        )
    ),
    page.add(
        Stack(
            [
                Text("Hello, Flet!"),
                Text("This is a simple application using Flet")
            ],
            alignment=MainAxisAlignment.CENTER
        )
    )
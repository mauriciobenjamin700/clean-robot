from flet import (
    Checkbox,
    TextField,
    Row,
    ElevatedButton
)

def Entry(page, bind):
    page.add(Checkbox(label=new_task.value))
    new_task.value = ""
    new_task.focus()
    new_task.update()

    new_task = TextField(hint_text="What's needs to be done?", width=300)
    page.add(Row([new_task, ElevatedButton("Add", on_click=bind)]))
    
    
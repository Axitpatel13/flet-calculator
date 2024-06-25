import flet as ft

def main(page: ft.Page):
    page.title = "Simple Calculator App"
    #page.theme_mode = "dark"     
    #users greetings
    answer = ft.Column()
    #click event
    def add_btn(e):
        answer.controls.clear()
        answer.controls.append(ft.Text(int(first_no.value) + int(last_no.value)))
        first_no.value = ""
        last_no.value = ""
        page.update()
        
    def sub_btn(e):
        answer.controls.clear()
        answer.controls.append(ft.Text(int(first_no.value) - int(last_no.value)))
        first_no.value = ""
        last_no.value = ""
        page.update()
        
    def mul_btn(e):
        answer.controls.clear()
        answer.controls.append(ft.Text(int(first_no.value) * int(last_no.value)))
        first_no.value = ""
        last_no.value = ""
        page.update()
        
    def div_btn(e):
        answer.controls.clear()
        answer.controls.append(ft.Text(int(first_no.value) / int(last_no.value)))
        first_no.value = ""
        last_no.value = ""
        page.update()
    
    #user input
    first_no = ft.TextField(label="Enter First Number: ", autofocus=True)
    last_no = ft.TextField(label="Enter Second Number: ")
    
    #button
    page.add(
        first_no,
        last_no
    )
    
    page.add(
        ft.Row(
            [
                ft.ElevatedButton("Addition",on_click=add_btn),
                ft.ElevatedButton("Subtraction",on_click=sub_btn),   
            ]
        )
    )
    
    page.add(
        ft.Row(
            [
                ft.ElevatedButton("Multiplication",on_click=mul_btn),   
                ft.ElevatedButton("Divison",on_click=div_btn)   
            ]
        )
    )
    
    page.add(
        ft.Row(
            [
                answer
            ]
        )
    )
    
ft.app(target=main)
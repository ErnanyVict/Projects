from flet import *



def App(page: Page):
    def tecla(e: KeyboardEvent):
        page.add(Text(f'Tecla pressionada: {e.key}, Shift: {e.shift}, Alt: {e.alt}, Control: {e.ctrl}, Meta: {e.meta}'))
        page.update()
    page.on_keyboard_event = tecla
    page.add( Text("Pressione qualquer telca"))
    

app(target=App)
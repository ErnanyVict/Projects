from tkinter import * 

menu_inicial = Tk() # type: ignore Criar pagina inicial
menu_inicial.title("App") # Mudar nome do programa
menu_inicial.geometry("500x300+500+200") # tamanho da pagina e lugar e estabelecer onde a pagina vai aparecer
menu_inicial.resizable(True, True)  # Permitir que o user possa mudar o tamanho
menu_inicial.minsize(500, 300) # Tamanho minimo da pagina
menu_inicial.maxsize(700, 400) # Tamanho maximo da pagina
# menu_inicial.state("zoomed") "zoomed" = maximizar a pagina, "iconic" = minimizar a pagina
# menu_inicial.iconbitmap("caminho até o ícone") muda o ícone 
menu_inicial.mainloop()


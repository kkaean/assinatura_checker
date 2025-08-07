# main.py (código atualizado)

import tkinter as tk
from model.model import ContadorDeArquivosModel
from view.gui_view import ContadorDeArquivosGUIView
from controller.controller import ContadorDeArquivosController

if __name__ == "__main__":
    # Inicializa o Tkinter
    root = tk.Tk()
    
    # Instancia as classes do MVC
    model = ContadorDeArquivosModel()
    controller = ContadorDeArquivosController(model)
    view = ContadorDeArquivosGUIView(root, controller)
    
    # Conecta a View ao Controller
    controller.set_view(view)
    
    # Inicia o loop principal da interface gráfica
    root.mainloop()
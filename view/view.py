# view/view.py
import tkinter as tk
from tkinter import filedialog
from controller.controller import AssinaturaController

class AssinaturaView:
    def __init__(self, root):
        self.root = root
        self.root.title("Verificador de Assinaturas PDF")
        self.root.geometry("400x300")
        self.controller = AssinaturaController()

        self.label = tk.Label(root, text="Selecione a pasta com arquivos PDF:")
        self.label.pack(pady=10)

        self.botao_selecionar = tk.Button(root, text="Selecionar Pasta", command=self.selecionar_pasta)
        self.botao_selecionar.pack(pady=5)

        self.resultado = tk.Text(root, height=10, width=50)
        self.resultado.pack(pady=10)

    def selecionar_pasta(self):
        caminho = filedialog.askdirectory()
        if caminho:
            resultado = self.controller.processar_diretorio(caminho)
            self.exibir_resultado(resultado)

    def exibir_resultado(self, dados):
        self.resultado.delete("1.0", tk.END)
        self.resultado.insert(tk.END, f"📁 Pastas: {dados['pastas']}\n")
        self.resultado.insert(tk.END, f"📄 Arquivos: {dados['arquivos']}\n")
        self.resultado.insert(tk.END, f"✅ Assinados: {dados['assinados']}\n")
        self.resultado.insert(tk.END, f"❌ Não assinados: {dados['nao_assinados']}\n")

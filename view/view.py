import tkinter as tk
from tkinter import filedialog, scrolledtext
from controller.controller import AssinaturaController

class AssinaturaView:
    def __init__(self):
        self.controller = AssinaturaController()
        self.root = tk.Tk()
        self.root.title("Verificador de Assinaturas Digitais do Governo")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        # Título
        titulo = tk.Label(self.root, text="Verificador de Assinaturas Digitais em PDFs", font=("Arial", 16, "bold"))
        titulo.pack(pady=10)

        # Botão de seleção
        self.botao = tk.Button(self.root, text="📁 Selecionar Pasta", font=("Arial", 12), command=self.selecionar_pasta)
        self.botao.pack(pady=10)

        # Área de resultados
        self.resultado_texto = scrolledtext.ScrolledText(self.root, height=25, width=100, font=("Consolas", 10))
        self.resultado_texto.pack(pady=10)

        self.root.mainloop()

    def selecionar_pasta(self):
        caminho = filedialog.askdirectory(title="Selecione a pasta com PDFs")
        if caminho:
            self.resultado_texto.delete("1.0", tk.END)
            resultado, resumo = self.controller.processar_diretorio_completo(caminho)

            for pasta in resultado:
                self.resultado_texto.insert(tk.END, f"📂 Pasta: {pasta['pasta']}\n")
                for arquivo in pasta['arquivos']:
                    status = "✅ Assinado" if arquivo['assinado'] else "❌ Não assinado"
                    self.resultado_texto.insert(
                        tk.END,
                        f"   - {arquivo['nome']} | {arquivo['paginas']} pág. | {status}\n"
                    )
                self.resultado_texto.insert(tk.END, "\n")

            self.resultado_texto.insert(tk.END, "📊 Resumo Geral:\n")
            self.resultado_texto.insert(tk.END, f" - Pastas analisadas: {resumo['total_pastas']}\n")
            self.resultado_texto.insert(tk.END, f" - PDFs encontrados: {resumo['total_pdfs']}\n")
            self.resultado_texto.insert(tk.END, f" - PDFs assinados: {resumo['total_assinados']}\n")

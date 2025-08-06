import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from controller.controller import AssinaturaController

class AssinaturaView:
    def __init__(self):
        self.controller = AssinaturaController()
        self.root = tk.Tk()
        self.root.title("Verificador de Assinaturas Digitais do Governo")
        self.root.geometry("700x500")

        self.label = tk.Label(self.root, text="Selecione a pasta principal:")
        self.label.pack(pady=10)

        self.botao = tk.Button(self.root, text="Selecionar Pasta", command=self.selecionar_pasta)
        self.botao.pack(pady=10)

        self.resultado_texto = scrolledtext.ScrolledText(self.root, height=20, width=90)
        self.resultado_texto.pack(pady=10)

        self.root.mainloop()

    def selecionar_pasta(self):
        caminho = filedialog.askdirectory()
        if caminho:
            self.resultado_texto.delete("1.0", tk.END)
            resultado, resumo = self.controller.processar_diretorio_completo(caminho)

            for pasta in resultado:
                self.resultado_texto.insert(tk.END, f"📁 {pasta['pasta']}\n")
                for arquivo in pasta['arquivos']:
                    status = "✅ Assinado" if arquivo['assinado'] else "❌ Não assinado"
                    self.resultado_texto.insert(
                        tk.END,
                        f"  - {arquivo['nome']} | {arquivo['paginas']} página(s) | {status}\n"
                    )
                self.resultado_texto.insert(tk.END, "\n")

            self.resultado_texto.insert(tk.END, "📊 Resumo:\n")
            self.resultado_texto.insert(tk.END, f"- Total de pastas: {resumo['total_pastas']}\n")
            self.resultado_texto.insert(tk.END, f"- Total de PDFs: {resumo['total_pdfs']}\n")
            self.resultado_texto.insert(tk.END, f"- PDFs assinados: {resumo['total_assinados']}\n")

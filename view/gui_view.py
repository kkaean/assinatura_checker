# view/gui_view.py

import tkinter as tk
from tkinter import filedialog, scrolledtext

class ContadorDeArquivosGUIView:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("Contador de Páginas")
        self.root.geometry("800x600")

        # Configura o layout da janela
        self.frame = tk.Frame(self.root, padx=10, pady=10)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Campo de entrada para o caminho
        self.caminho_label = tk.Label(self.frame, text="Diretório:", anchor="w")
        self.caminho_label.pack(fill="x", pady=(0, 5))
        self.caminho_var = tk.StringVar(value="")
        self.caminho_entry = tk.Entry(self.frame, textvariable=self.caminho_var)
        self.caminho_entry.pack(fill="x", pady=(0, 5))

        # Botão para selecionar o diretório
        self.selecionar_botao = tk.Button(self.frame, text="Selecionar Diretório", command=self.selecionar_diretorio)
        self.selecionar_botao.pack(fill="x", pady=(0, 10))
        
        # Botão para iniciar a análise
        self.analisar_botao = tk.Button(self.frame, text="Iniciar Análise", command=self.iniciar_analise_click)
        self.analisar_botao.pack(fill="x", pady=(0, 10))

        # Área de texto para exibir os resultados
        self.resultados_text = scrolledtext.ScrolledText(self.frame, wrap=tk.WORD)
        self.resultados_text.pack(fill=tk.BOTH, expand=True)
        self.resultados_text.configure(state=tk.DISABLED) # Começa desabilitado

    def selecionar_diretorio(self):
        caminho = filedialog.askdirectory()
        if caminho:
            self.caminho_var.set(caminho)

    def iniciar_analise_click(self):
        caminho = self.caminho_var.get()
        if not caminho:
            self.exibir_mensagem("Por favor, selecione um diretório.")
            return

        self.exibir_mensagem("Iniciando a análise...", limpar=True)
        self.controller.iniciar_analise(caminho)

    def exibir_mensagem(self, mensagem, limpar=False):
        self.resultados_text.configure(state=tk.NORMAL)
        if limpar:
            self.resultados_text.delete(1.0, tk.END)
        self.resultados_text.insert(tk.END, mensagem + "\n")
        self.resultados_text.see(tk.END) # Rola para o final
        self.resultados_text.configure(state=tk.DISABLED)

    def exibir_detalhes_pasta(self, pasta, dados_pasta):
        mensagem = f"--- Pasta: {pasta} ---\n"
        mensagem += f"Encontrados {dados_pasta['num_arquivos']} arquivos PDF.\n"
        
        for arquivo in dados_pasta['arquivos']:
            if 'erro' in arquivo:
                mensagem += f"  - Erro ao processar '{arquivo['nome']}': {arquivo['erro']}\n"
            else:
                mensagem += f"  - Arquivo '{arquivo['nome']}': {arquivo['paginas']} páginas.\n"
        mensagem += "-" * 20 + "\n"
        self.exibir_mensagem(mensagem)

    def exibir_resumo(self, resumo_dados):
        mensagem = "\n" + "=" * 30 + "\n"
        mensagem += "Resumo Final\n"
        mensagem += "=" * 30 + "\n"
        mensagem += f"Total de pastas verificadas: {resumo_dados['total_pastas']}\n"
        mensagem += f"Total de arquivos PDF encontrados: {resumo_dados['total_arquivos_pdf']}\n"
        mensagem += f"Soma total de páginas (apenas de PDFs): {resumo_dados['total_paginas']}\n"
        self.exibir_mensagem(mensagem)
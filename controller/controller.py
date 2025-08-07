# controller/controller.py (código atualizado)

from model.model import ContadorDeArquivosModel

class ContadorDeArquivosController:
    def __init__(self, model):
        self.model = model
        self.view = None  # A View será definida depois

    def set_view(self, view):
        self.view = view

    def iniciar_analise(self, caminho_base):
        """
        Orquestra o processo de análise e exibição.
        """
        if not self.view:
            print("Erro: View não definida.")
            return

        self.view.exibir_mensagem(f"Buscando a partir de: {caminho_base}\n")
        
        dados_analise = self.model.analisar_diretorio(caminho_base)
        
        for pasta, dados_pasta in dados_analise['detalhes_por_pasta'].items():
            self.view.exibir_detalhes_pasta(pasta, dados_pasta)
            
        self.view.exibir_resumo(dados_analise)
# controller/controller.py
from model.model import AssinaturaModel

class AssinaturaController:
    def __init__(self):
        self.model = AssinaturaModel()

    def processar_diretorio(self, caminho):
        return self.model.analisar_diretorio(caminho)

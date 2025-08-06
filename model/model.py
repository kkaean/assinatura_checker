# model/model.py
import os
import fitz  # PyMuPDF

class AssinaturaModel:
    def __init__(self):
        self.total_pastas = 0
        self.total_arquivos = 0
        self.assinados = 0
        self.nao_assinados = 0

    def verificar_assinatura_visual(self, caminho_pdf):
        try:
            doc = fitz.open(caminho_pdf)
            for pagina in doc:
                texto = pagina.get_text()
                if texto and ("Assinado digitalmente" in texto or "Assinatura" in texto):
                    return True
        except Exception as e:
            print(f"Erro ao verificar assinatura: {e}")
        return False

    def analisar_diretorio(self, caminho_raiz):
        self.total_pastas = 0
        self.total_arquivos = 0
        self.assinados = 0
        self.nao_assinados = 0

        for pasta_atual, subpastas, arquivos in os.walk(caminho_raiz):
            self.total_pastas += len(subpastas)
            for arquivo in arquivos:
                self.total_arquivos += 1
                caminho_arquivo = os.path.join(pasta_atual, arquivo)
                if arquivo.lower().endswith('.pdf'):
                    if self.verificar_assinatura_visual(caminho_arquivo):
                        self.assinados += 1
                    else:
                        self.nao_assinados += 1

        return {
            "pastas": self.total_pastas,
            "arquivos": self.total_arquivos,
            "assinados": self.assinados,
            "nao_assinados": self.nao_assinados
        }

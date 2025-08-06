import os
import fitz  # PyMuPDF

class AssinaturaModel:
    def __init__(self):
        pass

    def verificar_assinatura_visual(self, caminho_pdf):
        """
        Verifica se o PDF contém indícios visuais de assinatura digital do governo.
        Procura por frases comuns como 'Documento assinado digitalmente' ou 'Verifique em validar.iti.gov.br'.
        """
        try:
            if not os.path.exists(caminho_pdf):
                print(f"Arquivo não encontrado: {caminho_pdf}")
                return False

            doc = fitz.open(caminho_pdf)
            for pagina in doc:
                texto = pagina.get_text()
                if texto:
                    texto = texto.lower()
                    padroes = [
                        "documento assinado digitalmente",
                        "verifique em validar.iti.gov.br",
                        "assinatura gov.br",
                        "assinatura eletrônica",
                        "assinado digitalmente por"
                    ]
                    for padrao in padroes:
                        if padrao in texto:
                            return True
        except Exception as e:
            print(f"Erro ao verificar assinatura: {e}")
        return False

    def verificar_assinatura_em_lote(self, lista_caminhos):
        """
        Verifica múltiplos arquivos PDF e retorna um dicionário com os resultados.
        """
        resultados = {}
        for caminho in lista_caminhos:
            resultados[caminho] = self.verificar_assinatura_visual(caminho)
        return resultados

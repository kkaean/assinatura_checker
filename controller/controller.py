import os
import fitz
from model.model import AssinaturaModel

class AssinaturaController:
    def __init__(self):
        self.verificador = AssinaturaModel()

    def processar_diretorio_completo(self, caminho_raiz):
        resultado_final = []
        total_pdfs = 0
        total_assinados = 0
        total_pastas = 0

        for pasta_atual, _, arquivos in os.walk(caminho_raiz):
            pdfs_na_pasta = []
            for arquivo in arquivos:
                if arquivo.lower().endswith(".pdf"):
                    total_pdfs += 1
                    caminho_pdf = os.path.join(pasta_atual, arquivo)
                    try:
                        doc = fitz.open(caminho_pdf)
                        num_paginas = doc.page_count
                        assinado = self.verificador.verificar_assinatura_visual(caminho_pdf)
                        if assinado:
                            total_assinados += 1
                        pdfs_na_pasta.append({
                            "nome": arquivo,
                            "paginas": num_paginas,
                            "assinado": assinado
                        })
                    except Exception as e:
                        print(f"Erro ao abrir {arquivo}: {e}")
            if pdfs_na_pasta:
                total_pastas += 1
                resultado_final.append({
                    "pasta": os.path.basename(pasta_atual),
                    "arquivos": pdfs_na_pasta
                })

        resumo = {
            "total_pastas": total_pastas,
            "total_pdfs": total_pdfs,
            "total_assinados": total_assinados
        }

        return resultado_final, resumo

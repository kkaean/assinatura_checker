# model/model.py

import os
import fitz  # PyMuPDF

class ContadorDeArquivosModel:
    def analisar_diretorio(self, caminho_base):
        """
        Percorre o diretório e seus subdiretórios para contar pastas,
        arquivos e páginas de PDFs.
        Retorna um dicionário com todos os dados coletados.
        """
        total_pastas = 0
        total_arquivos_pdf = 0
        total_paginas = 0
        detalhes_por_pasta = {}

        for root, dirs, files in os.walk(caminho_base):
            total_pastas += 1
            
            arquivos_pdf_na_pasta = [f for f in files if f.lower().endswith('.pdf')]
            
            if arquivos_pdf_na_pasta:
                detalhes_por_pasta[root] = {
                    'num_arquivos': len(arquivos_pdf_na_pasta),
                    'arquivos': []
                }
                
                total_arquivos_pdf += len(arquivos_pdf_na_pasta)
                
                for arquivo in arquivos_pdf_na_pasta:
                    caminho_completo = os.path.join(root, arquivo)
                    
                    try:
                        doc = fitz.open(caminho_completo)
                        num_paginas = doc.page_count
                        doc.close()
                        
                        detalhes_por_pasta[root]['arquivos'].append({
                            'nome': arquivo,
                            'paginas': num_paginas
                        })
                        total_paginas += num_paginas
                        
                    except Exception as e:
                        detalhes_por_pasta[root]['arquivos'].append({
                            'nome': arquivo,
                            'erro': str(e)
                        })
        
        return {
            'total_pastas': total_pastas,
            'total_arquivos_pdf': total_arquivos_pdf,
            'total_paginas': total_paginas,
            'detalhes_por_pasta': detalhes_por_pasta
        }
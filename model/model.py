import os
import fitz  # PyMuPDF
import pikepdf

class AssinaturaModel:
    def verificar_assinatura(self, caminho_pdf):
        if not os.path.exists(caminho_pdf):
            print(f"❌ Arquivo não encontrado: {caminho_pdf}")
            return False

        if self._verificar_visivel(caminho_pdf):
            return True
        if self._verificar_embutido(caminho_pdf):
            return True
        return False

    def _verificar_visivel(self, caminho_pdf):
        try:
            doc = fitz.open(caminho_pdf)
            frases = [
                "documento assinado digitalmente",
                "assinatura digital",
                "certificado digital",
                "assinatura eletrônica",
                "assinatura com certificado"
            ]
            for pagina in doc:
                texto = pagina.get_text().lower()
                if any(frase in texto for frase in frases):
                    return True
            for campo in doc.widgets():
                if campo.field_type == fitz.PDF_WIDGET_TYPE_SIGNATURE:
                    return True
        except Exception as e:
            print(f"⚠️ Erro ao verificar texto visível: {e}")
        return False

    def _verificar_embutido(self, caminho_pdf):
        try:
            with pikepdf.open(caminho_pdf) as pdf:
                if "/AcroForm" in pdf.root:
                    acroform = pdf.root["/AcroForm"]
                    if "/Fields" in acroform:
                        for campo in acroform["/Fields"]:
                            obj = campo.get_object()
                            if obj.get("/FT") == "/Sig":
                                return True
                for nome, valor in pdf.docinfo.items():
                    if "sig" in nome.lower() or "assinatura" in nome.lower():
                        return True
        except Exception as e:
            print(f"⚠️ Erro ao verificar assinatura embutida: {e}")
        return False

import base64
import os

class ImagemService:

    def converter_para_base64(self, caminho_arquivo: str) -> str:
        if not os.path.exists(caminho_arquivo):
            raise FileNotFoundError(f"Arquivo não encontrado: {caminho_arquivo}")
            
        with open(caminho_arquivo, "rb") as file:
            bytes_imagem = file.read()
            return base64.b64encode(bytes_imagem).decode('utf-8')

    def salvar_base64(self, base64_str: str, caminho_saida: str) -> None:
        img_bytes = base64.b64decode(base64_str.encode('utf-8'))
        with open(caminho_saida, "wb") as file:
            file.write(img_bytes)
import base64
import os
import platform
import subprocess

class ImagemService:

    def salvar_base64(self, base64_str: str, caminho_saida: str) -> None:
        img_bytes = base64.b64decode(base64_str.encode('utf-8'))
        with open(caminho_saida, "wb") as file:
            file.write(img_bytes)
            
        self._abrir_no_chrome(caminho_saida)

    def _abrir_no_chrome(self, caminho_imagem: str) -> None:
        try:
            caminho_absoluto = os.path.abspath(caminho_imagem)
            sistema = platform.system().lower()

            if "windows" in sistema:
                subprocess.run(f'cmd /c start chrome "{caminho_absoluto}"', shell=True)
            elif "darwin" in sistema:  # macOS
                subprocess.run(["open", "-a", "Google Chrome", caminho_absoluto])
            else:  # Linux (Ubuntu)
                subprocess.run(["google-chrome", caminho_absoluto])
        except Exception as e:
            print(f"Erro ao abrir a imagem no Chrome: {e}")
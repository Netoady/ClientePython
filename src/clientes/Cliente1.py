import socket
import sys
import os

# Adiciona o diretório raiz do projeto ao PATH para localizar os pacotes src.menu e src.img
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.Menu.Menu_Cliente import MenuCliente

def main():
    try:
        Cliente_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Cliente_Socket.connect(('?.?.?.?', 12345))

        print("[Cliente 1] CONECTADO!!!!!!!")

        # Garante leitura linha a linha equivalente ao Scanner do Java
        socket_file = Cliente_Socket.makefile('r', encoding='utf-8')

        menu = MenuCliente(Cliente_Socket, socket_file)
        menu.iniciar()

    except Exception as erro:
        print(f"Erro na conexão: {erro}")

    finally:
        if 'Cliente_Socket' in locals():
            Cliente_Socket.close()

if __name__ == "__main__":
    main()
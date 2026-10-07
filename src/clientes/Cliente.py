import os
import socket
import sys

# Adiciona a raiz do projeto ao sys.path para import dos pacotes src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.Menu.Menu_Cliente import MenuCliente

def main():
    cliente_socket = None
    try:
        cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente_socket.connect(('?.?.?.?', 12345))

        print("[Cliente] CONECTADO!!!!!!!")

        # Garante leitura/escrita linha a linha com suporte a texto
        socket_file = cliente_socket.makefile('r', encoding='utf-8')

        menu = MenuCliente(cliente_socket, socket_file)
        menu.iniciar()

    except Exception as erro:
        print(f"Erro na conexão: {erro}")

    finally:
        if cliente_socket:
            cliente_socket.close()

if __name__ == "__main__":
    main()
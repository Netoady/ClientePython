import socket
import sys

def main():
    # Código principal do Cliente.py
    try:

        Cliente_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        Cliente_Socket.connect(('192.168.68.110', 12345))

        print("CONECTADO!!!!!!!")

        while True:

            linha_teclado = sys.stdin.readline()

            if not linha_teclado:
                break


            Cliente_Socket.sendall(linha_teclado.encode('utf-8'))


            dados_recebidos = Cliente_Socket.recv(4096)


            if not dados_recebidos:
                print("CONEXÃO ENCERRADA PELO SERVIDOR!!!!!!!!")
                break

            tempo = dados_recebidos.decode('utf-8').rstrip('\r\n')

            print(tempo)


    except Exception as erro:
        print(f"Erro na conexão: {erro}")


    finally:

        if 'Cliente_Socket' in locals():
            Cliente_Socket.close()

if _name_ == "_main_":
    main()
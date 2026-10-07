import os
import socket
import sys
import threading
import time  # Importado para o sleep

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

def simular_cliente(id_cliente: int) -> None:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('?.?.?.?', 12345))
        socket_file = s.makefile('r', encoding='utf-8')

        print(f"[TESTE CLIENTE {id_cliente}] CONECTADO!")

        # 1. Operação de Soma (1;10;20)
        s.sendall(b"1;10;20\n")
        resposta_soma = socket_file.readline().rstrip('\r\n')
        print(f"[TESTE CLIENTE {id_cliente}] Resposta Soma: {resposta_soma}")

        # Pausa de 1 segundo simulando a decisão do usuário no menu
        time.sleep(1)

        # 2. Envio de Mensagem (5;...)
        msg = f"5;Ola Servidor do Cliente {id_cliente}\n"
        s.sendall(msg.encode('utf-8'))
        resposta_msg = socket_file.readline().rstrip('\r\n')
        print(f"[TESTE CLIENTE {id_cliente}] Resposta Mensagem: {resposta_msg}")

        # Pausa final de 1 segundo antes de desconectar
        time.sleep(1)

        # Encerramento limpo
        s.sendall(b"0\n")
        s.close()
        print(f"[TESTE CLIENTE {id_cliente}] Finalizado com sucesso.")

    except Exception as erro:
        print(f"[TESTE CLIENTE {id_cliente}] Erro: {erro}")

def main():
    qtd_clientes = 15
    threads = []

    print(f"=== INICIANDO TESTE COM {qtd_clientes} THREADS SIMULTÂNEAS ===")

    for i in range(1, qtd_clientes + 1):
        t = threading.Thread(target=simular_cliente, args=(i,))
        threads.append(t)
        t.start()
        time.sleep(0.05)  # Pequeno delay (50ms) entre conexões para escalonamento suave

    for t in threads:
        t.join()

    print("\n=== TESTE FINALIZADO! ===")

if __name__ == "__main__":
    main()
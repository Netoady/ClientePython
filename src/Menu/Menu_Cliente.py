import socket
from src.img.Imagem_Service import ImagemService

class MenuCliente:

    def __init__(self, cliente_socket: socket.socket, socket_file):
        self.cliente_socket = cliente_socket
        self.socket_file = socket_file
        self.imagem_service = ImagemService()

    def iniciar(self) -> None:
        opcao = -1
        while opcao != 0:
            self._mostrar_menu()
            try:
                entrada = input("Escolha uma opção: ").strip()
                opcao = int(entrada)

                if opcao in (1, 2, 3, 4):
                    self._realizar_operacao(opcao)
                elif opcao == 5:
                    self._solicitar_e_receber_img()
                elif opcao == 6:
                    self._enviar_mensagem()
                elif opcao == 0:
                    self._enviar_linha("0")
                    print("SAINDO DO PROGRAMA!!!!!!")
                else:
                    print("!!!!!OPÇÃO INVÁLIDA, TENTE NOVAMENTE!!!!!")

            except ValueError:
                print("!!!!!DIGITE UM NÚMERO VÁLIDO!!!!!")
            except Exception as e:
                print(f"Erro na comunicação: {e}")
                break

    def _mostrar_menu(self) -> None:
        print("\n!!MENU!!")
        print("1 - OPÇÃO 1-(Somar)")
        print("2 - OPÇÃO 2-(Subtrair)")
        print("3 - OPÇÃO 3-(Multiplicar)")
        print("4 - OPÇÃO 4-(Dividir)")
        print("5 - OPÇÃO 5-(Imagem Base64)")
        print("6 - OPÇÃO 6 -(Mensagem)")
        print("0 - SAIR")

    def _enviar_linha(self, texto: str) -> None:
        self.cliente_socket.sendall(f"{texto}\n".encode('utf-8'))

    def _ler_linha(self) -> str:
        return self.socket_file.readline().rstrip('\r\n')

    def _solicitar_e_receber_img(self) -> None:
        self._enviar_linha("5")  # Solicita a imagem ao servidor
        print("Solicitando imagem ao servidor...")

        resposta_base64 = self._ler_linha()
        self.imagem_service.salvar_base64(resposta_base64, "imagem_recebida.png")
        print("IMG RECEBIDA E ABERTA NO CHROME COM SUCESSO!!!")

    def _realizar_operacao(self, operacao: int) -> None:
        n1 = input("Digite o primeiro número: ")
        n2 = input("Digite o segundo número: ")
        
        self._enviar_linha(f"{operacao};{n1};{n2}")
        resposta = self._ler_linha()
        print(f"Resultado: {resposta}")

    def _enviar_mensagem(self) -> None:
        msg = input("Digite a mensagem: ")
        self._enviar_linha(f"6;{msg}")
        resposta = self._ler_linha()
        print(f"Servidor: {resposta}")
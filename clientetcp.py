import socket
import sys

def main():
    try:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    except socket.error as e:
        print('A conexão falhou')
        print('Erro: {}'.format(e))
        sys.exit()

    print('Socket criado com sucesso')

    hostalvo = input('Digite o Host ou IP a ser conectado: ')
    portaalvo= input("Digite a porta a ser conectada: ")

    try:
        s.connect((hostalvo, int(portaalvo)))
        print('Cliente TCP conectado com sucesso ao host: '+ hostalvo + ' e a Porta: '+ portaalvo)
        s.shutdown(2)
    except socket.error as e:
        print('Não foi possível conectar ao host: '+ hostalvo + ' e a Porta: '+ portaalvo)
        print('Erro: {}'.format(e))
        sys.exit()



if __name__ == '__main__':
    main()

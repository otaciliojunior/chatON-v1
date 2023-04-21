import socket

# Configurações do cliente
HOST = '10.0.0.40'  # Use o endereço IP correto do servidor
PORT = 80 # Use a porta correta do servidor

# Cria o socket do cliente
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Loop para enviar e receber mensagens
while True:
    message = input('Digite sua mensagem: ')
    s.sendall(message.encode('utf-8'))
    if message == 'bye':
        # Se o cliente digitar 'bye', fecha a conexão e encerra o chat
        break
    data = s.recv(1024).decode('utf-8')
    print(f'Resposta do servidor: {data}')

s.close()
import socket


def client():
    # Create client socket (AF_INET => IP, SOCK_STREAM => TCP)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 5000))
    question = input("ask me a question: ")
    sock.send(question.encode())
    from_server = sock.recv(4096)
    sock.close()
    print(from_server.decode())


if __name__ == '__main__':
    client()

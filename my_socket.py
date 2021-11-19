import socket
import random
QUEUE_SIZE = 5
something = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."]


def server():
    serv = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM)
    serv.bind(('', 5000))
    serv.listen(QUEUE_SIZE)

    # always listen for connections
    while True:
        conn, addr = serv.accept()
        print(f'Cntn: {addr}')
        from_client = ''
        while True:
            data = conn.recv(4096)
            response = random.choice(something)
            # end of data
            if not data:
                break

            from_client += data.decode()
            print(from_client)
            conn.send(
                response.encode())

            conn.close()
            print('client disconnected')


if __name__ == '__main__':
    server()

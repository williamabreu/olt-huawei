import paramiko
import time
import signal
import rtt


class SSH_Client:
    __BUFFER_SIZE = 2048

    def __init__(self, host, port, login, password):
        self.__host = host
        self.__port = port
        self.__login = login
        self.__passwd = password
        self.__rtt = rtt.RTT(host)
        self.__ssh = paramiko.SSHClient()
        self.__shell = None

        self.__configure_alarm()

    def __configure_alarm(self):
        def handler(signum, frame):
            raise TimeoutError('Timeout expired')

        signal.signal(signal.SIGALRM, handler)

    def connect(self):
        self.__ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.__ssh.connect(self.__host, port=self.__port, username=self.__login,
                           password=self.__passwd, look_for_keys=False, allow_agent=False)
        self.__shell = self.__ssh.invoke_shell()
        self.__rtt.start()

    def disconnect(self):
        self.__ssh.close()
        self.__rtt.stop()

    def recv(self, timeout):
        signal.alarm(timeout)
        response = self.__shell.recv(SSH_Client.__BUFFER_SIZE)
        signal.alarm(0) # desliga alarme
        return response.decode('utf-8')

    def exec(self, cmd):
        self.__shell.send(cmd + '\r\n')
        time.sleep(self.__rtt.get_estimation() + 0.2)
        response = self.__shell.recv(SSH_Client.__BUFFER_SIZE)
        return response.decode('utf-8')

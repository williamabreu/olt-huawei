import paramiko, time

paramiko.util.log_to_file('syslogin.log')

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.10.16.38', port=22, username='root', password='admin123', look_for_keys=False, allow_agent=False)

shell = ssh.invoke_shell()

time.sleep(0.5)

response = shell.recv(2048)
print(response.decode('utf-8'))

cmd = input('input> ')

while cmd != 'quit':
    shell.send(cmd + '\r\n')
    time.sleep(0.5)
    response = shell.recv(2048)
    print(response.decode('utf-8'))
    cmd = input('input> ')

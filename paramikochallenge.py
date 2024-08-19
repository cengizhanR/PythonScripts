# #Challange1
# import paramiko
# import time
#
# # creating an ssh client object
# ssh_client = paramiko.SSHClient()
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
# print('Connecting to 192.168.56.2')
# ssh_client.connect(hostname= '192.168.56.2', port= 22, username= 'ubuntunode01', password= '123',
#                            look_for_keys=False, allow_agent=False)
#
#
# shell = ssh_client.invoke_shell()
# shell.send('show users\n')
# time.sleep(1)
#
# output = shell.recv(100000).decode()
# print(output)
#
#
# if ssh_client.get_transport().is_active():
#     print('Closing connection')
#     ssh_client.close()
#
# #Challange2
# import paramiko
# import getpass
# import time
#
# # creating an ssh client object
# ssh_client = paramiko.SSHClient()
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
# print('Connecting to 192.168.56.2')
# ssh_client.connect(hostname= '192.168.56.2', port= 22, username= 'ubuntunode01', password= '123',
#                            look_for_keys=False, allow_agent=False)
#
#
# shell = ssh_client.invoke_shell()
# shell.send('show users\n')
# time.sleep(1)
#
# output = shell.recv(100000).decode()
# print(output)
#
#
# if ssh_client.get_transport().is_active():
#     print('Closing connection')
#     ssh_client.close()
#
#

# #Challange3
# import paramiko
# import time
#
# # creating an ssh client object
# ssh_client = paramiko.SSHClient()
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
# print('Connecting to 192.168.56.2')
# ssh_client.connect(hostname= '192.168.56.2', port= 22, username= 'ubuntunode01', password= '123',
#                            look_for_keys=False, allow_agent=False)
#
#
# shell = ssh_client.invoke_shell()
# shell.send('show users\n')
# time.sleep(1)
#
# output = shell.recv(100000).decode()
#
# with open('file_name.txt', 'w') as f:
#     f.write(output)
#
# if ssh_client.get_transport().is_active():
#     print('Closing connection')
#     ssh_client.close()

# #Challange4
# import paramiko
# import time
#
# # creating an ssh client object
# ssh_client = paramiko.SSHClient()
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
# print('Connecting to 192.168.56.2')
# linux = {'hostname': '192.168.56.2', 'port': '22', 'username': 'ubuntunode01', 'password': '123','look_for_keys':False, 'allow_agent':False}
# ssh_client.connect(**linux)
#
#
# shell = ssh_client.invoke_shell()
# shell.send('show users\n')
# time.sleep(1)
#
# output = shell.recv(100000).decode()
#
# with open('file_name.txt', 'w') as f:
#     f.write(output)
#
# if ssh_client.get_transport().is_active():
#     print('Closing connection')
#     ssh_client.close()
#
# #Challange5
# import paramiko
# import time
#
# # creating an ssh client object
# ssh_client = paramiko.SSHClient()
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
# print('Connecting to 10.1.1.10')
# ssh_client.connect(hostname='10.1.1.10', port='22', username='u1', password='cisco',
#                    look_for_keys=False, allow_agent=False)
#
#
# shell = ssh_client.invoke_shell()
# shell.send('enable\n')
# shell.send('cisco\n')
# shell.send('terminal length 0\n')
# shell.send('show running-config\n')
# time.sleep(1)
#
# output = shell.recv(100000).decode()
#
#
# with open('running-config.txt', 'w') as f:
#     f.write(output)
#
#
# if ssh_client.get_transport().is_active():
#     print('Closing connection')
#     ssh_client.close()

# #Challange6
# import paramiko
# import time
#
# # creating an ssh client object
# ssh_client = paramiko.SSHClient()
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
# print('Connecting to 10.1.1.10')
# ssh_client.connect(hostname='10.1.1.10', port='22', username='u1', password='cisco',
#                    look_for_keys=False, allow_agent=False)
#
#
# shell = ssh_client.invoke_shell()
#
# shell.send('terminal length 0\n') ## needed to display the entire output at once
# shell.send('show ip int brief\n')
# time.sleep(1)
#
# output = shell.recv(100000).decode()
# print(output)
#
#
# if ssh_client.get_transport().is_active():
#     print('Closing connection')
#     ssh_client.close()
# #Challange7
# import paramiko
# import time
#
# # creating an ssh client object
# ssh_client = paramiko.SSHClient()
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
# print('Connecting to 10.1.1.10')
# ssh_client.connect(hostname='10.1.1.10', port='22', username='u1', password='cisco',
#                    look_for_keys=False, allow_agent=False)
#
#
# shell = ssh_client.invoke_shell()
# shell.send('terminal length 0\n')
# shell.send('show ip int brief\n')
# time.sleep(1)
#
# output = shell.recv(100000)
# # decoding from bytes to string
# output = output.decode()
# print(output)
#
#
# if ssh_client.get_transport().is_active():
#     print('Closing connection')
#     ssh_client.close()

# #Challange8
# import paramiko
# import time
#
# # creating an ssh client object
# ssh_client = paramiko.SSHClient()
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
# print('Connecting to 10.1.1.10')
# ssh_client.connect(hostname='10.1.1.10', port='22', username='u1', password='cisco',
#                    look_for_keys=False, allow_agent=False)
#
#
# shell = ssh_client.invoke_shell()
# shell.send('terminal length 0\n')
# shell.send('show ip int brief\n')
# time.sleep(1)
#
# output = shell.recv(100000)
# # decoding from bytes to string
# output = output.decode()
# print(output)
#
#
# if ssh_client.get_transport().is_active():
#     print('Closing connection')
#     ssh_client.close()

#Challange9
# import paramiko
# import time
#
# # creating an ssh client object
# ssh_client = paramiko.SSHClient()
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
# print('Connecting to 10.1.1.10')
# ssh_client.connect(hostname='10.1.1.10', port='22', username='u1', password='cisco',
#                    look_for_keys=False, allow_agent=False)
#
#
# shell = ssh_client.invoke_shell()
#
# # the second element (cisco) is the enable command
# commands = ['enable', 'cisco', 'conf t', 'username admin1 secret cisco', 'access-list 1 permit any', 'end',
#             'terminal length 0',  'sh run | i user']
#
#
# for cmd in commands:
#     print(f'Sending command: {cmd}')
#     shell.send(f'{cmd}\n')
#     time.sleep(0.5)
#
# output = shell.recv(100000)
# # decoding from bytes to string
# output = output.decode()
# print(output)
#
#
# if ssh_client.get_transport().is_active():
#     print('Closing connection')
#     ssh_client.close()
# #Challange10
# import paramiko
# import time
#
# # creating an ssh client object
# ssh_client = paramiko.SSHClient()
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
# print('Connecting to 192.168.56.2')
# linux = {'hostname': '192.168.56.2', 'port': '22', 'username': 'ubuntunode01', 'password': '123','look_for_keys':False, 'allow_agent':False}
# ssh_client.connect(**linux)
# with open('file_name.txt', 'r') as f:
#     content = f.read().splitlines()
#
# shell = ssh_client.invoke_shell()
# for cmd in content:
#     print(f'Sending command: {cmd}')
#     shell.send(f'{cmd}\n')
#     time.sleep(0.5)
#
# output = shell.recv(100000).decode()
#
# print(output)
#
# if ssh_client.get_transport().is_active():
#     print('Closing connection')
#     ssh_client.close()
#Challange11
#inside myparamiko
#Challange12
#inside myparamiko
#Challange13
#inside myparamiko
#Challange14
# import paramiko
# import time
# import threading
# def execute_command(device, command):
#
#     # creating an ssh client object
#     ssh_client = paramiko.SSHClient()
#     ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
#
#     print(f'Connecting to {device["hostname"]}')
#     ssh_client.connect(**device)
#
#
#     shell = ssh_client.invoke_shell()
#     print(f'\nSending command "{command}" to "{device["hostname"]}"')
#     shell.send('term length 0\n')
#     shell.send(f'{command}\n')
#     time.sleep(1)
#
#     output = shell.recv(100000).decode()
#     print(output)
#
#
#     if ssh_client.get_transport().is_active():
#         print('Closing connection')
#         ssh_client.close()
#
#
# if __name__ == '__main__':
#     router1 = {'hostname': '10.1.1.10', 'port': '22', 'username': 'u1', 'password': 'cisco',
#                   'look_for_keys': False, 'allow_agent': False}
#     router2 = {'hostname': '10.1.1.20', 'port': '22', 'username': 'u1', 'password': 'cisco',
#                   'look_for_keys': False, 'allow_agent': False}
#     router3 = {'hostname': '10.1.1.30', 'port': '22', 'username': 'u1', 'password': 'cisco',
#                   'look_for_keys': False, 'allow_agent': False}
#
#     routers = [router1, router2, router3]
#
#     for device in routers:
#         execute_command(device, 'show ip interface brief')

#Challange15
import paramiko
import time
import threading

def execute_command(device, command):

    # creating an ssh client object
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


    print(f'Connecting to {device["hostname"]}')
    ssh_client.connect(**device)


    shell = ssh_client.invoke_shell()
    print(f'Sending command "{command}" to "{device["hostname"]}"')
    shell.send('term length 0\n')
    shell.send(f'{command}\n')
    time.sleep(1)

    output = shell.recv(100000).decode()
    print(output)


    if ssh_client.get_transport().is_active():
        print('Closing connection')
        ssh_client.close()


if __name__ == '__main__':
    router1 = {'hostname': '10.1.1.10', 'port': '22', 'username': 'u1', 'password': 'cisco',
                  'look_for_keys': False, 'allow_agent': False}
    router2 = {'hostname': '10.1.1.20', 'port': '22', 'username': 'u1', 'password': 'cisco',
                  'look_for_keys': False, 'allow_agent': False}
    router3 = {'hostname': '10.1.1.30', 'port': '22', 'username': 'u1', 'password': 'cisco',
                  'look_for_keys': False, 'allow_agent': False}

    routers = [router1, router2, router3]


    threads = list()
    for device in routers:
        th = threading.Thread(target=execute_command, args=(device, 'show ip interface brief'))
        threads.append(th)

    for th in threads:
        th.start()


    for th in threads:
        th.join()

#Challange16
#inside myparamiko
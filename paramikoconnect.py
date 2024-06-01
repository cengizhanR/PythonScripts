import paramiko
import time
# creating an ssh client object
# ssh_client = paramiko.SSHClient()
# # print(type(ssh_client))
#
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# print('Connecting to 192.168.122.10')
# ssh_client.connect(hostname='192.168.122.10', port='22', username='u1', password='cisco',
#                    look_for_keys=False, allow_agent=False)
#
#
# # checking if the connection is active
# print(ssh_client.get_transport().is_active())
#
# # sending commands
# # ...
#
# print('Closing connection')
# ssh_client.close()

# ssh_client = paramiko.SSHClient()
# # print(type(ssh_client))
#
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
# router = {'hostname':'192.168.122.10', 'port':'22', 'username':'u1', 'password':'cisco'}
# print(f'Connecting to {router["hostname"]}')
# ssh_client.connect(**router,look_for_keys=False, allow_agent=False)
#
# shell = ssh_client.invoke_shell()
# shell.send('terminal length 0\n')
# shell.send('show version\n')
# shell.send('show ip int brief\n')
# time.sleep(1)
#
# output = shell.recv(10000)
# output=output.decode('utf-8')
# print(output)
# if ssh_client.get_transport().is_active() == True:
#     print('Closing connection')
#     ssh_client.close()

# ssh_client = paramiko.SSHClient()
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
# # creating a dictionary for each device to connect to
# router1 = {'hostname': '192.168.122.10', 'port': '22', 'username': 'u1', 'password': 'cisco'}
# router2 = {'hostname': '192.168.122.10', 'port': '22', 'username': 'u1', 'password': 'cisco'}
# router3 = {'hostname': '192.168.122.10', 'port': '22', 'username': 'u1', 'password': 'cisco'}
#
# # creating a list of dictionaries (of devices)
# routers = [router1, router2, router3]
#
# # iterating over the list (over the devices) and backup the config
# for router in routers:
#     print(f'Connecting to {router["hostname"]}')
#     ssh_client.connect(**router, look_for_keys=False, allow_agent=False)
#
#     shell = ssh_client.invoke_shell()
#
#     shell.send('enable\n')
#     shell.send('cisco\n')  # this is the enable password
#     shell.send('conf t\n')
#     shell.send('router ospf 1\n')
#     shell.send('net 0.0.0.0 0.0.0.0 area 0\n')
#     shell.send('end\n')
#     shell.send('terminal length 0\n')
#     shell.send('sh ip protocols\n')
#     time.sleep(2)
#
#     output = shell.recv(10000).decode()
#     print(output)
#
#     if ssh_client.get_transport().is_active() == True:
#         print('Closing connection...')
#         ssh_client.close()

# ssh_client = paramiko.SSHClient()
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
# # creating a dictionary for each device to connect to
# linux = {'hostname': '192.168.56.2', 'port': '22', 'username': 'ubuntunode01', 'password': '123'}
#
# print(f'Connecting to {linux["hostname"]}')
# ssh_client.connect(**linux, look_for_keys=False, allow_agent=False)
#
# stdin,stdout,stderr= ssh_client.exec_command('ifconfig\n')
# output=stdout.read()
# output=output.decode()
# print(output)
#
# stdin,stdout,stderr= ssh_client.exec_command('who\n')
# time.sleep(0.5)
# output=stdout.read()
# output=output.decode()
# print(output)
#
# stdin,stdout,stderr= ssh_client.exec_command('cat /etc/shadow\n')
# time.sleep(0.5)
# output=stdout.read()
# output=output.decode()
# print(output)
# print(stderr.read().decode())
# if ssh_client.get_transport().is_active() == True:
#     print('Closing connection...')
#     ssh_client.close()

# ssh_client = paramiko.SSHClient()
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
# # creating a dictionary for each device to connect to
# linux = {'hostname': '192.168.56.2', 'port': '22', 'username': 'ubuntunode01', 'password': '123'}
#
# print(f'Connecting to {linux["hostname"]}')
# ssh_client.connect(**linux, look_for_keys=False, allow_agent=False)
#
# stdin, stdout, stderr = ssh_client.exec_command('sudo useradd u3\n', get_pty=True)
#
# stdin.write('123\n')
# time.sleep(2)
# print(stderr.read().decode())
# stdin, stdout, stderr = ssh_client.exec_command('cat /etc/passwd\n')
# print(stdout.read().decode())
# time.sleep(1)
#
# if ssh_client.get_transport().is_active() == True:
#     print('Closing connection...')
#     ssh_client.close()
# import myparamiko
# router = {'server_ip': '192.168.56.2', 'server_port': '22', 'user': 'ubuntunode01', 'passwd': '123'}
# client= myparamiko.connect(**router)
# shell = myparamiko.get_shell(client)
# myparamiko.send_command(shell,'uname -a')
# cmd= 'sudo groupadd developers'
# myparamiko.send_command(shell,cmd)
# myparamiko.send_command(shell,'123',2)
# myparamiko.show(shell)
# myparamiko.send_command(shell,'tail -n 1 /etc/group')
# output=myparamiko.show(shell)
# print(output)
# myparamiko.close(client)

# import myparamiko # myparamiko.py should be in the same directory with this script (or in sys.path)
#
# router = {'server_ip':'192.168.122.10', 'server_port': '22', 'user': 'u1', 'passwd': 'cisco'}
# client = myparamiko.connect(**router)
# shell = myparamiko.get_shell(client)
#
# myparamiko.send_command(shell, 'terminal length 0')
# myparamiko.send_command(shell, 'enable')
# myparamiko.send_command(shell, 'cisco')  # this is the enable command
# myparamiko.send_command(shell, 'show run')
#
# output = myparamiko.show(shell)
# # processing the output
# # print(output)
# output_list = output.splitlines()
# output_list = output_list[9:-1]
# output = '\n'.join(output_list)
# # print(output)
#
# from datetime import datetime
# now=datetime.now()
# year = now.year
# month = now.month
# day = now.day
# hour = now.hour
# minute = now.minute
# file_name = f'{router["server_ip"]}_{year}_{month}_{day}.txt'
# print(file_name)
# with open(file_name, 'w') as f:
#     f.write(output)
#
# myparamiko.close(client)

# import myparamiko  # myparamiko.py should be in the same directory with this script (or in sys.path)
#
# router1 = {'server_ip': '192.168.122.10', 'server_port': '22', 'user': 'u1', 'passwd': 'cisco'}
# router2 = {'server_ip': '192.168.122.30', 'server_port': '22', 'user': 'u1', 'passwd': 'cisco'}
# router3 = {'server_ip': '192.168.122.20', 'server_port': '22', 'user': 'u1', 'passwd': 'cisco'}
#
# routers = [router1, router2, router3]
# for router in routers:
#     client = myparamiko.connect(**router)
#     shell = myparamiko.get_shell(client)
#
#     myparamiko.send_command(shell, 'terminal length 0')
#     myparamiko.send_command(shell, 'enable')
#     myparamiko.send_command(shell, 'cisco')  # this is the enable command
#     myparamiko.send_command(shell, 'show run')
#
#     output = myparamiko.show(shell)
#     # processing the output
#     # print(output)
#     output_list = output.splitlines()
#     output_list = output_list[9:-1]
#     output = '\n'.join(output_list)
#     # print(output)
#
#     from datetime import datetime
#
#     now = datetime.now()
#     year = now.year
#     month = now.month
#     day = now.day
#     hour = now.hour
#     minute = now.minute
#     file_name = f'{router["server_ip"]}_{year}_{month}_{day}.txt'
#     print(file_name)
#     with open(file_name, 'w') as f:
#         f.write(output)
#
#     myparamiko.close(client)

# import myparamiko # myparamiko.py should be in the same directory with this script (or in sys.path)
# import threading
# def backup(router):
#     client = myparamiko.connect(**router)
#     shell = myparamiko.get_shell(client)
#
#     myparamiko.send_command(shell, 'terminal length 0')
#     myparamiko.send_command(shell, 'enable')
#     myparamiko.send_command(shell, 'cisco')  # this is the enable command
#     myparamiko.send_command(shell, 'show run')
#
#     output = myparamiko.show(shell)
#     # processing the output
#     # print(output)
#     output_list = output.splitlines()
#     output_list = output_list[9:-1]
#     output = '\n'.join(output_list)
#     # print(output)
#
#     from datetime import datetime
#     now=datetime.now()
#     year = now.year
#     month = now.month
#     day = now.day
#     hour = now.hour
#     minute = now.minute
#     file_name = f'{router["server_ip"]}_{year}_{month}_{day}.txt'
#     print(file_name)
#     with open(file_name, 'w') as f:
#         f.write(output)
#
#     myparamiko.close(client)
# router1 = {'server_ip':'192.168.122.10', 'server_port': '22', 'user': 'u1', 'passwd': 'cisco'}
# router2 = {'server_ip':'192.168.122.30', 'server_port': '22', 'user': 'u1', 'passwd': 'cisco'}
# router3 = {'server_ip':'192.168.122.20', 'server_port': '22', 'user': 'u1', 'passwd': 'cisco'}
#
# routers = [router1,router2,router3]
# threads= list()
# for router in routers:
#     th=threading.Thread(target=backup,args=(router,))
#     threads.append(th)
#
# for th in threads:
#     th.start()
# for th in threads:
#     th.join()
# print(threads)
import myparamiko
import getpass

username = input('Username:')
password = getpass.getpass()

ssh_client=myparamiko.connect('192.168.56.2', '22',  username,  password)
remote_connection=myparamiko.get_shell(ssh_client)

newuser=input('Enter the user you want to create')
command = 'sudo useradd -m -d /home/' + newuser + ' -s /bin/bash ' + newuser
myparamiko.send_command(remote_connection,command)
myparamiko.send_command(remote_connection,password)
print('A user has been created')

answer=input('Display the users ! <y|n>')
if answer=='y':
    users = myparamiko.send_command(remote_connection,'cat /etc/passwd')
    print(users.decode())
myparamiko.close(ssh_client)

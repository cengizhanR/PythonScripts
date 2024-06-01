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

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# creating a dictionary for each device to connect to
linux = {'hostname': '192.168.56.2', 'port': '22', 'username': 'ubuntunode01', 'password': '123'}

print(f'Connecting to {linux["hostname"]}')
ssh_client.connect(**linux, look_for_keys=False, allow_agent=False)

stdin, stdout, stderr = ssh_client.exec_command('sudo useradd u3\n', get_pty=True)

stdin.write('123\n')
time.sleep(2)
print(stderr.read().decode())
stdin, stdout, stderr = ssh_client.exec_command('cat /etc/passwd\n')
print(stdout.read().decode())
time.sleep(1)

if ssh_client.get_transport().is_active() == True:
    print('Closing connection...')
    ssh_client.close()

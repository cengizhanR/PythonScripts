# from netmiko import Netmiko
# connection = Netmiko(host='192.168.56.2',port='22', username='ubuntunode01',password='123',device_type='linux')
from netmiko import ConnectHandler
# creating a dictionary for the device to connect to
# cisco_device = {
#        'device_type': 'linux',     #device type from https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py
#        'host': '192.168.56.2',
#        'username': 'ubuntunode01',
#        'password': '123',
#        'port': 22,
#        'secret': '123',     # optional, default 22
#        'verbose': True  # optional, default False
#        }
# connection=ConnectHandler(**cisco_device)
# prompt=connection.find_prompt()
# print(prompt)
# if '$' in prompt:
#        connection.enable()
# prompt=connection.find_prompt()
# print(prompt)
# print(connection.check_config_mode())
# if not connection.check_config_mode():
#        connection.check_config_mode()
# print(connection.check_config_mode())
# connection.send_command('username u4 secret cisco')
# output=connection.send_command('cat /etc/shadow')
# print(output)
# print('Closing connection')
# connection.disconnect()


# from netmiko import ConnectHandler
# cisco_device = {
#        'device_type': 'cisco_ios',
#        'host': '192.168.122.10',
#        'username': 'u1',
#        'password': 'cisco',
#        'port': 22,             # optional, default 22
#        'secret': 'cisco',      # this is the enable password
#        'verbose': True         # optional, default False
#        }
# connection = ConnectHandler(**cisco_device)
# print('Entering the enable mode...')
# connection.enable()
#
# # this method receives a list of commands to send to the device
# # in enters automatically into global config mode and exists automatically at the end
# # commands = ['int loopback 0', 'ip address 1.1.1.1 255.255.255.255', 'exit', 'username netmiko secret cisco']
# cmd = 'ip ssh version 2;access-list 1 permit any;ip domain-name network-automation.io'
# # cmd= '''ip ssh version 2
# # access-list 1 permit any
# # ip domain-name network-automation.io
# # '''
# # output = connection.send_config_set(cmd.split('\n'))
# output = connection.send_config_set(cmd.split(';'))
# print(connection.find_prompt())
# connection.send_command('write memory')
# print(output)
# print('CLosing Connection')
# connection.disconnect()
# cisco_device = {
#        'device_type': 'cisco_ios',
#        'host': '192.168.122.10',
#        'username': 'u1',
#        'password': 'cisco',
#        'port': 22,             # optional, default 22
#        'secret': 'cisco',      # this is the enable password
#        'verbose': True         # optional, default False
#        }
# connection = ConnectHandler(**cisco_device)
# print('Entering the enable mode...')
# connection.enable()
#
# print('Sendin command command from file')
# output=connection.send_config_from_file('ospf.txt')
# print(output)
# print('CLosing Connection')
# connection.disconnect()

# with open('devices.txt') as f:
#        devices=f.read().splitlines()
#
# device_list=list()
# for ip in devices:
#        cisco_device = {
#               'device_type': 'cisco_ios',
#               'host': ip,
#               'username': 'u1',
#               'password': 'cisco',
#               'port': 22,             # optional, default 22
#               'secret': 'cisco',      # this is the enable password
#               'verbose': True         # optional, default False
#               }
#        device_list.append(cisco_device)
#        # print(device_list)
#
# print(device_list)
# # exit(1)
# for device in device_list:
#     connection = ConnectHandler(**device)
#
#     print('Entering the enable mode ...')
#     connection.enable()
#
#     # prompting the user for a config file
#     file = input(f'Enter a configuration file (use a valid path) for {device["host"]}:')
#
#     print(f'Running commands from file: {file} on device: {device["host"]}')
#     output = connection.send_config_from_file(file)
#     print(output)
#
#     print(f'Closing connection to {cisco_device["host"]}')
#     connection.disconnect()
#
#     print('#' * 30)
# import time
# start= time.time()
# with open('devices.txt') as f:
#        devices=f.read().splitlines()
#
# for ip in devices:
#        cisco_device = {
#               'device_type': 'cisco_ios',
#               'host': ip,
#               'username': 'u1',
#               'password': 'cisco',
#               'port': 22,             # optional, default 22
#               'secret': 'cisco',      # this is the enable password
#               'verbose': True         # optional, default False
#               }
#        connection = ConnectHandler(**cisco_device)
#        print('Entering the enable mode...')
#        connection.enable()
#        output = connection.send_command('show run')
#        # print(output)
#        prompt = connection.find_prompt()
#        # print(prompt)
#        hostname = prompt[0:-1]
#        # print(hostname)
#        from datetime import datetime
#
#        now = datetime.now()
#        year = now.year
#        month = now.month
#        day = now.day
#
#
#        filename = f'{hostname}_{year}-{month}-{day}-backup.txt'
#        with open(filename, 'w') as backup:
#               backup.write(output)
#               print(f'Backup of {hostname} is succesfull')
#               print('*'*30)
#        print('CLosing Connection')
#        connection.disconnect()
#
# end=time.time()
# print(f'Total time {end-start}')
import time
import threading
start = time.time()

def backup(device):
       connection = ConnectHandler(**device)
       print('Entering the enable mode...')
       connection.enable()
       output = connection.send_command('show run')
       # print(output)
       prompt = connection.find_prompt()
       # print(prompt)
       hostname = prompt[0:-1]
       # print(hostname)
       from datetime import datetime

       now = datetime.now()
       year = now.year
       month = now.month
       day = now.day

       filename = f'{hostname}_{year}-{month}-{day}-backup.txt'
       with open(filename, 'w') as backup:
              backup.write(output)
              print(f'Backup of {hostname} is succesfull')
              print('*' * 30)
       print('CLosing Connection')
       connection.disconnect()

with open('devices.txt') as f:
       devices=f.read().splitlines()
threads = list()
for ip in devices:
       device = {
              'device_type': 'cisco_ios',
              'host': ip,
              'username': 'u1',
              'password': 'cisco',
              'port': 22,             # optional, default 22
              'secret': 'cisco',      # this is the enable password
              'verbose': True         # optional, default False
              }
       th = threading.Thread(target=backup, args=(device,))
       threads.append(th)

for th in threads:
       th.start()

for th in threads:
       th.join()

end=time.time()
print(f'Total time {end-start}')
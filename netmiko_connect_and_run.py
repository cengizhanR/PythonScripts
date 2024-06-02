# from netmiko import Netmiko
# connection = Netmiko(host='192.168.56.2',port='22', username='ubuntunode01',password='123',device_type='linux')
from netmiko import ConnectHandler
# creating a dictionary for the device to connect to
cisco_device = {
       'device_type': 'linux',     #device type from https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py
       'host': '192.168.56.2',
       'username': 'ubuntunode01',
       'password': '123',
       'port': 22,
       'secret': '123',     # optional, default 22
       'verbose': True  # optional, default False
       }
connection=ConnectHandler(**cisco_device)
prompt=connection.find_prompt()
print(prompt)
connection.enable()
output=connection.send_command('cat /etc/shadow')
print(output)
print('Closing connection')
connection.disconnect()
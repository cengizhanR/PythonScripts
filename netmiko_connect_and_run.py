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
if '$' in prompt:
       connection.enable()
prompt=connection.find_prompt()
print(prompt)
if not connection.check_config_mode():
       connection.check_config_mode()
print(connection.check_config_mode())
connection.send_command('username u4 secret cisco')
output=connection.send_command('cat /etc/shadow')
print(output)
print('Closing connection')
connection.disconnect()
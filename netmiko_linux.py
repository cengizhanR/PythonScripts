from netmiko import ConnectHandler
# # http://ktbyers.github.io/netmiko/COMMON_ISSUES.html
# import logging
# logging.basicConfig(filename='test.log', level=logging.DEBUG)
# logger = logging.getLogger("netmiko")
#
# linux = {
#     'device_type': 'linux',
#     'host': '192.168.56.2',
#     'username': 'ubuntunode01',
#     'password': '123',
#     'port': 22,  # optional, default 22
#     'secret': '123',  # sudo passwd
#     'verbose': True  # optional, default False
# }
# connection = ConnectHandler(**linux)
#
# connection.enable() #sudo su
#
# output = connection.send_command('apt update && apt install -y apache2', read_timeout=60)
# print(output)
# print('CLosing Connection')
# connection.disconnect()

from netmiko import file_transfer

linux = {
    'device_type': 'linux',
    'host': '192.168.56.2',
    'username': 'ubuntunode01',
    'password': '123',
    'port': 22,  # optional, default 22
    'secret': '123',  # sudo passwd
    'verbose': True  # optional, default False
}
connection = ConnectHandler(**linux)

# Transfer file to the remote server
transfer_output = file_transfer(
    connection,
    source_file='test.log',
    dest_file='test.log',
    file_system='/home/ubuntunode01/',  # Ensure this is the correct destination directory
    direction='put',
    overwrite_file=True
)

print(transfer_output)
print('Closing Connection')
connection.disconnect()
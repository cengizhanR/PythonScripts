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

ssh_client = paramiko.SSHClient()
# print(type(ssh_client))

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

router = {'hostname':'192.168.122.10', 'port':'22', 'username':'u1', 'password':'cisco'}
print(f'Connecting to {router["hostname"]}')
ssh_client.connect(**router,look_for_keys=False, allow_agent=False)

shell = ssh_client.invoke_shell()
shell.send('terminal length 0\n')
shell.send('show version\n')
shell.send('show ip int brief\n')
time.sleep(1)

output = shell.recv(10000)
output=output.decode('utf-8')
print(output)
if ssh_client.get_transport().is_active() == True:
    print('Closing connection')
    ssh_client.close()
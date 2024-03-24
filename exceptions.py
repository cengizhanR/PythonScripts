# import  os
# all_files = os.listdir("C:/Users/cengi/OneDrive/Masaüstü/")
# print(all_files)
# txt_files = filter(lambda x: x[-4:] == 'a.txt', all_files)
# print(txt_files)
# open(txt_files[0])
# with open ('a.txt') as f:
#     print(f.read())
# try:
#     a=int(input(f'Emter a: '))
#     b=int(input('Enter b: '))
#     c=a/b
#     print(c)
# except:
#     print('An exeption occured')
# else:
#     print('No Errors')
#     print(f'c = {c}')
# finally:
#     print('Good bye!')
# x=10
# print(x**x)
# f=open('a.txt', 'w')
# try:
#     f.write('wrte somethin to file.')
# except:
#     print('Connot write to file')
# else:
#     print('File was written successfully!')
# finally:
#     print('This code is always executed!')
#     if not f.closed:
#         f.close()
#     print(f'File closed: {f.closed}')
#
# print('Some other code')
###TEST YOUR NETWORK CONNECTION
import subprocess
# command='ping -n 1 8.8.8.8'
# output=subprocess.check_output(command.split())
# print(output.decode())
with open('host.txt') as f:
    id_addresses = f.read().splitlines()
    print(id_addresses)
    for ip in id_addresses:
        try:
            command = f'ping -n 1 {ip}'
            output = subprocess.check_output(command.split())
            print(output.decode())
        except Exception as e:
            print(f'Host {ip} is down!!! => {e}')
        print('#'*50)
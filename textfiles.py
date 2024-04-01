#Opening and reading files

# f= open('configuration.txt','rt') #r read file t text b binary write b instead of t
# content = f.read()
# print(content)
# print(f.closed)
# f.close()
# print(f.closed)
# f= open('C:\\Users\\cengi\\PycharmProjects\\pythonScripts\\pythonProject3\\settings.txt')
# #raw string
# f=open(r'C:\Users\cengi\PycharmProjects\pythonScripts\pythonProject3\settings.txt')
# f=open('configuration.txt')
# content = f.read(5)
# print(content)
# content= f.read(3)
# print(content)
#
# print(f.tell())
# f.seek(2)
# content = f.read(3)
# print(content)
#
# f.seek(0)
# content=f.read(3)
# print(content)
# f=open('configuration.txt')
# print(f.read())
# print('#'*50)
# f.seek(0)
# print(f.read())
# with open('configuration.txt') as file:
#     content = file.read()
#     print(content)
#     print(file.closed)
#
# print(file.closed)
# file.read()
#Reading files into a list
#1 f.read().splitlines()
# with open('configuration.txt') as f:
#     content = f.read().splitlines()
#     print(content)
# print('#'*50)
# with open('configuration.txt') as f:
#     content=f.readlines()
#     print(content)
# print('#'*50)
# with open('configuration.txt') as f:
#     content=f.readline()
#     print(content, end='')
#     print(f.readline())
# print('#'*50)
# with open('configuration.txt') as f:
#     content=list(f)
#     print(content)
#
# print('#'*50)
# with open('configuration.txt') as f:
#     for line in f:
#         print(line,end='')
#WRITING TO TEXT
# with open('myfile.txt', 'w') as f:
#     f.write('Just a line.\n')
#     f.write('Just a  2nd line.\n')
#
# with open('myfile.txt', 'a') as f:
#     f.write('Some text here.\n')
#     f.write('Another text.\n')
#
# with open('myfile.txt', 'r+') as f:
#     f.seek(5)
#     f.write('100')
#     f.write('line added with r+.\n')
#     f.seek(10)
#     print(f.read())
with open('devices.txt') as f:
    content=f.read().splitlines()
    #print(content)
    devices = list()
    for line in content[1:]:
        devices.append(line.split(':'))

    print(devices)

    for device in devices:
        print(f'pinging {device[1]}')
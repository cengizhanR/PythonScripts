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

import csv
# with open('airtravel.csv', 'r') as f:
#     reader = csv.reader(f)
#     next(reader) # it wil skipt he first line
#     year_1958 = dict()
#     for row in  reader:
#         year_1958[row[0]]= row[1]
#
#     print(year_1958)
#     max_1958 = max(year_1958.values())
#     print(max_1958)
#     for k, v in year_1958.items():
#         if max_1958 == v:
#             print(f'Busiest Month in 1958: {k}, Flights:{v.strip()}')

# with open('people.csv', 'a') as csvfile:
#     writer = csv.writer(csvfile)
#     csvdata = (5, 'Anne', 'Amsterdam')
#     writer.writerow(csvdata)

# with open('numbers.csv','w',newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(['x','x**2','x**3','x**4'])
#     for x in range(1,101):
#         writer.writerow([x,x**2,x**3,x**4])
# with open('passwd.csv', 'r') as f:
#     reader = csv.reader(f, delimiter=':', lineterminator='\n')
#     for row in reader:
#         print(row)
# csv.register_dialect('hashes', delimiter='#', quoting=csv.QUOTE_NONE, lineterminator='\n')
# with open('items.csv','r') as csvfile:
#     reader= csv.reader(csvfile, dialect='hashes')
#     for row in reader:
#         print(row)
#
# with open('items.csv','a') as csvfile:
#     writer = csv.writer(csvfile, dialect='hashes')
#     writer.writerow(('anan', 111,3.3))
# with open ('devices.txt', 'r') as f:
#      content= f.read().splitlines()
#      dedi=list()
#      # print(content)
#      for line in content:
#          dedi.append(line.split(':'))
#
#
# print(dedi)
#second way
# with open('devices.txt') as f:
#     rader = csv.reader(f, delimiter=':')
#     mylist=list()
#     for row in rader:
#         mylist.append(row)
# print(mylist)

# with open('macs.txt') as f:
#     content = f.read().split()
#     print(content)
#     content = list(set(content))
#     print(content)
#
# with open('mac_uniqe.txt','w', newline='') as f:
#     for mac in content:
#         f.write(f'{mac}\n')

# with open('sample_file.txt') as f:
#     content=f.read().splitlines()
#     print(content)
#     my_str= '\n'.join(content)
#     print(my_str)
# with open('file.txt','r', newline='') as f:
#      context=f.readlines()
#      print(context)
#      tmp_list=list()
#      for line in context:
#          if line.strip() != '':
#              tmp_list.append(line)
# print(tmp_list)
#
# with open('fileWithout.txt', 'w') as f:
#     ali = f.write(''.join(tmp_list))
# import time
# def tail(txt,n):
#     with open(txt,'r') as f:
#         content = f.read().splitlines()
#         last = content[len(content)-n:]
#         print(last)
#         my_str='\n'.join(last)
#         return my_str
#
# while True:
#     t=tail('sample_file.txt',3)
#     print(t)
#     time.sleep(3)
#     print('')
# def wc(txt):
#     with open(txt,'r') as f:
#         content=f.read().splitlines()
#         print(content)
#         lines = len(content)
#         print(list(content[1]))
#         words=0
#         for line in content:
#             words += len(line.split())
#
#         chars=0
#         for line in content:
#             chars += len(list(line))
#
#
#         return  chars, lines, words
#
#
# print(wc('sample_file.txt'))
# with open('banking.txt', 'r') as f:
#     content = f.read().splitlines()
#     print(content)
#     deposit, withdrawal = 0,0
#
#     for item in content:
#       tmp=item.split(':')
#       print(tmp)
#       if tmp[0] == 'D':
#             deposit += int(tmp[1])
#       elif tmp[0] == 'W':
#           withdrawal +=int(tmp[1])
#       else:
#           print('File Format eror')
#
#     blance = deposit-withdrawal
#     print(blance)
# with open('american-english.txt', 'r') as f:
#     words= f.read().splitlines()
#     print(words)
#
#     words_and_length = dict()
#     for w in words:
#         words_and_length[w] = len(w)
#         print(w)
#     for k,v in words_and_length.items():
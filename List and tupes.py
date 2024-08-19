##PYTHON LISTS

# l1= [1, 2.5,'Python', True, ['abc', 'xyz'], (10,20,30)]
# print(len(l1))
# l2=[] #empty list
# l3 = list() #empty list
# print(l1[0])
# print(x := l1[-1])
# l4 = list('abcd')
# print(l4)
# l4[0]='X'
# l4.append(100)
# print(l4)
# l1=[3,4]
# print(l1, id(l1))
# l1=l1+[5,6]
# print(l1, id(l1))
# l1 += [7,8]
# print(l1, id(l1))
# l1.extend([11,12])
# print(l1, id(l1))
# #append vs extend
# l1.append(['a','b'])
# print(l1)
# l1.extend(['x','y'])
# print(l1)
# l1.append(20)
# l1.extend([20])
# print(l1)
# l2=list('abc')
# l3=l2*3
# print(l3)
####### list slicing
# numbers= [1,2,3,4,5]
# nums = numbers[1:4]
# print(f'{nums}')
# print(f'{numbers}')
######LIST COPY GOTCHAS
# l1= [1,2,3]
# l2=l1
# l2[0]='XX'
# l2.append(10)
# print(f'l2:{l2}')
# print(f'l1:{l1}')
# print(id(l1),id(l2))
# l1.remove(2)
# print(f'l2:{l2}')
# ## to create copy use copy method
# l3=l1.copy()
# l3.append('abc')
# print(f'l1 {l1}')
# print(f'l3 {l3}')
# print(id(l1),id(l3))
#2. lesson
# nums = [1,2,3,4,5,6,7,0,1,2]
# #This is wrong
# # for n in nums:
# #     if n <5:
# #         nums.remove(n)
# # print(nums)
# #This true
# new_list =list()
# for n in nums:
#     if n >=5:
#         new_list.append(n)
# print(new_list)
#
# my_list = [n for n in nums if n>=5]
# print(my_list)
# l1=list()
# print(dir(l1))
# help(l1.append)
#Addint to list append(),extend(), insert()
# l1=[1,2.2,'abc']
# l1.append(5)
# #l1.append(6,7) #Error
# l1.append([6,7])
# print(l1)
# #2.list.extend()
# l1.extend('xy')
# print(l1)
# #3. list.insert()
# years=[2020,2022,2023]
# years.insert(1,2021)
# years.insert(len(years),2024)
# print(years)
# years.insert(-1,2025) #3inserts on the second to last position
# print(years)
# #4 list.clear()
# years.clear()
# print(years) #removes all elements
# #5.list pop
# l2=[10,20,30,40]
# x=l2.pop()
# print(x)
# print(l2)
# y=l2.pop(1)
# print(y,l2)
# #6.list.remove
# l3=[10,20,10,40,20,10,20,20,'z']
# l3.remove(10)
# print(l3)
# while 20 in l3:
#     l3.remove(20)
# print(l3)
##7 . list.index()
# names=['john','dan','tom','john','bill']
# i=names.index('dan')
# print(f'dan is at index {i}')
# print(f'fafa   {names.index('john')}')
# #8 list.count()
# letter=list('adadadsaggadarhenefadada')
# n=letter.count('a')
# print(n)
# #9 list.reverse()
# l1=[1,3,'abc',10,'x']
# l1.reverse()
# print(f'l1: {l1}')
# #10. list.sort() and sorted(list)
# ages=[10,8,23,40,35]
# la=sorted(ages)
# print(la,ages)
# ages.sort()
# print(n:=ages.sort())
# print(ages)
# ages.sort(reverse=True)
# print(ages)
# #max and min
# l2=[-9,10,5,100,66]
# print(f'max: {max(l2)}')
# print(f'min: {min(l2)}')
# print(f'sum: {sum(l2)}')
#Split
# s1='I am lea:rning Pyth:on Prog:rammiLng!'
# l1=s1.split(':')
# print(l1)
#
# ip_list=['192.168.0.1','192.168.0.2', '192.168.0.3']
# ip_str=' '.join(ip_list)
# print(ip_str)
# ip_str=','.join(ip_list)
# print(ip_str)
# interface = '''wlo1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
#         inet 192.168.0.105  netmask 255.255.255.0  broadcast 192.168.0.255
#         inet6 fe80::6ec6:fea5:4a08:33ae  prefixlen 64  scopeid 0x20<link>
#         ether 14:13:33:ee:9c:1b  txqueuelen 1000  (Ethernet)
#         RX packets 1007942  bytes 902567350 (902.5 MB)
#         RX errors 0  dropped 0  overruns 0  frame 0
#         TX packets 531217  bytes 158518152 (158.5 MB)
#         TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0'''
#
# interface_list= interface.splitlines()
# print(interface_list)
# ip_mac=list()
# for line in interface_list[1:4]:
#     print(line)
#     tmp_list = line.split()
#     print(tmp_list)
#     ip_mac.append(tmp_list[1])
#
# print(ip_mac)
# ip_mac_str= ','.join(ip_mac)
# print(ip_mac_str)
#TUPLE OPERATIONS
# my_tuple=(1.4,10,'abc',True,(30,40),'x')
# t1=my_tuple + tuple('yz')
# print(t1)
# print(my_tuple[0:2])
# movies =('The wuzart', 'The Legend', 'Casablanca')
# for movie in movies:
#     print(f'watch {movie}')
#Tuple Methods
# t1=(1,2,1,3,4)
# #1. tuple.index()
# i=t1.index(2)
# print(f'2 is at position {i}')
# #2. tuple.count()
# n=t1.count(1)
# print(n)
# print(len(t1))
# print(sum(t1))
# print(max(t1))
# print(min(t1))
# t2=sorted(t1)
# print(t2)
# import sys
# l1 = [1,2,3,4,5,6]
# t1=(1,2,3,4,5,6)
# print(f'list memory size: {sys.getsizeof(l1)}')
# print(f'list memory size: {sys.getsizeof(t1)}')

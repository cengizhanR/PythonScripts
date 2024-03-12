# #PYTHON SETS
# s1={1,2,3,'a','b',4,1,2,'a',3,10}
# print(s1)
# #print(s1[0]) Error
# #SETS ARE MUTABLE
# s1.add((10,20))
# print(s1)
# s1.remove('a')
# print(s1)
# s2=set()
# s3={}
# print(type(s3),type(s2))
# #str => set
# s4=set('hellooooooo!!!')
# print(s4)
# #tuple => set
# s5=set((1,2,3,4,4,'abc'))
# print(s5)
# #list => set
# l2=[10,20,30,40]
# print(set(l2))
# macs=['10-3D-1C-FC-9D-D8','10-3D-1C-FC-9D-D8','10-3D-1C-FC-9D-90','10-3D-1C-FC-9D-D8','10-3D-1C-FC-9D-D8']
# mac_addresses = set(macs)
# print(mac_addresses)
# print(len(mac_addresses))
# print(list(mac_addresses))
# for item in s4:
#     print(item)
#
# print('x' in s4)
# set1={1,2,3}
# set2={2,3,1}
# print(set1 == set2)
# print(set1 is set2)
#SET METHODS
#1. set.add()
# s1={1,2,3}
# s1.add('a')
# s1.add(4.5)
# print(s1)
# #2. set.remove(item)
# s1.remove(3)
# #s1.remove(3) error
# print(s1)
# #3. set.discard(item)
# s1.discard('a')
# print(s1)
# s1.discard('x')  #not error
# #4.set.pop
# x=s1.pop()
# print(x,s1)
# s2=set('abc')
# s3=s2
# s3.add('x')
# print(s2)
# #5.set.clear()
# s3.clear()
# print(f's2: {s2}, s3:{s3}')
# #6 set.copy()
# s4=s1.copy()
# s4.add('z')
# print(f's4: {s4}, s1:{s1}')


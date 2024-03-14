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
#SET METHODS PART2
# set1={1,3,5,9}
# set2={5,7,9}
# #1. set.intersection()
# set3=set1.intersection(set2)
# print(set3)
# set3=set1 & set2
# print(set3)
# #2. set.difference()
# set4 = set1.difference(set2)
# print(f'set4: {set4}')
# set4= set1-set2
# print(f'set4: {set4}')
# set4=set1.difference([1,2,3,4,5])
# print(f'set4: {set4}')
# #3. set.symmetric_difference()
# set5=set1.symmetric_difference(set2)
# print(f'set5: {set5}')
# set5=set1 ^ set2
# print(f'set5: {set5}')
# #4 set.union()
# set6=set1.union(set2)
# print(f'set6: {set6}')
# set6=set1| set2
# print(f'set6: {set6}')
# #5 set.isdisjoint()
# s1={1,3,5}
# s2={5,6,7}
# print(s1.isdisjoint(s2))
# s3={8,9}
# print(s1.isdisjoint(s3))
# #<,<=,>,>=
# print({1,3}<{1,2,3,4})
#PYTHON FROZENSETS
fs1=frozenset({1,2,3,'a','b'})
print(fs1,type(fs1))
s1='Python is cool!!'
fs2=frozenset(s1)
print(fs2)
fs3=frozenset()
fs1=frozenset([1,2,3,4])
fs2=frozenset([3,4,5,6])
fs3=fs1.intersection(fs2)
print(fs3)
s1={4,10,20}
result1=s1.intersection(fs1)
result2=fs1-s1
print(f'result1 type: {type(result1)}') #set
print(f'result2 type: {type(result2)}') #frozenset
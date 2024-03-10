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
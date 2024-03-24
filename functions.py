#Python Functions

# def my_function():
#     print('Hello Python World!')
#     x=10
#     print(x ** x)
#
# my_function()

# def difference(a, b):
#     result = a - b
#     print(result)
#
# difference(1, 5)
#
# def func1(x, y, z):
#     print(f'first {x}')
#     print(f'second {y}')
#     print(f'third {z}')
#
# func1(y=7, x=3, z=9)

# def add(x, y=10):
#     print(f'x is {x} and y is {y}')
#     print(f'{x} + {y} = {x+y}')
#
# add(2,3)
# add(6)
# def add1(a, b):
#     print(f'Sum: {a+b}')
#
# def add2(a,b):
#     return a+b
#
# add1(10,20)
# my_sum=add2(5,2)
# print(my_sum)

# def my_func(x):
#     return x, x**2, x**3, x**4
#
# print(my_func(3))
# print(list(my_func(3)))
# a, b, c, d= my_func(10)
# print(a, b, c, d)
# x, *y=my_func(4)
# print(x,y)
# def average(a,b, *args):
#     return (a+b+sum(args))/(2+ len(args))
#
# print(average(4,5,6,7))
#
# def concatenate(*args):
#     result=''
#     for tmp in args:
#         result=result+tmp
#     return result
#
# r=concatenate('Python', '3', '!')
# print(r)
# result= concatenate('I','love','Python')
# print(result)
##**kwargs
# def my_function(**kwargs):
#     print(kwargs)
#     for k, v in kwargs.items():
#         print(f'k is {k} and v is {v}')
#
# my_function(name='John', age=40, location='London')
# person = {'name':'John', 'age':40, 'location':'London'}
# my_function(**person)
# def connect(ip,port,username,password):
#     print(ip,port,username,password)
#
# linux_server={'ip':'200.0.10.1','port':22, 'username':'admin','password':'ali'}
# connect(**linux_server)
# x=10
# def my_func():
#     global x
#     x +=1
#     print(f'x inside function {x}')
#
# my_func()
# print(f'outside function is {x}')

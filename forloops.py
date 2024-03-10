#FOR LOOPS

# for ada in 'Python':
#     print(ada)

# for ada in {1, 'a', 'b'}:
#     print(ada)
#     print('bye')
# print('22323')

# my_str = input('Enter Something: ')
# vowels = 'aeiou'
# for item in my_str:
#     if item in vowels:
#         print(item, end=' ')
# print('Hello Python!')
# x=101
# y = x // 2
# for n in [1, 2, 3, 4, 5, 6, 7]:
#     nn=n ** 2
#     if nn % 2 ==0:
#         print(f'{nn} is even.')
#     else:
#         print(f'{nn} is odd.')
# #RANGES
# r = range(2,10,3)
# print(type(r))
# print(list(r))
#LOOPS AND RANGES
# s=0
# for n in range(101):
#     s += n
#     print(f'Sum:{s}')
# for _ in range(10):
#     print('Do something',_)

# import random
# names= ['Diana', 'Pail', 'Ana', 'Dan', 'Victor', 'marry', 'Alexandra', 'Maria','Jeff', 'Bob', 'Bill', 'Angie']
# for _ in range(3):
#     print(f'Choosing winner. Round {_}...')
#     winner= random.choice(names)
#     names.remove(winner)
#     print(winner)
#     print('############')
###########################################################
##For, countine and pass Statements

# for letter in 'Go Python goooo!':
#     if letter == 'o':
#         continue
#     print(letter, end='')
#
# for n in range(10):
#     if n % 2 ==0:
#         print(f'Found an even number: {n}')
#         continue
#     print(f'Found an odd number: {n}')

# for n in range(10):
#     if n % 2 ==0:
#         pass
#         print(f'Found an even number: {n}')
#     print(f'Found an odd number: {n}')

# for number in range(10):
#     print(number)
#     if number == 5:
#         break
# exit() #stop entire scrips
# print('Ouside For')

# for letter in 'Python':
#     if letter == 'o':
#         print('letter is p and break')
#         break
#     print(letter)
# for n in range(1,12):
#     if n % 13 ==0:
#         print('Breaking')
# else:
#     print('There is no 13 ile bolunen')
# for l in 'abc':
#     print(l)
#     for n in range(3):
#         if n==1:
#             break
#         print(n)

#While loops
# x=0
# while x<10:
#     print(f'infineteloop {x}')
#     x+=1
# else:
#     print(f'Printing Fnisidadada')
#While And Continue
# x=12
# while x<100:
#     x=x+1
#     if x % 13 !=0: continue
#     print(x)

# while True:
#     guess = int(input('Enter Your lucky number: '))
#     if guess==7:
#         print(f'You win')
#         break
#     print(f'{guess} was not')
# a= int(input('Enter Number: '))
# while a >1:
#     b= a//2
#     while b>1:
#         if a %b ==0:
#             break
#         b -=1
#     else:
#         print(f'{a} is prime')
#     a -=1
##### THE WALRUS OPERATOR
# NAME := expression
# print(x := 2+3)
# print(f'x is {x}')
# value = input('Enter something: ')
# while value !='':
#     print(f'You Entered: {value}')
#     value = input('Enter something: ')

# while(value := input('Enter something: ')) !='':
#     print(f'You entered {value}')
# data = input('Enter Your Name: ')
# if len(data) > 0:
#     print(f'Your name has {len(data)} character')
# else:
#     print('Your Name cant not empty')
#
# if len(data := input('Enter your name: ')) >0:
#     print(f'Your name has  {len(data)} character')
# else:
#     print(f'Your name can not be emty')
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
for l in 'abc':
    print(l)
    for n in range(3):
        if n==1:
            break
        print(n)
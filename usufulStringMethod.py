my_str= 'I learn Python Programming.'
#1. str.upper()
print(my_str.upper())
#2.str.lower()
print(my_str.lower())
#3. str.strip()
ip = '        192.168.9.1'
ip=ip.strip()
print(ip)
value = '$$2000##'
print(value.strip('#$'))
#4. str.replace()
new_value=value.replace('$','@')
print(new_value)
#5. str.count()
txt='I learn Python, Python is cool!'
n=txt.lower().count('python')
print(n)
#6. str.split()
my_list=txt.split()
print(my_list)
print('1.2.3.4.5'.split('.'))
#7. str.join()
ip='10.1.2.3'
ip_list = ip.split('.')
print(ip_list)
ip_str='.'.join(ip_list)
print(ip_str)
#8 str.find()
my_str='I learn Python Programing.'
print(my_str.find('Python'))
#in
print('Python' in my_str)
print('Golang' in my_str)
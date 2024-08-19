#Identity Operators
a, b= 3,4
c=a is b
print(c)
# Immutable
print(id(a))
a += 3
print(id(a))
numbers = [1,2,3]
print(numbers)
numbers.append(100)
print(numbers)
nums = numbers.copy()
print(numbers == nums)
# INTRO TO STRING
print('Hi there\'m')
languages = """dadad
sdsds
sdss
sds
"""
print(languages)

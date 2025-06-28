def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b


str1 = input('Enter first string: ')
str2 = input('Enter second string: ')

str1, str2 = swap(str1, str2)
print('After swapping: ', str1, str2)

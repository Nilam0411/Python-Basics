# write a python program to check whether a given string is palindrome or not
str = input('enter a string:')
rev = str[::-1]
if str==rev and str.lower()==rev:
    print('the given string is palindrome')
else:
    print('the given string is not palindrome')
'''

# wap to check whether a triangle is isosceles, equilateral or scalene
print('enter all three sides of triangle:')
x = int(input('x:'))
y = int(input('y:'))
z = int(input('z:'))
if x==y==z:
    print('equilateral triangle')
elif x==y or y==z or z==x:
    print('isoscalene triangle')
else:
    print('scalene triangle')
'''
#wap to check validity of triangle
print('Enter all angles of the triangle:')
x = float(input('x:'))
y = float(input('y:'))
z = float(input('z:'))
if x+y+z==180:
    print('triangle is valid')
else:
    print('invalid triangle')

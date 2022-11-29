l = ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test', 'Ok']
e = 'Why'
try:
    i = l.index(e)
    print(f'First Index of element "{e}" in the list : ', i)
except ValueError as err:
    print(f'Element "{e}" not found in the list: ', err)
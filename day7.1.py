#pattern
'''
1 
2 2 
3 3 3 
4 4 4 4 
'''
for i in range(4):
    for j in range(i+1):
        print(i+1, end=' ')
    print()

print('.........................................')

'''
1 
1 2 
1 2 3 
1 2 3 4 
'''
for i in range(4):
    for j in range(i+1):
        print(j+1, end=' ')
    print()

print('.........................................')

'''
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5 
'''
n=5
for i in range(n):
    for j in range(n-i):
        print(i+1, end=' ')
    print()

print('.........................................')

'''
1 
2 3 
4 5 6 
7 8 9 10 
'''
n=1
for i in range(4):
    for j in range(i+1):
        print(n, end=' ')
        n=n+1
    print()

print('.........................................')

'''
5 5 5 5 5 
5 5 5 5 
5 5 5 
5 5 
5 
'''
n=5
for i in range(n):
    for j in range(n-i):
        print('5 ', end='')
    print()

print('.........................................')

'''
* 
* * 
* * * 
* * * * 
* * * * * 
'''
n=5
for i in range(n):
    for j in range(i+1):
        print('* ',end='')
    print()

print('.........................................')

'''
* * * * * 
* * * * 
* * * 
* * 
* 
'''

n=5
for i in range(n):
    for j in range(n-i):
        print('* ', end='')
    print()

print('.........................................')

n=5
for i in range()
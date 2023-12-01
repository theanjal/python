#function

def func1(a):
    print(a)

func1('hello')

#multiplication table
n=int(input('enter a no. :\n'))
def mul(n):
    for i in range(1,11):
        m=n*i
        print(m)
mul(n)


#even or odd
n=int(input('enter a number :\n'))
def odev(n):
    if n%2==0:
        print('number is even')
    else:
        print('number is odd')
odev(n)


#lower to upper
n=input('enter a string :\n')
def upp(n):
    m=n.upper()
    print(m)
upp(n)


#count vowel consonents 
n=input('enter a string :\n')
def count_voco(n):
    count_vowel=0
    count_conso=0
    for i in range(len(n)):
        if n[i] in ['a','e','i','o','u','A','E','I','O','U']:
            count_vowel=count_vowel+1
        else:
            count_conso=count_conso+1
    print('count of vowels :'+ str(count_vowel))
    print('count of consonents :'+str(count_conso))
count_voco(n)


#area of circle 3.14*r*r
n=float(input('enter radius of circle :\n'))
def circle_area(n):
    area=3.14*n*n
    print(area)
circle_area(n)



#season and suggest chappal rainy,snowy,sunny
n=input('enter the season : (rainy/sunny/snowy)\n')
def suggest_chappal(n):
    if n=='rainy':
        print('please use Sandals')
    elif n=='sunny':
        print('please use Shoes')
    elif n=='snowy':
        print('please use Boots')
suggest_chappal(n)

#factorial



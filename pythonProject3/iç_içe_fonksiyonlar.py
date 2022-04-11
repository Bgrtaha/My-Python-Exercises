'''''''''
def factorial(number):
    if not isinstance(number, int):
        raise TypeError("number must be an integer")
    if not number >= 0:
        raise ValueError("number must be zero or positive")

    def inner_factorial(number):
        if number <= 1:
            return 1
        return number * inner_factorial(number - 1)
    return inner_factorial(number)

try:
    print(factorial(4))
except Exception as ex:
    print(ex)
'''''''''

'''''''''
def usalma(number):
    def inner(power):
        return number ** power

    return inner

two = usalma(2)  # 2-3
three = usalma(3)  # 3-4

print(two(3))
print(three(2))
'''''''''

'''''''''
def yetki_sorgula(page):
    def inner(role):
        if role == 'Admin':
            return "{0} rolü {1} sayfasına ulaşabilir.".format(role,page)
        else:
            return "{0} rolü {1} sayfasına ulaşamaz.".format(role,page)
    return inner

user1 = yetki_sorgula('Product Edit')
print(user1("Admin"))
print(user1("User"))
'''''''''

'''''''''
def islem(islem_adi):
    def toplam(*args):
         toplam = 0
         for i in args:
             toplam+=i
         return toplam

    def carpma(*args):
         carpim = 1
         for i in args:
             carpim*=i
         return carpim

    if islem_adi == "toplama":
        return toplam
    else:
        return carpma

toplama = islem("toplama")
print(toplama(1,3,5,6,7))
çarpma = islem("çarpma")
print(çarpma(1,2,3,4,5))
'''''''''
'''''''''
def toplama(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b

def islem(f1, f2, f3, f4, islem_adi):
    if islem_adi == "toplama":
        print(f1(2,3))
    elif islem_adi == "cikarma":
        print(f2(5,3))
    elif islem_adi == "carpma":
        print(f3(3,4))
    elif islem_adi == "bolme":
        print(f4(10,2))
    else:
        print("geçersiz işlem...")

islem(toplama, cikarma, carpma, bolme, "toplama")
islem(toplama, cikarma, carpma, bolme, "cikarma")
islem(toplama, cikarma, carpma, bolme, "carpma")
islem(toplama, cikarma, carpma, bolme, "bolme")
islem(toplama, cikarma, carpma, bolme, "toplamaa")
'''''''''
'''''''''
def my_decorator(func):
    def wrapper(name):
        print ("fonksiyondan önceki işlemler")
        func(name)
        print("fonksiyondan sonraki işlemler")
    return wrapper
@my_decorator
def sayHello(name):
    print("hello", name)
sayHello('ali')

#sayHello = my_decorator(sayHello)
#sayHello()
'''''''''
'''''''''
import math
import time

def calculate_time(func):
    def inner(*args,**kwargs):
        start = time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish = time.time()
        print("fonksiyon "+func.__name__+" "+ str(finish-start) + "saniye sürdü.")
    return inner

@calculate_time
def usalma(a,b):
   print (math.pow(a,b))

@calculate_time
def faktoriyel(num):
    print(math.factorial(num))

@calculate_time
def toplama(a,b):
    print(a+b)

usalma(2,3)
faktoriyel(4)
toplama(10,20)
'''''''''

# 1- Girilen 2 sayıdan hangisi büyüktür ?
'''''''''
a = int(input('a: '))
b = int(input('b: '))
if a > b:
    print(f'a: {a} b: {b} den büyüktür.')
else:
    print(f'a: {a} b: {b} den küçüktür.')
'''''''''

# 2- Kullanicıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız. Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
'''''''''
vize1 = float(input('1. vize: '))
vize2 = float(input('2. vize: '))
final = float(input('final: '))
ortalama = (((vize1 + vize2)/2) * 0.6) + (final * 0.4)
if ortalama >= 50:
    print(f'not ortalamanız : {ortalama} ve geçtiniz')
else:
    print(f'not ortalamanız : {ortalama} ve kaldınız')
'''''''''

# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırın.
'''''''''
sayi = int(input('sayı: '))
if sayi % 2 == 0:
    print('sayı çift')
else:
    print('sayı tek')
'''''''''

# 4- Girilen bir sayının negatif pozitif durumunu yazdırın.
'''''''''
sayi = int(input('sayı: '))
if sayi >= 0:
    print('pozitif')
else:
    print('negatif')
'''''''''

# 5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
# (email: email@sadikturan.com parola:abc123)
'''''''''
email = 'email@sadikturan.com'
password = 'abc123'
girilenEmail = input('email: ')
girilenPassword = input('parola: ')
if girilenEmail == email and girilenPassword == password:
    print('hoşgeldiniz')
elif girilenEmail == email and girilenPassword != password:
    print('parola yanlış')
elif girilenEmail != email and girilenPassword == password:
    print('email yanlış')
else:
    print('yanlış giriş yaptınız')
'''''''''


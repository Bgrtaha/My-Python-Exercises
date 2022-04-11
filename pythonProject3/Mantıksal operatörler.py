# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
'''''''''
sayi = float(input('sayı: '))
if (sayi > 0) and (sayi <= 100):
    print(f'sayı 0-100 arasında.')
else:
    print(f'sayı 0-100 arasında değil.')
'''''''''

# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
'''''''''
sayi = int(input('sayı: '))
if (sayi > 0) and (sayi % 2 == 0):
    print('girilen sayı pozitif çift sayı')
elif (sayi > 0) and (sayi % 2 != 0):
    print('girilen sayı pozitif tek sayı')
elif (sayi < 0) and (sayi % 2 == 0):
    print('girilen sayı negatif çift sayı')
elif (sayi < 0) and (sayi % 2 != 0):
    print('girilen sayı negatif tek sayı')
else:
    print('sayı 0')
'''''''''

# 3- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
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

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
'''''''''
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
if a > b > c:
    print(f'{a} > {b} > {c}')
elif a > c > b:
    print(f'{a} > {c} > {b}')
elif b > a > c:
    print(f'{b} > {a} > {c}')
elif b > c > a:
    print(f'{b} > {c} > {a}')
elif c > a > b:
    print(f'{c} > {a} > {b}')
elif c > b > a:
    print(f'{c} > {b} > {a}')
else:
    print('daha devam ettirilir de zaman kaybı')
'''''''''

#5- Kullanıcidan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#   Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#   a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
#   b-) Finalden 70 alındığında ortalamanın önemi olmasın.
'''''''''
vize1 = float(input('1. vize: '))
vize2 = float(input('2. vize: '))
final = float(input('final: '))
ortalama = (((vize1 + vize2)/2) * 0.6) + (final * 0.4)
if (ortalama >= 50 and final >= 50) or final >= 50:
    print(f'not ortalamanız : {ortalama} ve geçtiniz')
else:
    print(f'not ortalamanız : {ortalama} ve kaldınız')
'''''''''

# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#Formül: (Kilo / boy uzunluğunun karesi)
#Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
# 0-18.4 => Zayıf
# 18.5-24.9 => Normal
# 25.0-29.9 => Fazla Kilolu
# 30.0-34.9 => Şişman (Obez)
'''''''''
name = input('adınız: ')
kg = float(input('kilonuz: '))
hg = float(input('boyunuz: '))
index = (kg) / (hg ** 2)
if (index >= 0) and (index<=18.4):
    print(f'{name} az yemek ye zayıfsın')
elif (index>18.4) and (index<=24.9):
    print(f'{name} normalsin süper boyle devam')
elif (index>24.9) and (index<=29.9):
    print(f'{name} dikkat et kilolu olmaya baslamıssın gidisat iyi degil')
elif (index>=29.9) and (index<=34.9):
    print(f'{name} olm obez olmussun lan aç tartılsan 150 kilo gelirsin ')
else:
    print('sen ölmüşsün')
'''''''''

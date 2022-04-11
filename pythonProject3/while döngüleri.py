sayilar = [1,3,5,7,9,12,19,21]
# 1: sayilar listesini while ile ekrana yazdırın.
'''''''''
i = 0
while i < len(sayilar):
    print(sayilar[i])
    i += 1
'''''''''

# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm
#3   tek sayıları ekrana yazdırın.
'''''''''
başlangıc = int(input('ilk değerinizi girin: '))
bitiş = int(input('2. değerinizi girin: '))
i = başlangıc + 1
while i < bitiş:
    if i % 2 == 1:
        print(i)
    i += 1
'''''''''

# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.
'''''''''
max = 100
min = 1
while max > min+1:
    max -= 1
    print(max)
'''''''''

# 4: Kullanicıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde
#    yazdırın.
'''''''''
sayılar = []

while len(sayılar) < 5:
    sayı = int(input('sayı giriniz: '))
    sayılar.append(sayı)
sayılar.sort()
print(sayılar)
'''''''''

# 5: Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesinde saklayın.
# ** ürün sayısını kullanicıya sorun.
# ** dictionary listesi yapısı (name, price) şeklinde olsun.
# ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.
'''''''''
ürünler = []

ürün_sayisi = int(input('kaç ürün eklemek istersiniz: '))

while len(ürünler) < ürün_sayisi:
    name = input('ürün adı: ')
    price = input('ürün fiyatı: ')
    ürünler.append({
        'name': name,
        'price': price
    })

for ürün in ürünler:
    print(ürün)
'''''''''

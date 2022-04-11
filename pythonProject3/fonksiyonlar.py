# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyon yazınız.
'''''''''
def yazdir(kelime, adet):
    print(kelime * adet)

yazdir('merhaba ',5)
'''''''''

# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çevir.
'''''''''
def listeye_cevir(*params):
    liste = []
    for param in params:
        liste.append(param)
    return liste
print(listeye_cevir(1,2,3,4,1,'merhaba'))
'''''''''

'''''''''
# 3- Gönderilen 2 sayi arasındaki tüm asal sayıları bulun.
sayı1 = int(input('ilk sayıyı girin: '))
sayı2 = int(input('2.sayıyı girin: '))

def iki_sayı_arasındaki_asal_sayi(sayı1,sayı2):
    for sayı in range(sayı1,sayı2+1):
        if sayı > 1:
            for i in range(2, sayı):
                if (sayı % i == 0):
                    break
            else:
                print(sayı)
iki_sayı_arasındaki_asal_sayi(sayı1,sayı2)
'''''''''

# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde yazdırın.
'''''''''
def tam_bölenlerini_bul(sayi):
    tamBolenler = []

    for i in range(2,sayi):
        if sayi % i == 0:
            tamBolenler.append(i)
    return tamBolenler

print(tam_bölenlerini_bul(30))
'''''''''






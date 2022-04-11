def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(':')
    ogrenci_name = liste[0]
    notlar = liste[1].split(',')
    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])
    ortalama = (not1+not2+not3)/3

    if 100 >= ortalama >= 90:
        harf = 'AA'
    elif 89 >= ortalama >= 80:
        harf = 'BA'
    elif 79 >= ortalama >= 70:
        harf = 'BB'
    elif 69 >= ortalama >= 60:
        harf = 'CB'
    elif 59 >= ortalama >= 50:
        harf = 'CC'
    else:
        harf = 'FF'

    return ogrenci_name + ':' + harf + '\n'

def ortalamalari_oku():
    with open("sinav_notlari.txt","r",encoding='utf-8') as file:
        data = file.readlines()
        print(type(data))

       # for satir in file:
       #     print(not_hesapla(satir))

def not_gir():
    ad = input('öğrenci adı: ')
    soyad = input('öğrenci soyad: ')
    not1 = input('not 1: ')
    not2 = input('not 2: ')
    not3 = input('not 3: ')
    with open("sinav_notlari.txt","a",encoding='utf-8') as file:
        file.write(ad + ' ' + soyad +':' +not1 + ',' +not2+ ',' +not3+'\n')

def notlari_kayitet():
    with open('sinav_notlari.txt','r',encoding='utf-8') as file:
        liste=[]

        for i in file:
            liste.append(not_hesapla(i))

        with open('sonuclar.txt','w',encoding='utf-8') as file2:
            for x in liste:
                file2.write(x)



while True:
    islem = input('1- Notları Oku\n2- Not Gir\n3- Notları Kayıt Et\n4- Çıkış')

    if islem == '1':
        ortalamalari_oku()
    elif islem == '2':
        not_gir()
    elif islem == '3':
        notlari_kayitet()
    else:
        break
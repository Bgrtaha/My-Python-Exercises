#1- Bilgileri verilen öğrencileri kullanicıdan aldığınız bilgilerle dictionary içinde saklayınız.
ogrenciler = {
    '120': {
        'ad': 'Ali',
        'soyad': 'Yılmaz',
        'telefon': '532 000 00 01'
    },
    '125': {
        'ad': 'Can',
        'soyad': 'Korkmaz',
        'telefon': '532 000 00 02'
    },
    '128': {
        'ad': 'Volkan',
        'soyad': 'Yükselen',
        'telefon': '532 000 00 03'
    }
}

ogrenciler = {}

while len(ogrenciler.keys()) < 3:
    number = input("öğrenci no: ")
    name = input("öğrenci adı: ")
    surname = input ("öğrenci soyad: ")
    phone = input("öğrenci telefon: ")

    #ogrenciler[number] = {
    #'ad': name,
    #'soyad': surname,
    #'telefon': phone
    #}

    ogrenciler.update({
        number: {
            'ad': name,
            'soyad': surname,
            'telefon':phone
        }
    })
print(ogrenciler)


#2- öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.
ogrNo = input("Öğrenci numarası yazın: ")
ogrenci = ogrenciler[ogrNo]

print(ogrenci)




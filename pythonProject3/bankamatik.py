SadikHesap = {
    'ad': 'Sadık Turan',
    'hesapNo': '13245678',
    'bakiye': 3000,
    'ekHesap': 2000
}
AliHesap = {
    'ad': 'Ali Turan',
    'hesapNo': '12345678',
    'bakiye': 2000,
    'ekHesap': 1000
}
miktar= int(input('Kaç para çekmek istersiniz?: '))
def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if hesap['bakiye'] >= miktar:
        hesap['bakiye'] -= miktar
        print(f"parayı çektiniz. Kalan bakiyeniz: {hesap['bakiye']} , kalan ek hesap limitiniz: {hesap['ekHesap']}")
    else:
        toplam_miktar = hesap['bakiye'] + hesap['ekHesap']
        if toplam_miktar >= miktar:
            ek_hesap_izni = input('ek hesap kullanmak istermisiniz?(e/h): ')
            if ek_hesap_izni == 'e':
                hesap['ekHesap'] = toplam_miktar - miktar
                hesap['bakiye'] = 0
                print(f"parayı çektiniz. Kalan bakiyeniz: {hesap['bakiye']} , kalan ek hesap limitiniz: {hesap['ekHesap']}")
            else:
                print('ek hesapsız bakiyeniz yetersiz kalıyor.')
        else:
            print('bakiye yetersiz')

paraCek(SadikHesap,miktar)

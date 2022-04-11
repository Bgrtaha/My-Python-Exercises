'''''''''
1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile
buldurmaya çalışın. (hak = 5)
** "random modülü" için "python random" şeklinde arama yapın.
** 100 üzerinden puanlama yapın. Her soru 20 puan.
** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın.
'''''''''
'''''''''
import random
sayı = random.randint(1,10)
hak_sayısı = int(input('kaç hak kullanmak istersiniz?: '))
can = hak_sayısı
sayaç = 0
#puan =(100-((100/hak_sayısı)*(sayaç-1)))
while can > 0:
    can -= 1
    sayaç += 1
    tahmin = int(input('sayıyı tahmin ediniz: '))

    if sayı == tahmin:
        print(f'Tebrikler {sayaç}. denemenizde buldunuz. Puanınız {100-(100/hak_sayısı)*(sayaç-1) }')
        break
    elif tahmin > sayı:
        print('Aşşağı')
    else:
        print('Yukarı')
    if can == 0:
        print(f'Bilemediniz. Sayı {sayı} idi.')
        break
'''''''''

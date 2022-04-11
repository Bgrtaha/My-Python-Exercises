# Soru: Girilen bir sayının asal olup olmadığını bulun.

sayı = int(input('sayıyı giriniz: '))
for asal in range(2, sayı):

    if (sayı % asal == 0):
        print(f'{sayı} sayısı asal değildir.')
        break
else:
    print(f'{sayı} sayısı asaldır.')

from random import randint
rand=randint(1, 100)
 
while True:
    sayi=int(input("1 ile 100 arasında değer gir):"))
    if sayi < rand:
        print("Daha Yüksek Bir Sayı Girin.")
        continue
    if sayi > rand:
        print("Daha Düşük Bir Sayı Girin.")
        continue
    else:
        print("Rastele seçilen sayı {0}!".format(rand))
        break
liste_1 = input('Aralarında 0 (sıfır) da bulunan en az 3 tane sayıyı aralarında boşluk bırakarak yazınız. ');
liste = list(map(int, liste_1.split()))
liste_2 = []

liste_2 = [sayi for sayi in liste if sayi == 0]
liste_2 += [sayi for sayi in liste if sayi != 0]

print(liste)
print(liste_2)
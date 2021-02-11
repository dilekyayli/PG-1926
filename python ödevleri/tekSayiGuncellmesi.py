liste = []
tek_liste = []
liste_sayi = int(input('Kaç tane sayı girilecek: '))

for sor in range(liste_sayi):
    girilen_sayi = int(input('Sayıyı giriniz: '))
    liste.append(girilen_sayi)
    print(liste)

for sayi in liste:
    if(sayi%2==1):
        tek_liste.append(sayi)

tek_liste.sort()
print('En büyük tek sayı: ' ,tek_liste[len(tek_liste)-1])
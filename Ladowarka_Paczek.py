waga_suma = 0
paczki = 0
aktualna_waga = 0
waga_min = 20
paczka_min = 0

ilosc_paczek = int(input("Ile elementów chcesz wysłać? "))
if ilosc_paczek < 1:
    paczki -= 1
    print("Paczek musi być conajmniej 1 szt.")

for i in range(ilosc_paczek):
    while True:
        waga = int(input("Podaj wagę każdego elementu do wysłania: "))
        if waga < 1 or waga > 10:
            print("Waga paczki nieprawidłowa, elementy mogą ważyć od 1 kg do max 10 kg \n")
            print("Dodawanie paczek zostaje przerwane, a wszystkie paczki zostały wysłane\n")
            break

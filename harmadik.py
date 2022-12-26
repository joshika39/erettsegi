# - valtozok es beolvasas
# - elagazasok
# - ciklusok
# - osztalyok
# - listak
# - fajlkezeles
# - fuggveny

tizedes = 3.14  # lebegopontos - float szam
egesz = 123  # INT
ujszam = egesz * tizedes
teszt = True
teszt2 = False

k_nev = "Joshua"
v_nev = "Hegedus"

print(f'{v_nev} {k_nev}')
kor = int(input('Kor: '))

if kor >= 60:
    print('Hat maga mar idos')
    print('Jejj, bent vagyok az if ben')
    print('Ez csak akkor fut le, ha az ember kora nagyobb mint hatvan')
else:
    print('Hat neked meg elotted az elet')

if kor >= 60:
    print('Hat maga mar idos')
    print('Jejj, bent vagyok az if ben')
    print('Ez csak akkor fut le, ha az ember kora nagyobb mint hatvan')
elif kor >= 40:
    print('Maga kozepkoru')
elif kor >= 30:
    print('Maga majdnem kozepkoru')
elif kor == 20:
    print('ez az ev emanuella kedvence eve')
else:
    print('Hat neked meg elotted az elet')

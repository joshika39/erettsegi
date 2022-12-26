import math
import random

dobasok = ['F', 'I']

# HF: Kicserelni a random.choice-t a lenti hosszabb reszre

# szam = random.randint(1, 10)
# if szam % 2 == 0:
#     print(f'{szam}: paros')
#     dobas = 'I'
# else:
#     print(f'{szam}: paratlan')
#     dobas = 'F'

print('1. Feladat')
dobas = random.choice(dobasok)
print(f'Pénzfeldobás eredménye: {dobas}')


print('2. Feladat')
# bekeri a felhasznalo tippjet
tipp = input('Tippeljen! (F/I)= ')

# Leellenőrzi, hogy jó e a tipp
dobas = random.choice(dobasok)
if dobas == tipp:
    print('Ön eltalálta.')
else:
    print('Ön nem találta el.')

file = open('kiserlet.txt', 'r')

print('3. Feladat')
dobasszam = 0
for sor in file.readlines():
    if sor != '':
        dobasszam += 1
print(f'A kiserlet {dobasszam} dobasbol allt.')

print('4. Feladat')
fejek = 0

# !!! Ha egyszer vegig megyunk a file-on, akkor az olvasast ujra kell inditani !!!
file.seek(0)  # NAGYON FONTOS VISSZATENNI AZ OLVASOT
for sor in file.readlines():
    if sor[0] == "F":
        fejek += 1

print(f'A fej relativ gyakorisaga a kiserlet soran {round(fejek/dobasszam*100, 2)}% volt')  # Sima kerekites
print(f'A fej relativ gyakorisaga a kiserlet soran {math.floor(fejek/dobasszam*100)}% volt')  # Lefele kerekites
print(f'A fej relativ gyakorisaga a kiserlet soran {math.ceil(fejek/dobasszam*100)}% volt')  # Felfele kerekites


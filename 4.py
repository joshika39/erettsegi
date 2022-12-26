oraszam = '4., 5.'
print(f'Ez a {oraszam} ora')

lista = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# lista = range(1, 101)
# Start

szam = int(input('Kerek egy szamot: '))

for i in range(1, 11):
    print(f'Most az i erteke: {i}')
    print(f'Az {i} + {szam} = {i + szam}')

szam = 0
while szam < 20:
    if szam > 10:
        print(f"{szam} nagyobb mint 10")
    elif szam < 10:
        print(f"{szam} kisebb mint 10")
    else:
        print(f"Az i az {szam}")
    szam += 1


print('Feladat: Irasd ki az elso n termeszetes szamot')
n = int(input('Meddig irjam a szamokat: '))
for i in range(1, n + 1):
    print(i)
    if i >= 100:
        break
else:
    print(f'Kiirtam a szamokat: {n}-ig')

print()
print('Lista kiiratas:')
# szamok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# for i in szamok:
#     print(i)

fruits = ['alma', 'korte', 'barack', 'szilva', 'eper']
rossz_gyumolcs = input('Adjon meg egy nemszeretett gyumolcsot: ')
for gyumolcs in fruits:
    if gyumolcs == rossz_gyumolcs:
        print(f'Te nem szereted a(z) {gyumolcs} gyumolcsot')
        break
else:
    print("Te minden gyumolcsot szeretsz a listabol")

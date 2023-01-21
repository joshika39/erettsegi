
file = open('valaszok.txt', 'r')
sorok = file.readlines()

# print(sorok[0])

versenyzok = []
valaszok = []

for i in range(1, len(sorok)):
    # print(i)
    sor = sorok[i]  # FIGYELEM: itt indexet hasznalunk
    # print(f'{i+1}. {sor}', end='')

    adatok = sor.split(' ')
    versenyzok.append(adatok[0].strip())
    valaszok.append(adatok[1].strip())  # STRIP hasznalata

# print(versenyzok)
# print(valaszok)

print('3. Feladat')
versenyzok_hossz = len(versenyzok)
azonosito = input('A versenyző azonosítója = ')
for i in range(0, versenyzok_hossz):
    if versenyzok[i] == azonosito:
        print(f'{valaszok[i]}\t(a versenyzo valasza)')


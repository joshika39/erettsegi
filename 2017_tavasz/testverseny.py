
file = open('valaszok.txt', 'r')
sorok = file.readlines()

# print(sorok[0])

versenyzok = []
valaszok = []

jo_megoldas = sorok[0].strip()

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
kivalasztott = 0
for i in range(0, versenyzok_hossz):
    if versenyzok[i] == azonosito:
        print(f'{valaszok[i]}\t(a versenyzo valasza)')
        kivalasztott = i

print("4. Feladat")
kivalasztott_valasz = valaszok[kivalasztott]
print(f'{jo_megoldas}\t(a helyes megoldás)')
for i in range(0, len(jo_megoldas)):
    if kivalasztott_valasz[i] == jo_megoldas[i]:
        print('+', end='')
    else:
        print(' ', end='')
print('\t(a versenyző helyes válaszai)')

print('5. Feladat')
sorszam = input(' A feladat sorszáma = ')
sorszam = int(sorszam)

feladat = jo_megoldas[sorszam - 1]
helyes_valaszok = 0
for i in range(0, len(valaszok)):
    v_feladat = valaszok[i]
    if v_feladat[sorszam - 1] == feladat:
        helyes_valaszok += 1
szazalek = (helyes_valaszok / len(valaszok)) * 100
print(f'A feladatra {helyes_valaszok} fő, a versenyzők {round(szazalek, 2)}%-a adott helyes választ.')

print('6. Feladat: A versenyzők pontszámának meghatározása')
pontok_file = open('pontok.txt', 'w')

for i in range(0, len(valaszok)):
    pontszam = 0
    for j in range(0, len(jo_megoldas)):
        if jo_megoldas[j] == valaszok[i][j]:
            if j >= 0 and j <= 4:
                pontszam += 3
            elif j >= 5 and j <= 9:
                pontszam += 4
            elif j >= 10 and j <= 12:
                pontszam += 5
            elif j == 13:
                pontszam += 6
    pontok_file.write(f'{versenyzok[i]} {pontszam}\n')
pontok_file.close()
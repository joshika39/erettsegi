# 1. fajl eltarolasa valtozoban -> read (r) mode
file = open('autok.txt', 'r')

# 1.1 Kivesszuk a sorokat a file-bol -> sorok: list[str]
sorok = file.readlines()

# 1.1.1 adatokat tarolo lista
adminisztracio = []

# 1.2 Vegig megyunk a sorokon,

# - for i in range(0, len(sorok)) -> ha elter az elso valahany sor
# elso_sor = sorok[0]
# masodik_sor = sorok[1]

# for i in range(2, len(sorok)):
#     sor = sorok[i]  # kivesszuk hasznalatra az adott sort
#     csupasz_sor = sor.strip()  # lecsupaszitja az alabbi karaktereket: \n, \t, ' '
#     print(csupasz_sor)

# - for sor in sorok -> ha minden sor ugyan olyan

for sor in sorok:
    csupasz_sor = sor.strip()  # lecsupaszitja az alabbi karaktereket: \n, \t, ' '
    # print(csupasz_sor)  # teszt esetere

    # 1.3 feldaraboljuk a sor adatait a feladatban megadott elvalasztoval: \t , ' ', :, ;
    adatok = csupasz_sor.split(' ')

    # 1.4 ideiglenes lista keszitese
    ideig_lista = [int(adatok[0]), adatok[1], adatok[2], int(adatok[3]), int(adatok[4]), int(adatok[5])]

    # 1.5 az ideiglenes lista eltarolasa a fo listaban
    adminisztracio.append(ideig_lista)

print('2. Feladat')
utolso_auto = -1

gyumik = ["alma", "korte", "barack", "japan datolyaszilva", "sarkanygyumolcs"]
print(f'a lista hossza: {len(gyumik)}')

for i in range(len(gyumik) - 1, -1, -1):
    print(f'{i}: {gyumik[i]}')

# for i in range(len(adminisztracio) - 1, 0, -1): # ha visszafele megyunk: utolso index -> lista hossz - 1
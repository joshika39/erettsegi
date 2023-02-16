file = open('ajto.txt')
sorok = file.readlines()

atjarasok = []

for sor in sorok:
    sor = sor.strip()  # !!!!!! Ne felejtsd el !!!!!!!
    adatok = sor.split(' ')
    seged_lista = [int(adatok[0]), int(adatok[1]), int(adatok[2]), adatok[3]]
    atjarasok.append(seged_lista)

print("2. Feladat")
elso_belepo = atjarasok[0][2]
utolso_kilepo = -1
for i in range(len(atjarasok) - 1, 0, -1):
    if atjarasok[i][3] == "ki":
        # print(atjarasok[i])  # csak tesztelesre
        utolso_kilepo = atjarasok[i][2]
        break
print(f"Az első belépő: {elso_belepo}")
print(f"Az utolsó kilépő: {utolso_kilepo}")

# print("3. Feladat")
szemelyek_athaladasa = [0 for i in range(0, 51)]

for atjaras in atjarasok:
    szemelyek_athaladasa[atjaras[2]] += 1

athaladas_file = open('athaladsok.txt', 'w')

for i in range(0, 51):
    if szemelyek_athaladasa[i] != 0:
        athaladas_file.write(f"{i} {szemelyek_athaladasa[i]}\n")
        
athaladas_file.close()

print('4. Feladat')
bent_tartozkodoak = []
for ember in atjarasok:
    if ember[3] == "be":
        bent_tartozkodoak.append(ember[2])
    elif ember[3] == "ki":
        bent_tartozkodoak.remove(ember[2])

print("A végén a társalgóban voltak: ", end='')
bent_tartozkodoak = sorted(bent_tartozkodoak)
for elem in bent_tartozkodoak:
    print(f"{elem} ", end='')
print()

print('5. Feladat')
bent_levok = 0
max_bent_levok = 0
max_ido = []
for ember in atjarasok:
    if ember[3] == "be":
        bent_levok += 1
    elif ember[3] == "ki":
        bent_levok -= 1
    if max_bent_levok < bent_levok:
        max_bent_levok = bent_levok
        max_ido = [ember[0], ember[1]]
print(f'Például {max_ido[0]}:{max_ido[1]}-kor voltak a legtöbben a társalgóban.')


print('6. Feladat')
azonosito = int(input('Adja meg a személy azonosítóját! '))

print('7. Feladat')
for ember in atjarasok:
    if ember[2] == azonosito and ember[3] == "be":
        print(f'{ember[0]}:{ember[1]}-', end='')
    elif ember[2] == azonosito and ember[3] == "ki":
        print(f'{ember[0]}:{ember[1]}')

print('\n8. Feladat')
def percbe(ora, perc):
    return ora * 60 + perc

ossz_perc = 0
bent_van = False
for ember in atjarasok:
    # belepes = 0

    if ember[2] == azonosito and ember[3] == "be":
        ossz_perc -= percbe(ember[0], ember[1])
        bent_van = True
    elif ember[2] == azonosito and ember[3] == "ki":
        ossz_perc += percbe(ember[0], ember[1])
        bent_van = False

if bent_van:
    ossz_perc += percbe(15, 0)
    print(f'A(z) {azonosito}. személy összesen {ossz_perc} percet volt bent, a megfigyelés végén a társalgóban volt.')
else:
    print(f'A(z) {azonosito}. személy összesen {ossz_perc} percet volt bent, a megfigyelés végén nem volt a társalgóban.')


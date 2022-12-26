file = open("kerites.txt", "r")
keritesek = []

for sor in file.readlines():
    adatok = sor.split(' ')
    kerites = []
    kerites.append(int(adatok[0]))
    kerites.append(int(adatok[1]))
    kerites.append(adatok[2])
    keritesek.append(kerites)

# Beta feladat: az adatokat feldolgozva irasd ki erthetoen, hogy a 15 meternel szelesebb keritesek melyik oldalon vannak

for kerites in keritesek:
    if kerites[1] >= 15:
        if kerites[0] == 0:
            print(f'Kerites a paros oldalon van, a szelesseg {kerites[1]}')
        else:
            print(f'Kerites a paratlan oldalon van, a szelesseg {kerites[1]}')

print("2. Feladat")
print(f'Az eladott telkek száma: {len(keritesek)}')

print("3. Feladat")
if keritesek[-1][0] == 0:
    print('A páros oldalon adták el az utolsó telket. ')
else:
    print('A páros oldalon adták el az utolsó telket. ')



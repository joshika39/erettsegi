

def hivas_mpbe(hivas):
    return mpbe(hivas[0], hivas[1], hivas[2])


print('5. Feladat')

ora_str = input('Adjon meg egy idopontot! (ora perc masodperc) ')
adatok = ora_str.split(' ')

ora = int(adatok[0])
perc = int(adatok[1])
mp = int(adatok[2])
ido_mp = mpbe(ora, perc, mp)
beszelo = -1
varakozo = 0
hivasok_hossz = len(kicsatl)

for i in range(hivasok_hossz-1, 0, -1):
    becsatl_mp = hivas_mpbe(becsatl[i])
    kicsatl_mp = hivas_mpbe(kicsatl[i])

    if becsatl_mp <= ido_mp and ido_mp < kicsatl_mp:
        varakozo += 1
        beszelo = i

if beszelo > -1:
    print(f'A varakozok szama: {varakozo-1} a beszelo a {beszelo + 1}. hivo.')
else:
    print('Nincs beszelo')


print('6. Feladat')
vegso = 0
vegso_elott = 0
for i in range(0, hivasok_hossz):
    becsatl_mp = hivas_mpbe(becsatl[i])
    kicsatl_mp = hivas_mpbe(kicsatl[i])
    if becsatl_mp < mpbe(12, 0, 0) and hivas_mpbe(kicsatl[i]) > hivas_mpbe(kicsatl[vegso]):
        vegso_elott = vegso
        vegso = i

varakozas = hivas_mpbe(kicsatl[vegso_elott]) - hivas_mpbe(becsatl[vegso])
print(f'Az utolso telefonalo adatai a(z) {vegso + 1}. sorban vannak, {varakozas} masodpercig vart.')
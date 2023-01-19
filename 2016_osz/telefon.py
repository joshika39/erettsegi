def mpbe(o: int, p: int, mp: int):
    o_mp = o * 60 * 60
    p_mp = p * 60
    return o_mp + p_mp + mp


file = open('hivas.txt', 'r')

becsatl = []
kicsatl = []

# vegig megyunk a sorokat tarolo lista elemein
sorok = file.readlines()
for sor in sorok:
    # print(sor, end='')  # csak tesztelesre

    # Feldaraboljuk az egesz "asdsad asda fgfd dsfwf" fajta stringet a szokozok menten
    adatok = sor.split(' ')
    # print(adatok)  # csak tesztelesre

    # Atalkitjuk szamma az adatok lista tartalmat
    szamok = []
    for adat in adatok:
        szamok.append(int(adat))
    # print(szamok)  # csak tesztelesre

    # Amikor egy sor elemeit szeretnenk kulon eltarolni, azt mindig 'lista a listaban' modon csinaljuk
    b_o, b_p, b_mp = szamok[0], szamok[1], szamok[2]
    k_o, k_p, k_mp = szamok[3], szamok[4], szamok[5]

    becsatl.append([b_o, b_p, b_mp])  # al lista igy is letre hozhato
    kicsatl.append([k_o, k_p, k_mp])

    # becsatl.append(b_o)
    # becsatl.append(b_p)
    # becsatl.append(b_mp)
    #
    # kicsatl.append(k_o)
    # kicsatl.append(k_p)
    # kicsatl.append(k_mp)

print('3. Feladat')
hivasok = [0 for i in range(0, 20)]  # 0->19ig fel toltjuk nullakkal
print(hivasok)   # csak tesztelesre

for hivas in becsatl:
    hivasok[hivas[0]] += 1

print(hivasok)  # csak tesztelesre

hivasok_hossz = len(hivasok)
for index in range(0, hivasok_hossz):
    if hivasok[index] != 0:
        print(f'{index} ora {hivasok[index]} hivas')

print('4. Feladat')


becsatl_mp = mpbe(becsatl[0][0], becsatl[0][1], becsatl[0][2])
kicsatl_mp = mpbe(kicsatl[0][0], kicsatl[0][1], kicsatl[0][2])
hossz = kicsatl_mp - becsatl_mp

max_hossz = hossz
max_hossz_i = 0

hivasok_hossz = len(kicsatl)
for i in range(1, hivasok_hossz):
    becsatl_mp = mpbe(becsatl[i][0], becsatl[i][1], becsatl[i][2])
    kicsatl_mp = mpbe(kicsatl[i][0], kicsatl[i][1], kicsatl[i][2])
    hossz = kicsatl_mp - becsatl_mp
    if hossz > max_hossz:
        max_hossz = hossz
        max_hossz_i = i

print(f'A leghosszabb ideig vonalban levo hivo {max_hossz_i + 1}. sorban szerepel,a hivas hossza: {max_hossz} masodperc.')

print('5. Feladat')

ora_str = input('Adjon meg egy idopontot! (ora perc masodperc) ')
adatok = ora_str.split(' ')

ora = int(adatok[0])
perc = int(adatok[1])
mp = int(adatok[2])
ido_mp = mpbe(ora, perc, mp)

hivasok_hossz = len(kicsatl)
for i in range(0, hivasok_hossz):
    becsatl_mp = mpbe(becsatl[i][0], becsatl[i][1], becsatl[i][2])
    kicsatl_mp = mpbe(kicsatl[i][0], kicsatl[i][1], kicsatl[i][2])
    if ora >= 8:
        if becsatl_mp < ido_mp and kicsatl_mp > ido_mp:
            print(f'A varakozok szama: _ a beszelo a {i+1}. hivo.')





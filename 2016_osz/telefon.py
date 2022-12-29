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
hivasok = [0 for i in range(0, 20)]
print(hivasok)   # csak tesztelesre

for hivas in becsatl:
    hivasok[hivas[0]] += 1

print(hivasok)  # csak tesztelesre

for index, hivas in enumerate(hivasok):
    if hivas != 0:
        print(f'{index} ora {hivas} hivas')

# hivasszam = 0  # Tarolja az egy orahoz tartozo hivasok szamat
# jelen_ora = becsatl[0][0]  # Eloszor beallitom a legelso hivas orajara
# for i, hivas in enumerate(becsatl):  # Hasznat veszem a lista elemeinek az indexenek
#
#     # Megnezem, hogy az epp szamolas alatti ora van e soron
#     if jelen_ora == becsatl[i][0]:
#         hivasszam += 1  # noveljuk egyel a jelen hivasok szamat
#
#     #  Megnezzuk van e kovetkezo elem
#     if i + 1 < len(becsatl):
#
#         # Van e ora valtas es ha igen, akkor mindent vissza allitunk az alap allapotba
#         if becsatl[i][0] != becsatl[i + 1][0]:
#             print(f'{jelen_ora} ora {hivasszam} hivas')
#             # print(f'Ora valtas tortent: {becsatl[i][0]} != {becsatl[i + 1][0]}')
#             hivasszam = 0
#             jelen_ora = becsatl[i + 1][0]  # kovetkezo elem ora erteke


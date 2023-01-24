
megallok = []
datumok = []
idopk = []
azonositok = []
tipusok = []
ervenyessegek = []


class UtasAdat:
    def __init__(self, sor):
        adatok = sor.split(' ')
        self.megallo = int(adatok[0])
        ido_adat = adatok[1].split('-')
        self.datum = ido_adat[0]
        self.ido = ido_adat[1]
        self.azon = adatok[2]
        self.j_tipus = adatok[3]
        self.ervenyesseg = adatok[4]


utasadatok = []  # type: list[UtasAdat]

file = open('utasadat.txt', 'r')
sorok = file.readlines()

for sor in sorok:
    # Opcio 1
    # utasadat = UtasAdat(sor)
    # utasadatok.append(utasadat)

    # Opcio 2
    adatok = sor.split(' ')
    megallok.append(int(adatok[0]))
    ido_adat = adatok[1].split('-')
    datumok.append(ido_adat[0].strip())
    idopk.append(ido_adat[1].strip())
    azonositok.append(adatok[2].strip())
    tipusok.append(adatok[3].strip())
    ervenyessegek.append(adatok[4].strip())

# minta_utas = utasadatok[0]
# print(minta_utas.azon)

print('2. Feladat')
print(f'A buszra {len(megallok)} utas akart felszállni.')

print('3. Feladat')
eltiltottak = 0
for i in range(0, len(megallok)):
    if len(ervenyessegek[i]) > 2:
        if ervenyessegek[i] < datumok[i]:
            eltiltottak += 1
    else:
        if int(ervenyessegek[i]) == 0:
            eltiltottak += 1
print(f'A buszra {eltiltottak} utas nem szállhatott fel.')

print('4. Feladat')
felszallasok = [0 for i in range(0, 30)]
for i in range(0, len(megallok)):
    megallo = megallok[i]
    felszallasok[megallo] += 1

max_felszallo = felszallasok[0]
max_felszallo_i = 0

for i in range(len(felszallasok) - 1, 0, -1):
    if felszallasok[i] >= max_felszallo:
        max_felszallo = felszallasok[i]
        max_felszallo_i = i

print(f"A legtöbb utas ({max_felszallo} fő) a {max_felszallo_i}. megállóban próbált felszállni.")

print('5. Feladat')
kedvezmenyek = ['TAB', 'NYB']
ingyen_jegyek = ['NYP', 'RVS', 'GYK']
kedvezmenyesek = 0
ingyenesek = 0
for i in range(0, len(megallok)):
    if tipusok[i] in kedvezmenyek:
        if ervenyessegek[i] >= datumok[i]:
            kedvezmenyesek += 1
    elif tipusok[i] in ingyen_jegyek:
        if ervenyessegek[i] >= datumok[i]:
            ingyenesek += 1

print(f"Ingyenesen utazók száma: {ingyenesek} fő")
print(f"A kedvezményesen utazók száma: {kedvezmenyesek} fő")

def napokszama(e1:int, h1:int, n1: int, e2:int, h2: int, n2: int) -> int:
    h1 = (h1 + 9) % 12
    e1 = e1 - h1 // 10
    d1 = 365*e1 + e1 // 4 - e1 // 100 + e1 // 400 + (h1*306 + 5) // 10 + n1 - 1
    h2 = (h2 + 9) % 12
    e2 = e2 - h2 // 10
    d2 = 365*e2 + e2 // 4 - e2 // 100 + e2 // 400 + (h2*306 + 5) // 10 + n2 - 1
    return d2-d1



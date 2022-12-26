# list() -> amikor zarojelet latsz az fuggvenyt jelent

# valtozo = input()
# print(valtozo)

# 1. Feladat: Listaban eltarolni 5 sor erteket, majd irjuk ki az 5 sor erteket

# lista = []
# for i in range(5):  # 5 szor ismetles (0-4 ig), ugy is jo hogy range(1, 6)
#     lista.append(input())
#
# for elem in lista:
#     print(f'"{elem}", {len(elem.split(" "))} ->', elem.split(" "))

# 1. Írd ki a neved (simán print-el)
# 2. Kérjük be a dátumot. (Külön év, honap nap, mind szam kent)
# 3. Írassuk ki a mai dátumot.
# 4. Írassuk ki hanyadika lesz 2 nap múlva. (csak nap, szam)
# 5. Írassuki a dátumot két évvel ezelőtt (egesz datum)

# ev = int(input("Kerem az jelenlegi evet: "))
# honap = int(input("Kerem az jelenlegi honapot (szamkent): "))
# nap = int(input("Kerem az jelenlegi napot (szamkent): "))
#
# print(f'{ev}. {honap}. {nap}. ')
# print(f'2 nap mulva {nap+2}.-ika/ike lesz ')
# print(f'2 evvel ezelott: "{ev-2}. {honap}. {nap}." volt a datum.')

tipus = input("Kerem az atalkitas tipusat: ")
if tipus == "kg":
    x = float(input("Kerem az erteket: "))
    m_egyseg = input("Kerem a mertekegyseget: ")
    if m_egyseg == "kg":
        print(f'{x}kg az {x*1000}g')
    elif m_egyseg == "g":
        print(f'{x}g az {x/1000}kg')
    else:
        print("nem tamogatott mertekegyseg")
elif tipus == "c":
    x = float(input("Kerem az erteket: "))
    m_egyseg = input("Kerem a mertekegyseget: ")
    if m_egyseg == "c":
        print(f'{x}c az {x * 1.8 + 32}f')
    elif m_egyseg == "f":
        print(f'{x}f az {(x - 32) / 1.8}f')
    else:
        print("nem tamogatott mertekegyseg")
else:
    print("Ilyet meg nem tudunk atalakitani")

# + -> osszead
# - -> kivon
# * -> szoroz
# / -> oszt
# % -> maradekosan oszt
# // -> egesz szamos osztas

ido = input("Kezdesi ido (ora:perc) : ")
hossz = int(input("Hossz (percekben): "))
ora, perc = ido.split(':')
ido_perc = int(ora) * 60 + int(perc)  # ez az ido atalakitva percekke
veg_ido = ido_perc + hossz
veg_ora = (veg_ido // 60) % 24
veg_perc = veg_ido - (veg_ido // 60) * 60
print(f'A film {veg_ora}:{veg_perc}-kor fejezdodik')




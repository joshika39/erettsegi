file = open("jarmu.txt", "r")  # r - csak olvasas modban nyitjuk meg

idopontok = []
rendszamok = []

for sor in file.readlines():
    adatok = sor.split(' ')
    print(adatok)
    # idopont = []
    # idopont.append(int(adatok[0]))
    # idopont.append(int(adatok[1]))
    # idopont.append(int(adatok[2]))

    idopontok.append([int(adatok[0]), int(adatok[1]), int(adatok[2])])
    rendszamok.append(adatok[3])

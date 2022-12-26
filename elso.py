# print('Hello World!', end='\n')  # \n -> egy uj sor, \t -> tabulator
# print('Nevem: Joshua', end='')  # ez egy string
alkalom = 2  # int (Integer -> egész) típus
minta = 2.14  # float (lebegőpontos szám) típus

print('Hello World!')
nev = input('Nevem: ')
lakhely = input('Lakhelyem: ')
iskola = input('Iskolám: ')
print('Szia ' + nev)
# kor = input('Korod: ') -> ez str típus
korqwe = int(input('Korod: '))

print(f'Te most {korqwe} eves vagy')
print(f'Ket ev mulva {korqwe + 2} eves leszel')

apukora = korqwe * 2.5
print(f'Apu kora: {apukora}')

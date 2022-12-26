import math

# FUGGVENY DEFINICIO: Egy olyan kodreszlet, amely tobbszor meghivhato, akar mas parameterekkel


def harmadik_oldal():
    ertekek = input('Kerek 2 oldal erteket (a b formaban): ')
    a, b = ertekek.split(' ')
    a = int(a)
    b = int(b)
    print(f'A haromszog oldalai: {a}, {b}')
    pitagorasz = math.sqrt(pow(a, 2) + pow(b, 2))
    return pitagorasz


haromszog1_c = harmadik_oldal()
haromszog2_c = harmadik_oldal()
haromszog3_c = harmadik_oldal()

print(f'haromszog 1 3. oldala: {haromszog1_c}')
print(f'haromszog 2 3. oldala: {haromszog2_c}')
print(f'haromszog 3 3. oldala: {haromszog3_c}')

# fontos linek:
# https://www.w3schools.com/python/python_functions.asp
# https://www.programiz.com/python-programming/function

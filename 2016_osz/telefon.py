
def mpbe(o: int, p: int, mp: int):
    o_mp = o * 60 * 60
    p_mp = p * 60
    return o_mp + p_mp + mp


print(f'{2}:{23}:{45} = {mpbe(2, 23, 45)}mp')
print(f'{1}:{2}:{41} = {mpbe(1, 2, 41)}mp')
print(f'{8}:{6}:{10} = {mpbe(8, 6, 10)}mp')

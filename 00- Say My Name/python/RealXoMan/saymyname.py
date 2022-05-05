def saymyname(name):
    if name.lower() == 'heisenberg':
        return "You're God damn right."
    return "Game Over. You Lose :)"

print("Say My Name O-O: ")
name = input()
print(saymyname(name))
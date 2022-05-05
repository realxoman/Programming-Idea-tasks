def saymyname(name):
    return (("Game Over. You Lose :)","You're goddamn right.")['heisenberg' == name.lower()])

print("Say My Name O-O: ")
name = input()
print(saymyname(name))
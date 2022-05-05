def saymyname(name):
    return ((False,True)['heisenberg' == name.lower() or name == 0])

print("Say My Name O-O: ")
while((condition := False) == False):
    name = saymyname(input())
    if name:
        print("You're goddamn right.")
        break
    print("Wrong, Again. Say My Name O-O: ")
    
    
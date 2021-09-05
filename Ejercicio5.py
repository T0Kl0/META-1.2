def ac (texto):
    x = texto.split()
    z = ''
    for letra in x:
        z += letra[0]
    
    z = z.upper()
    return z

an=input("PUEDE ESCRIBIR: ")
print (ac(an))
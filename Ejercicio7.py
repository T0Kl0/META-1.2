import random

num=random.randrange(1,50)
a= int(input("ESCRIBE UN NUMERO DEL 1 AL 50: "))
print (num)
while a != num:
    if a>50 or a<0: print("PORFAVOR INGRESAR UN NUMERO QUE SE ENCUENTRE ENTRE EL 1 AL 50")
    elif a<num: a= int (input("UN NUMERO MAS ALTO, INGRESE UN NUMERO ENTRE EL 1 AL 50"))
    elif a>num: a= int(input("UN NUMERO MAS BAJO,INGRESE UN NUMERO ENTRE EL 1 AL 50"))
else: print("ES TODO HAZ GANADO")
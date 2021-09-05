def convertidor():
    rawInput = input("\nINGRESA UNA PALABRA O FRASE PARA CHECAR SI ES PALINDROMO: ") 
    rawString = rawInput.lower() 
    rawList = list(rawString) 
    return rawList

def metodo (dirtyList): 
    analphabeticList = [" ", "-", ".", ",", ":", ";", "!", "?", "'", "\""] 
    for character in analphabeticList: 
        if character in dirtyList: 
            dirtyList.remove(character) 
            return metodo(dirtyList)
    return dirtyList 

def checador(straightList):
    reversedList = straightList[::-1] 
    if reversedList == straightList: 
        return "SI ES PALINDORMO!" 
    else: 
        return "NO ES PALINDORMO." 

def main(): 
    print("\nCHECADOR DE PALINDROMO") 
    List = convertidor()  
    List = metodo(List) 
    palindromeCheck = checador(List)
    print(palindromeCheck)

main() 
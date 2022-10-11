def string():
    string = "Bonjour"
    print(string, type(string))
    print("Avec une chaîne vous pouvez afficher les caractères séparément")
    print("Mais vous ne pouvez pas modifier une chaîne")
    for s in string: print(s)
    
def integer():
    string = input("Ecrivez ce que vous voulez : ")
    length = len(string) # on a changé (implicitement) le type de la variable string
    print(length, type(length)) # int veut dire integer (entier relatif -2, -1, 0, 1, 2,...)

def floating_point_number():
    string = input("Ecrivez ce que vous voulez : ")
    ratio = len(string) / len("Python")
    print(ratio, type(ratio)) # float veut dire floating point number (nombre à virugle flottante)

def list_of_elements():
    liste = [True, 1, 2.718, "Bonjour"]
    print(liste, type(liste)) #
    for elt in liste: print(elt)

def n_uplet():
    year_of_birth = int(input("Votre année de naissance = "))
    immuable = (year_of_birth, 2022 - year_of_birth)
    print(immuable, type(immuable)) #
    print(f"Vous êtes né en {immuable[0]} donc vous avez {immuable[1]} ans")

def dictionnaire():
    dico = {"clé" : "valeur", "key" : "value"}
    print("Un dictionnaire fonctionne avec des clé et des valeurs")
    print(dictionnaire, type(dictionnaire))
    for k, v in dico.items(): print(k, v)
   
def ensemble():
    chiffres = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    print(chiffres, type(chiffres))
    for digit in chiffres: print(digit)


    

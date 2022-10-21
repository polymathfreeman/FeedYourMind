def addition(a, b): return a + b
def soustraction(a, b): return a - b
def multiplication(a, b): return a * b
def division_dec(a, b): return a / b    
def division_euc(a, b): return a // b
def modulo(a, b): return a % b
def puissance(a, n): return a ** n
def racine_carree(a): return a ** 0.5
def racine_n_ieme(a, n): return a ** (1/n)

def ab(operation):
    a = int(input("a = "))
    b = int(input("b = "))
    result = operation(a, b)
    return a, b, result 
    
def calculette():
    menu = """
1) Addition +
2) Soustraction -
3) Multiplication *
4) Division décimale /
5) Division euclidienne // 
6) Modulo %
7) Puissance **
8) Racine carrée √
9) Racine n-ième n√
Q) Quitter
Votre choix : """

    choix = True
    while choix:
        choix = input(menu)
        if choix == '1': 
            a, b, result = ab(addition)        
            print(f"{a} + {b} = {result}")
        elif choix == '2': 
            a, b, result = ab(soustraction)        
            print(f"{a} - {b} = {result}")
        elif choix == '3': 
            a, b, result = ab(multiplication)        
            print(f"{a} * {b} = {result}")
        elif choix == '4': 
            a, b, result = ab(division_dec)        
            print(f"{a} / {b} = {result}")
        elif choix == '5': 
            a, b, result = ab(division_euc)        
            print(f"{a} // {b} = {result}")
        elif choix == '6': 
            a, b, result = ab(modulo)        
            print(f"{a} % {b} = {result}")
        elif choix == '7': 
            a, n, result = ab(puissance)        
            print(f"{a} ** {n} = {result}")
        elif choix == '8':
            a = float(input("a = "))
            print(f"√{a} = {racine_carree(a)}")
        elif choix == '9': 
            a, n, result = ab(racine_n_ieme)        
            print(f"{n}√{a} = {result}")
        elif choix.upper() == 'Q':
            choix = False
            print("Au revoir")




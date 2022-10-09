def intro():
    bbygf = "le vrai Big Boss du YouTube game français, celui qui charbonne pour de vrai.\n" # \n = next line
    bbygf += "Le seul qui vous apprend VRAIMENT comment devenir libre pas comme les baltringues qui vendent du rêve."
    msg = "Apprenez la programmation avec Polymath Freeman"
    print(msg.upper())
    print(bbygf)
    print("Abonnez-vous, cliquez bande de S******".upper())


def string():
    print_fct = 'La fonction "print" est une fonction intégrée qui permet \n'
    print_fct += '"d\'imprimer" des chaînes de caractères à l\'écran'
    print(print_fct)
    escape = 'Le symbole backslash (contre-oblique) permet d\'échapper (annuler la fonction) un caractère'
    print(escape)
    frame = "Comme vous avez pu le voir une chaîne de caractères doit être encadrée par au choix :"
    print(frame)
    
    string_delimiters = {'" "', "' '", "''' '''", '""" """'}
    
    for string_delimiter in string_delimiters: print(string_delimiter, end = "|\t")
    print() # sert juste à aller à la ligne après la boucle (lire le commentaire ci-dessous bande de b*t*rds)
    # je modifie la sortie par défaut de la fonction print pour afficher une tabulation (espace horizontal)
    # au lieu d'aller à la ligne (comportement par défaut)
    
    hello = "Bonjour"
    print(f'La variable "hello" contient la valeur {hello}')
    triple_quote = """Une chaîne de caractères (string en anglais) précédée par la lettre 'f' 
permet d'évaluer des variables"""
    print(triple_quote)

def for_loop():
    for_keyword = "Le mot-clé \"for\" sert à effectuer une répétition d'instructions."
    print(for_keyword)
    digits_ex = "Par exemple pour afficher les 10 chiffres de 0 à 9 on peut écrire for i in range(10): print(i)"
    print(digits_ex)
    input("Appuyez sur la touche 'Entrée' pour déclencher la boucle...")
    for i in range(10): print(i)

def blocks():
    colon = "En programmation Python, le symbole ':' sert à indiquer le début d'un bloc d'instructions"
    print(colon)
    one_liner = "Lorsqu'il n'y a qu'une seule instruction il est possible de l'écrire à la suite sur la même ligne."
    print(one_liner)
    multiple_lines = "Lorsqu'il y a plusieurs instructions il faut indenter\n"
    multiple_lines += "(j'ai un clavier QWERTY d'où les embrouilles...)"
    print(multiple_lines)
    indent = "Indenter signifie décaler vers la droite (laisser une marge).\n"
    indent += "En général en Python il faut 4 espaces."
    print(indent)
    print("Exemples de blocs d'instructions")

def if_block():
    age = 16
    if age < 18:
        print("Vous êtes mineur")
        print("Donc vous ne pouvez pas voter (est-ce vraiment grave ?)")
        print("Vous ne pouvez pas conduire de voiture sans être accompagné par un adulte référent")
        print("Vous n'êtes pas totalement responsable de vos actes (voir la loi pour plus de détails)")
    print("Le mot-clé 'if' (si en anglais) sert à créer des structures de branchements (conditionnels)")

def while_loop():
    age = 16
    while age < 18:
        print("Vous êtes mineur")
        wait = f"Attendez encore {18 - age}"
        print(wait)
        age = age + 1 # ceci est 1 com pour dire on prend la valeur de la variable age et on lui ajoute 1 (mise à jour)
        # comme on met à jour la variable age au bout d'un moment sa valeur va dépasser 18
        # et on sortira de la boucle

def if_else_block():
    age = 18
    if age < 18: print("Vous êtes mineur")
    else: print("Vous êtes majeur")

def if_elif_else_block():
    age = 16
    if age < 16: print("Vous êtes un petit mineur")
    elif age < 18:
        print("Vous êtes mineur mais si vous voulez vous pouvez apprendre à conduire une voiture")
    else: print("Vous êtes majeur")
    
print("Organisons le code à l'aide de fonctions (regroupements de bouts de code)")
print('La fonction intégrée "input" sert à récupérer des saisies de la part de l\'utilisateur')

def main_function():
    menu = """
    1) Intro
    2) String (sans capuche)
    3) For loop
    4) Blocks 
    5) If blocks
    6) While Loop
    7) If else blocks
    8) If elif else blocks
    9) Play and use this code
    Q) Quit
    Your choice: """
    choice = True 
    while choice:
        choice = input(menu)
        if choice == '1': intro() # appel de la fonction
        elif choice == '2': string()
        elif choice == '3': for_loop()
        elif choice == '4': blocks()
        elif choice == '5': if_block()
        elif choice == '6': while_loop()
        elif choice == '7': if_else_block()
        elif choice == '8': if_elif_else_block()
        elif choice.upper() == 'Q': 
            choice = False
            print("Abonnez-vous, cliquez bande de S******".upper())
            print("Au revoir (pensez à Giscard en lisant ça)")
            print("Abonnez-vous, cliquez bande de S******".upper())
        elif choice == '9':
            hacker = "https://laurentgarnier.podia.com/comment-devenir-1-vrai-hacker"
            print(f"Allez récupérer ma formation GRATUITE sur :\n{hacker}")
            print("Abonnez-vous, cliquez bande de S******".upper())
        else: print("Vous devez choisir une option du menu sinon vous ne pourrez jamais quitter cet enfer !!!!!!")
        
main_function()
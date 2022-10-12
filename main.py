from create_html_skeleton import create_html_file, read_html_file


def main():
    choix = True
    menu = """
    1) Créer un fichier html
    2) Lire un fichier html
    Q) Quitter
    Votre choix : """
    while choix:
        choix = input(menu)
        if choix == '1': create_html_file()
        elif choix == '2':
            filename = input("Nom du fichier à lire : ")
            read_html_file(filename)
        elif choix.upper() == 'Q':
            choix = False
            print("Au revoir")
        else:
            print("Relisez le menu")
            print("Choisissez une option du menu")

main()


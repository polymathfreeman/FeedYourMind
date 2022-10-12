import body_of_html_page 


def header():
    html_header = '''\n\t<header>\n'''
    menu = """
    1) Titre de niveau h(n)
    Q) Quitter le menu du header
    Votre choix : """
    choix = True
    while choix:
        choix = input(menu)
        if choix == '1': 
            n = int(input("Niveau du titre h(n), n = "))
            html_header += "\t\t" + body_of_html_page.h(n)
        elif choix.upper() == 'Q': 
            choix = False
            html_header += "\t</header>\n\n"
    return html_header


import body_of_html_page  


def nav():
    html_nav = '''\n\t<nav>\n'''
    menu = """
    1) Titre de niveau h(n)
    2) Liste 
    3) Formulaire
    4) Lien URL
    5) Image 
    Q) Quitter le menu de navigation
    Votre choix : """
    choix = True
    while choix:
        choix = input(menu)
        if choix == '1': 
            n = int(input("Niveau du titre h(n), n = "))
            html_nav += "\t" + body_of_html_page.h(n)
        elif choix == '2': html_nav += body_of_html_page.choose_list()
        elif choix == '3': html_nav += body_of_html_page.forms()
        elif choix == '4': html_nav += body_of_html_page.a_url()
        elif choix == '5': html_nav += body_of_html_page.choose_img()
        elif choix.upper() == 'Q': 
            choix = False
            html_nav += "\t</nav>\n\n"
    return html_nav


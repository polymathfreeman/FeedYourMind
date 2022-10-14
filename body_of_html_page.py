from body_header import header
from body_nav import nav
from body_main import main


def h(n):
    hn = input(f"Titre de niveau h{n} = ")
    return f"\n\t<h{n}>{hn}</h{n}>\n"

def ul():
    result = "\t<ul>\n"
    nb_elts = int(input("Nombre d'éléments dans la liste non ordonnée nb_elts = "))
    for i in range(nb_elts):
        li = input(f"Il reste {nb_elts - i} éléments à ajouter. Élément à ajouter = ")
        result += f"\t\t<li>{li}</li>\n"
    result += "\t</ul>\n"
    return result


def ol():
    result = "\t<ol>\n"
    nb_elts = int(input("Nombre d'éléments dans la liste ordonnée nb_elts = "))
    for i in range(nb_elts):
        li = input(f"Élément numéro {i+1} = ")
        result += f"\t\t<li>{li}</li>\n"
    result += "\t</ol>\n"
    return result


def choose_list():
    liste = input("Liste ordonnée (Y) ou non ordonnée (N) : ")
    if liste.upper() == 'Y': return ol()
    elif liste.upper() == 'N': return ul()


def input_type(type_label):
    label_for = input("label for= ")
    inside_label = input("inside label = ")
    result = f'\t\t<label for="{label_for}"{inside_label}:</label><br>\n'
    id = input("id = ")
    name = input("name = ")
    result += f'\t\t<input type="{type_label}" id="{id}" name="{name}">\n\n'
    return result     
    

    
def labels():
    input_types = {
        'button','checkbox', "color", "date", "datetime-local", "email", "file",
        "hidden", "image", "month", "number", "password", "radio", "input_range",
        "reset", "search", "submit", "tel", "text", "time", "url", "week"
    }
    look_at_types = input("Do you want to look at what types are available? Yes|No ")
    if look_at_types in {"yes", "YES", 'y', 'Y'}:
        for it in input_types: print(it)
        w3schools = "https://www.w3schools.com/html/html_form_input_types.asp"
        mdn = "https://developer.mozilla.org/en-US/docs/Learn/Forms/HTML5_input_types"
        docs = {mdn, w3schools}
        print("More details on:")
        for help in docs: print(help)
            
    it = input("Input type = ")
    if it in input_types:
        return input_type(type_label=it)
    else:
        while it not in input_types:
            print("Choose from that list")
            for it in input_types: print(it)
            it = input("Input type = ")
            if it in input_types: return input_type(type_label=it)


def forms():
    result = '\t<form action="/action_page.php">\n'
    cond = True
    while cond:
        choix = input("Do you want to add a label/input type? Y|N ")
        if choix in {'y', 'Y', "yes", "Yes"}: result+= labels()
        else: cond = False
    result += '\t</form>\n'
    return result 





def a_url(img=False):
    html_a = """
\t<a\n\thref="""
    href = input("href = ")
    html_a += href + " target=_blank>\n\t"
    if img: visible = img_tag()
    else: visible = input("Texte visible : ")
    html_a += visible + "\n\t</a>\n"
    return html_a



def paragraph():
    html_p = """
\t<p>\n"""
    continuer = True
    while continuer:
        ligne = input("Écrivez une linge (80 caractères max) : ")
        html_p += "\t\t" + ligne + "\n"
        breakline = input("Voulez-vous que le texte aille à la ligne ? (Y|N) ")
        if breakline == 'Y': html_p += "\t\t<br>\n"
        url = input("Voulez-vous insérer un lien url ? Oui|Non ")
        if url in {'o', 'O', 'oui', 'Oui'}: html_p += a_url()
        continuer = input("Continuer ? Oui|Non ")
        if continuer in {'n', 'N', 'non', 'Non'}:
            continuer = False
            print("Fin du paragraphe.")
            html_p += "\t</p>\n"
    return html_p



def img_tag():
    html_img = '''
\t<img src='''
    src = input("src = ")
    html_img += src + ' '
    alt = input("alt = ")
    html_img += alt + "/>\n"
    return html_img


def choose_img():
    link = input("Image avec (Y) ou sans (N) lien URL : ")
    if link.upper() == 'Y': return a_url(img=True)
    elif link.upper() == 'N': return img_tag()
    

def footer():
    copyleft = """
    <footer>
      <p>©Copyleft until 2140 by Satoshi Nakamoto. All rights reversed.</p>
    </footer>
    """
    return copyleft
    
def body():
    html_body = '''
\t<body>
'''
    menu = """
    1) Header
    2) Nav
    3) Main
    4) Footer
    Q) Quitter
    Votre choix : """
    choix = True
    while choix:
        choix = input(menu)
        if choix == '1': html_body += header()
        elif choix == '2': html_body += nav()
        elif choix == '3': html_body += main()
        elif choix == '4': html_body += footer()
        elif choix.upper() == 'Q': 
            choix = False
            html_body += "</body>\n"
    return html_body



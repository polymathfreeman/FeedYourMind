html_template = '''<!DOCTYPE html>
<html>
'''

def head():
    titre = input("Saisir le titre de votre page web : ")
    html_head = '''
\t<head>
\t\t<meta charset="utf-8">
\t\t<meta name="viewport" content="width=device-width">
'''
    html_head += f'\t\t<title>{titre}</title>\n'
    html_head += '\t\t<link href="style.css" rel="stylesheet" type="text/css" />\n'
    html_head += '\t</head>'
    return html_head

html_template += head()

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

def audio():
    result = '\t<audio controls autoplay muted>\n'
    audio_file_name = input("Nom du fichier audio : ")
    point_index = audio_file_name.index('.')
    audio_type = audio_file_name[point_index + 1:]
    result += f'\t\t<source src="{audio_file_name}" type="audio/{audio_type}">\n'
    result += '\t\tYour browser does not support the audio element.\n'
    result += '\t</audio>\n'
    return result

def video():
    width = int(input("width = "))
    height = int(input("height = "))
    result = f'\t<video width="{width}" height="{height}" autoplay muted>\n'
    video_file_name = input("Nom du fichier vidéo : ")
    point_index = video_file_name.index('.')
    video_type = video_file_name[point_index + 1:]
    result += f'\t\t<source src="{video_file_name}" type="video/{video_type}">\n'
    result += '\t\tYour browser does not support the video tag.\n'
    result += '\t</video>\n'
    return result

def header():
    html_header = '''
\t<header>\n
    '''
    menu = """
    1) Titre de niveau h(n)
    Q) Quitter
    Votre choix : """
    choix = True
    while choix:
        choix = input(menu)
        if choix == '1': 
            n = int(input("Niveau du titre h(n), n = "))
            html_header += "\t" + h(n)
        elif choix.upper() == 'Q': 
            choix = False
            html_header += "\t</header>\n\n"
    return html_header

def nav():
    html_nav = '''
\t<nav>\n
    '''
    menu = """
    1) Titre de niveau h(n)
    2) Liste non ordonnée ul
    3) Liste ordonnée ol
    4) Formulaire
    Q) Quitter
    Votre choix : """
    choix = True
    while choix:
        choix = input(menu)
        if choix == '1': 
            n = int(input("Niveau du titre h(n), n = "))
            html_nav += "\t" + h(n)
        elif choix == '2': html_nav += ul()
        elif choix == '3': html_nav += ol()
        elif choix == '4': html_nav += forms()
        elif choix.upper() == 'Q': 
            choix = False
            html_nav += "\t</nav>\n\n"
    return html_nav


def a_url(img=False):
    html_a = """
\t<a\n\thref="""
    href = input("href = ")
    html_a += href + " target=_blank>\n\t"
    if img: visible = img()
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
        url = input("Voulez-vous insérer un lien url ? Oui|Non ")
        if url in {'o', 'O', 'oui', 'Oui'}: html_p += a_url()
        continuer = input("Continuer ? Oui|Non ")
        if continuer in {'n', 'N', 'non', 'Non'}:
            continuer = False
            print("Fin du paragraphe.")
            html_p += "\t</p>\n"
    return html_p


def img():
    html_img = '''
\t<img src='''
    src = input("src = ")
    html_img += src + ' '
    alt = input("alt = ")
    html_img += alt + "/>\n"
    return html_img


    
def article_section(a_or_s):
    menu = """
    1) Titre de niveau h(n)
    """
    
    if a_or_s == "article":
        html_a_or_s = '''
\t<article>\n
    '''
        menu += """
        2) section"""
    elif a_or_s == "section":
        html_a_or_s = '''
\t<section>\n
    ''' 
        menu += """
        2) article"""
        
    menu += """
    3) Paragraph p
    4) Lien URL a
    5) Image (sans lien URL) img
    6) Image (avec lien URL) img
    7) Audio
    8) Vidéo
    9) Formulaire
    Q) Quitter
    Votre choix : """
    choix = True
    while choix:
        choix = input(menu)
        if choix == '1': 
            n = int(input("Niveau du titre h(n), n = "))
            html_a_or_s += h(n)
        elif choix == '2': article_section()
        elif choix == '3': html_a_or_s += paragraph()
        elif choix == '4': html_a_or_s += a_url()
        elif choix == '5': html_a_or_s += img()
        elif choix == '6': html_a_or_s += a_url(img=True)
        elif choix == '7': html_a_or_s += audio()
        elif choix == '8': html_a_or_s += video()
        elif choix == '9': html_a_or_s += forms()
        elif choix.upper() == 'Q': 
            choix = False
            if a_or_s == "article": html_a_or_s += "\t</article>\n\n"
            elif a_or_s == "section": html_a_or_s += "\t</section>\n\n"
    return html_a_or_s
    

def aside():
    html_aside = """
\t<aside>\n
"""

    menu = """
    1) Titre de niveau h(n)
    2) Paragraph p
    3) Lien URL a
    4) Image (sans lien URL) img
    5) Image (avec lien URL) img
    6) Audio
    7) Vidéo
    8) Formulaire
    Q) Quitter
    Votre choix : """
    choix = True
    while choix:
        choix = input(menu)
        if choix == '1': 
            n = int(input("Niveau du titre h(n), n = "))
            html_aside += h(n)
        elif choix == '2': html_aside += paragraph()
        elif choix == '3': html_aside += a_url()
        elif choix == '4': html_aside += img()
        elif choix == '5': html_aside += a_url(img=True)
        elif choix == '6': html_aside += audio()
        elif choix == '7': html_aside += video()
        elif choix == '8': html_aside += forms()
        elif choix.upper() == 'Q': 
            choix = False
            html_aside += "\t</aside>\n\n"
    return html_aside
    
def main():
    html_main = '''
\t<main>\n
    '''
    menu = """
    1) Titre de niveau h(n)
    2) article
    3) section
    4) aside
    Q) Quitter
    Votre choix : """
    choix = True
    while choix:
        choix = input(menu)
        if choix == '1': 
            n = int(input("Niveau du titre h(n), n = "))
            html_main += "\t" + h(n)
        elif choix in '2': 
            a_or_s = "article"
            html_main += article_section(a_or_s)
        elif choix in '3': 
            a_or_s = "section"
            html_main += article_section(a_or_s)
        elif choix == '4': html_main += aside()
        elif choix.upper() == 'Q': 
            choix = False
            html_main += "\t</main>\n\n"
    return html_main


    
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
        elif choix.upper() == 'Q': 
            choix = False
            html_body += "</body>\n"
    return html_body

html_template += body() + "\n</html>\n"
print(html_template)


with open('index.html', 'w') as f:
    f.write(html_template)

with open('index.html', 'r') as f:
    print(f.read())



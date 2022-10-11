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

def labels():
    label_name = input("Label's name: ")
    label_value = input("Label's value")
    result = f'\t\t<label for="{label_name}">{label_value}:</label><br>\n'
    input_types = {
        'button': input_button(),
        'checkbox': input_checkbox(),
        "color": input_color(),
        "date": input_date(),
        "datetime-local": input_datetime(),
        "email": input_email(),
        "file": input_file(),
        "hidden": input_hidden(),
        "image": input_image(),
        "month": input_month(),
        "number": input_number(),
        "password": input_password(),
        "radio": input_radio(),
        "input_range": input_range(),
        "reset": input_reset(),
        "search": input_search(),
        "submit": input_submit(),
        "tel": input_tel(),
        "text": input_text(),
        "time": input_time(),
        "url": input_url(),
        "week": input_week()
    }
    look_at_types = input("Do you want to look at what types are available? Yes|No ")
    if look_at_types in {"yes", "YES", 'y', 'Y'}:
        for k, v in input_types: print(k, v)
            
    input_type = input("Input type = ")
    result += f'\t\t<input type="{input_type}" id="{label_name}" name="{label_name}" value="{label_value}"><br>\n'
    
def forms():
    result = '\t<form action="/action_page.php">\n'
    result+= labels()
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
    
def body():
    html_body = '''
\t<body>
'''
    menu = """
    1) Titre de niveau h(n)
    2) Liste non ordonnée ul
    3) Liste ordonnée ol
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
            html_body += h(n)
        elif choix == '2': html_body += ul()
        elif choix == '3': html_body += ol()
        elif choix == '7': html_body += audio()
        elif choix == '8': html_body += video()    
        elif choix.upper() == 'Q': 
            choix = False
            html_body += "</body>\n</html>"
    return html_body

html_template += body()
print(html_template)


with open('index.html', 'w') as f:
    f.write(html_template)

with open('index.html', 'r') as f:
    print(f.read())



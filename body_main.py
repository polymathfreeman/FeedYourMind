import body_of_html_page  


def article_section(a_or_s):
    menu = """
    1) Titre de niveau h(n)\n"""
    
    if a_or_s == "article":
        html_a_or_s = '''\n\t<article>\n'''
        menu += """2) section\n"""
    elif a_or_s == "section":
        html_a_or_s = '''\n\t\t<section>\n''' 
        menu += """2) article\n"""
        
    menu += """
    3) Paragraph p
    4) Lien URL a
    5) Image 
    6) Liste
    7) Audio
    8) Vidéo
    9) Formulaire
    Q) Quitter le menu de cet"""
    if a_or_s == "article": menu += f" {a_or_s}\n"
    elif a_or_s == "section": menu += f"tte {a_or_s}\n"
    menu += "Votre choix : "
    
    choix = True
    while choix:
        choix = input(menu)
        if choix == '1': 
            n = int(input("Niveau du titre h(n), n = "))
            html_a_or_s += body_of_html_page.h(n)
        elif choix == '2': body_of_html_page.article_section()
        elif choix == '3': html_a_or_s += body_of_html_page.paragraph()
        elif choix == '4': html_a_or_s += body_of_html_page.a_url()
        elif choix == '5': html_a_or_s += body_of_html_page.choose_img()
        elif choix == '6': html_a_or_s += body_of_html_page.choose_list()    
        elif choix == '7': html_a_or_s += body_of_html_page.audio()
        elif choix == '8': html_a_or_s += body_of_html_page.video()
        elif choix == '9': html_a_or_s += body_of_html_page.forms()
        elif choix.upper() == 'Q': 
            choix = False
            if a_or_s == "article": html_a_or_s += "\t</article>\n\n"
            elif a_or_s == "section": html_a_or_s += "\t</section>\n\n"
    return html_a_or_s
    

def aside():
    html_aside = """\n\t<aside>\n"""

    menu = """
    1) Titre de niveau h(n)
    2) Paragraph p
    3) Lien URL a
    4) Image 
    5) Liste
    6) Audio
    7) Vidéo
    8) Formulaire
    Q) Quitter le menu de cette balise <aside>
    Votre choix : """
    choix = True
    while choix:
        choix = input(menu)
        if choix == '1': 
            n = int(input("Niveau du titre h(n), n = "))
            html_aside += body_of_html_page.h(n)
        elif choix == '2': html_aside += body_of_html_page.paragraph()
        elif choix == '3': html_aside += body_of_html_page.a_url()
        elif choix == '4': html_aside += body_of_html_page.choose_img()
        elif choix == '5': html_aside += body_of_html_page.choose_list()
        elif choix == '6': html_aside += audio()
        elif choix == '7': html_aside += video()
        elif choix == '8': html_aside += body_of_html_page.forms()
        elif choix.upper() == 'Q': 
            choix = False
            html_aside += "\t</aside>\n\n"
    return html_aside



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



    
def main():
    html_main = '''\n\t\t<main>\n'''
    menu = """
    1) Titre de niveau h(n)
    2) article
    3) section
    4) aside
    Q) Quitter le menu du bloc <main>
    Votre choix : """
    choix = True
    while choix:
        choix = input(menu)
        if choix == '1': 
            n = int(input("Niveau du titre h(n), n = "))
            html_main += "\t" + body_of_html_page.h(n)
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


def doc_type(): return '''<!DOCTYPE html>\n\t<html>\n'''

def head():
    welcome = "Bienvenue dans la partie <head> de votre page HTML"
    print(welcome.upper())
    
    html_head = '''\t<head>
\t\t<meta charset="utf-8">
\t\t<meta name="viewport" content="width=device-width">\n'''
    
    titre = input("Saisir le titre de votre page web : ")
    html_head += f'\t\t<title>{titre}</title>\n'
    html_head += '\t\t<link href="style.css" rel="stylesheet" type="text/css" />\n'
    html_head += '\t</head>\n'
    return html_head



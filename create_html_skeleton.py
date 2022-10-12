import head_of_html_page 
import body_of_html_page  

#html_template += body_of_html_page.body() + "\n</html>\n"
#print(html_template)

def create_html_file():
    print("Par défaut le fichier créé s'appellera index.html")
    filename = input("Voulez-vous modifier le nom du fichier ? (Y|N) ")
    if filename.upper() == 'Y': filename = input("Nom du fichier : ")
    else: filename = "index.html"
    html_template = head_of_html_page.doc_type()
    html_template += head_of_html_page.head()
    html_template += body_of_html_page.body() + "\n</html>\n"
    print(html_template)
    
    with open(filename, 'w') as f:
        f.write(html_template)

    print("New file has been created".upper())
    print("Open index.html to check the code")

def read_html_file(filename="index.html"):
    with open(filename, 'r') as f:
        print(f.read())



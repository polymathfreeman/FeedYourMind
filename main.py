def get_cyrillic_unicode():
    L1, l1 = '\u0410', '\u0430'
    L2, l2 = '\u0411', '\u0431'
    L3, l3 = '\u0412', '\u0432'
    L4, l4 = '\u0413', '\u0433'
    L5, l5 = '\u0414', '\u0434'
    L6, l6 = '\u0415', '\u0435'
    L7, l7 = '\u0416', '\u0436'
    L8, l8 = '\u0417', '\u0437'
    L9, l9 = '\u0418', '\u0438'
    L10, l10 = '\u0419', '\u0439'
    L11, l11 = '\u041A', '\u043A'
    L12, l12 = '\u041B', '\u043B'
    L13, l13 = '\u041C', '\u043C'
    L14, l14 = '\u041D', '\u043D'
    L15, l15 = '\u041E', '\u043E'
    L16, l16 = '\u041F', '\u043F'
    L17, l17 = '\u0420', '\u0440'
    L18, l18 = '\u0421', '\u0441'
    L19, l19 = '\u0422', '\u0442'
    L20, l20 = '\u0423', '\u0443'
    L21, l21 = '\u0424', '\u0444'
    L22, l22 = '\u0425', '\u0445'
    L23, l23 = '\u0426', '\u0446'
    L24, l24 = '\u0427', '\u0447'
    L25, l25 = '\u0429', '\u0449'
    L26, l26 = '\u042A', '\u044A'
    L27, l27 = '\u042C', '\u044C'
    L28, l28 = '\u042D', '\u044D'
    L29, l29 = '\u042E', '\u044E'
    L30, l30 = '\u042F', '\u044F'
    
    maj = (
        L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, 
        L11, L12, L13, L14, L15, L16, L17, L18, L19, L20, 
        L21, L22, L23, L24, L25, L26, L27, L28, L29, L30
    )
    
    minu = (
        l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, 
        l11, l12, l13, l14, l15, l16, l17, l18, l19, l20, 
        l21, l22, l23, l24, l25, l26, l27, l28, l29, l30
    )
    
    return maj, minu


    
def print_cyrllic_alphabet(maj, minu):
    print("=" * 40)
    print("Alphabet cyrillique Russe")
    print("=" * 40)
    print("\nMajuscules")
    print("-" * 40)
    for L in range(len(maj)): print(L, ':', maj[L])
    print("\nMinuscules")
    print("-" * 40)
    for l in range(len(minu)): print(l, ':', minu[l])



def end_page(page_name):
    print(f"{page_name} has been created")
    input("Hit 'Enter' to proceed...")



def xelatex_preambule(filename='alpha.tex'):
    print("Creating XeLaTeX preambule...")
    
    with open(filename, 'w') as alphabetFile:    
        alphabetFile.write('\\documentclass[12pt,a4paper]{article}\n')
        alphabetFile.write('\\usepackage{fontspec}\n')
        alphabetFile.write('\\usepackage{xunicode}\n')
        alphabetFile.write(r'\newfontfamily\cyrillicfont{Times New Roman}')
        alphabetFile.write('\n\\usepackage{polyglossia}\n')
        alphabetFile.write('\\usepackage{xltxtra}\n')
        alphabetFile.write('\\setmainlanguage{french}\n')
        alphabetFile.write('\\setotherlanguages{russian, english}\n')
        alphabetFile.write('\\usepackage{hyperref}\n')
        alphabetFile.write('\\usepackage{graphics}\n')

        hypersetup = '\\hypersetup{colorlinks=true, '
        hypersetup += 'citecolor=electricblue, '
        hypersetup += 'filecolor=electricblue, '
        hypersetup += 'linkcolor=red,urlcolor=blue}\n'
        alphabetFile.write(hypersetup)

        alphabetFile.write('\\author{Laurent Garnier}\n')
        alphabetFile.write('\\date{}\n')

        title = 'Alphabet cyrillique Russe '
        title += '\\textrussian{русский}\\\ '
        title += '\\title{avec Python 3 et \\XeLaTeX}\n'
        alphabetFile.write(title)

    end_page(page_name="Preambule")


def create_title_page(filename='alpha.tex'):
    print("Creating title page...")
    
    with open(filename, 'a') as alphabetFile:
        alphabetFile.write('\n\\begin{titlepage}\n')
        alphabetFile.write('\n\\begin{center}\n')
        
        title = '\n{\Large '
        title += '{\sc Alphabet cyrillique Russe\par '
        title += 'avec Python 3\par et \\XeLaTeX} \par}'
        alphabetFile.write(title)
    
        alphabetFile.write('\n\\vspace{2cm}')
        alphabetFile.write('\n\\end{center}\n')
        alphabetFile.write('\\newpage\n')

        #{\Large Introduction To French Slang \par}
        alphabetFile.write('\n\\vspace{2cm}\n')

        alphabetFile.write('\n\\begin{center}\n')
        alphabetFile.write('\nBY\n')

        author = '\n{\Large Laurent \\textsc{Garnier} '
        author += '\par}\n'
        alphabetFile.write(author)
    
        alphabetFile.write('\n\\vspace{2cm}\n')

        polyglot = '{\sc Visit my blog on languages:}\n '
        polyglot += '\\url{www.polyglothuman.fr}\\par\n'
        alphabetFile.write(polyglot)

        gpr = '{\sc Visit my blog on Russian:}\n '
        gpr += '\\url{www.govoritparoussky.fr}\\par\n'
        alphabetFile.write(gpr)
        alphabetFile.write('\n\\end{center}\n')
        alphabetFile.write('\\newpage\n')

        alphabetFile.write('\n\\begin{center}\n')
        
        lang_sci = '\n {\sc Visit my YouTube channel:} \n '
        lang_sci = '\\url{http://bit.ly/LanguageScience}\\par\n'
        alphabetFile.write(lang_sci)

        russian_playlist = '\n {\sc Visit my playlist on Russian:} \n '
        russian_playlist = '\\url{http://bit.ly/LearnRussianWithMe}\\par\n'
        alphabetFile.write(russian_playlist)
        alphabetFile.write('\n\\end{center}\n')
        alphabetFile.write('\n\\end{titlepage}\n')

    end_page(page_name="Title page")

def section_alpha(filename='alpha.tex'):
    print("Creating alphabet section...")
    
    with open(filename, 'a') as alphabetFile:
        alphabetFile.write('\\section{Alphabet cyrillique russe}\n')
        alphabetFile.write(r'\begin{center}')
        alphabetFile.write('\n \\begin{tabular}{c|c|c}\n')
        alphabetFile.write(r'    Indice & Lettre Majuscule & lettre minuscule \\')
        alphabetFile.write('\n')
        alphabetFile.write(r'    \hline')
        alphabetFile.write('\n')

        maj, minu = get_cyrillic_unicode()
        for L in range(len(maj)):
            alphabetFile.write('    ')
            alphabetFile.write(str(L))
            alphabetFile.write(' & ')
            alphabetFile.write(r'\textrussian{')
            alphabetFile.write(maj[L])
            alphabetFile.write('} & ')
            alphabetFile.write(r'\textrussian{')
            alphabetFile.write(minu[L])
            alphabetFile.write('}')
            alphabetFile.write(r' \\')
            alphabetFile.write('\n')
    
        alphabetFile.write('  \\end{tabular}\n')
        alphabetFile.write(r'\end{center}')
        alphabetFile.write('\n')

    end_page(page_name="Alphabet section")

def section_blogs(filename='alpha.tex'):
    print("Creating blogs section...")
    
    with open(filename, 'a') as alphabetFile:    
        alphabetFile.write(r'\section{Retrouvez les détails et les sons sur mon blog}')
        alphabetFile.write('\n')
        article = '{\Large '
        article += 'Allez consulter cet article de blog '
        article += 'dans lequel je détaille la logique de '
        article += 'l\'alphabet cyrillique russe :\par}\n'
        alphabetFile.write(article)
        alphabetFile.write('\\begin{center}\n')
        url = '\\url{https://govoritparoussky.fr/'
        url += 'comment-apprendre-lalphabet-russe-'
        url += 'meme-quand-on-est-debutant/}\n'
        alphabetFile.write(url)
        alphabetFile.write('\\end{center}\n')

    end_page(page_name="Blogs section")


def section_examples(filename='alpha.tex'):
    print("Creating example section...")
    
    with open(filename, 'a') as alphabetFile:
        alphabetFile.write(r'\section{Quelques exemples}')
        alphabetFile.write('\n')
        alphabetFile.write('\\begin{description}\n')
        alphabetFile.write(r'\item[russe]\textrussian{а ты говоришь по русски?}')
        alphabetFile.write('\n')
        alphabetFile.write('\\item[français]Parles-tu Russe ?\n')
        alphabetFile.write(r'\item[russe]\textrussian{Я немного говорю по русски}')
        alphabetFile.write('\n')
        alphabetFile.write('\item[français] Je parle un peu russe\n')
        alphabetFile.write('\\end{description}\n')
    
    end_page(page_name="Example section")


def generate_xelatex_doc(filename='alpha.tex'):
    
    xelatex_preambule(filename)
    
    with open(filename, 'a') as alphabetFile:    
        alphabetFile.write('\n\\begin{document}\n')
        
    create_title_page(filename)

    with open(filename, 'a') as alphabetFile:
        alphabetFile.write('\n\\tableofcontents\n')
    
    section_alpha(filename)
    section_blogs(filename)
    section_examples(filename)
        
    with open(filename, 'a') as alphabetFile:
        alphabetFile.write('\\end{document}')


def print_file_in_console(filename='alpha.tex'):
    alphabetFile = open('alpha.tex')
    content = alphabetFile.read()
    print(content)
    alphabetFile.close()


def test():
    filename = input("XeLaTeX file name= ")
    generate_xelatex_doc(filename)
    overleaf = "https://www.overleaf.com/"
    print(f"Visit {overleaf} to compile XeLaTeX into PDF")

test()
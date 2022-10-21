import pandas as pd
normal_cdf_table = 'https://fr.wikipedia.org/wiki/Loi_normale'
choix = input(f"Watch this website:\n{normal_cdf_table}\nDo you want to scrap this normal cumulative function table? ")
if choix.upper() in {'Y', "YES", 'O', "OUI"}:
    loi_normale = pd.read_html(normal_cdf_table)
    print(len(loi_normale))
    print(loi_normale[1])


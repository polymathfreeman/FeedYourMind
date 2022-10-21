import spacy
import requests
from bs4 import BeautifulSoup 
from collections import Counter

print("spacy version:", spacy.__version__)
nlp = spacy.load("en_core_web_sm")
response = requests.get("http://lite.cnn.com/en")
soup = BeautifulSoup(response.text, "html.parser")

[s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
text = soup.getText()
doc = nlp(text)

names = []
for ent in doc.ents:
    if ent.label_ == "PERSON":
        names.append(ent.lemma_)


print("These people are in the headlines today")
print(Counter(names).most_common(10))



import spacy
nlp = spacy.load("en_core_web_sm")
from os import listdir
from os.path import isfile, join
import re
mypath = "Data"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
counter = 1
for x in onlyfiles:
    print(counter)
    counter+=1
    out = "Taged"
    out = join(out, x)
    out = open(out, 'w')
    mypath2 = join(mypath, x)
    with open(mypath2, 'r') as f1:
        content = f1.readlines()
    s = ""
    for y in content:
        s+=y
    doc = nlp(s)
    s = re.sub(r'http\S+', '', s)
    s2=""
    for k in s.split("\n"):
        s2 +=(re.sub(r"[^a-zA-Z0-9]+", ' ', k))
    doc = nlp(s2)
    for X in doc.ents:
        out.write(X.text + ' ')
    out.close()
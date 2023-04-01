
import pandas as pd
with open("appalti.txt", "r") as f:
    lines = f.readlines()

elenco = []

libri = 0
capitoli = 0
testo_articoli = []
articolo = []

for enumed_line, line in enumerate(lines):
    if "LIBRO" in line:
        libro = line.replace("\n", " ")
        libri += 1
        capitoli = 0
    if "Articolo" in line:
        capitoli += 1
        elenco.append([libro, line.replace("\n", " "), lines[enumed_line + 1].replace("\n", " "), f"{libri:02}.{capitoli:02}",  capitoli])
        testo_articoli.append(articolo)
        articolo = []
    articolo.append(line.replace("\n", " "))

elenco = pd.DataFrame(elenco)
testo = pd.Series(testo_articoli[1:])

elenco.columns = ["libro", "articolo", "testo", "codice", "capitolo"]
risultato = pd.concat([elenco, testo], axis=1)

risultato.to_csv("codice_appalti.csv", index=False, sep="|")
risultato.to_json("codice_appalti.json", orient="records", lines=True)
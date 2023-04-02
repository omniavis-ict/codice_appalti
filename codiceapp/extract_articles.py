
import pandas as pd
import re


def remove_page_number_and_other_noise_text(lines)-> list:
    for line in lines:
        # if find string start with schema like —  1  — with regex, remove it
        if "Supplemento ordinario n. 12/L  alla GAZZETTA UFFICIALE Serie generale - n. 77 31-3-2023" in line:

            # print(line)
            lines.remove(line)
            # print("removed — n — line")

    print(len(lines))

    for line in lines:
        # if line contains only spaces, remove it
        if ' \n' == line:
            # print(line)
            lines.remove(line)
            # print("removed spaces line")
    return lines


def extract_articles(lines):
    elenco = []

    libri = 0
    capitoli = 0
    testo_articoli = []
    articolo = []

    for enumed_line, line in enumerate(lines):
        if "LIBRO" in line:
            libro = line.replace("\n", "")
            libri += 1
            capitoli = 0
        if "Articolo" in line:
            capitoli += 1
            nArticolo = line.replace("\n", "").replace(".", "").strip()
            titoloArticolo = lines[enumed_line + 1].replace("\n", "").strip()
            elenco.append([libro, nArticolo, titoloArticolo, f"{libri:02}.{capitoli:02}.", f"{libri:02}.{capitoli:02}. {nArticolo.strip()} - {titoloArticolo.strip()}" ])
            testo_articoli.append(articolo)
            articolo = []
        articolo.append(line.replace("\n", " ").strip())
    return elenco, testo_articoli


def export(elenco, testo_articoli):
    elenco = pd.DataFrame(elenco)
    testo = pd.Series(testo_articoli[1:])

    elenco.columns = ["libro", "articolo", "testo", "codice", "capitolo"]
    risultato = pd.concat([elenco, testo], axis=1)

    risultato.to_csv("codice_appalti.csv", index=False, sep="|")
    risultato.to_json("codice_appalti.json", orient="records", lines=True)
    risultato.to_excel("codice_appalti.xlsx", index=False)



if __name__ == "__main__":
    elenco, testo_articoli = extract_articles(lines)

    export(elenco, testo_articoli)

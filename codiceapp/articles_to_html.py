import pandas as pd
import json


with open("codice_appalti.json", "r") as f:
    data = pd.read_json(f, lines=True)


html = []

for index, row in data.iterrows():
    # access data using column names
    try:
        html.append(f"<h2>{row['capitolo']}</h2>, <p>{row['0'][2]}</p>")
    except:
        html.append(f"<h2>{row['capitolo']}</h2>")

print(html[0:3])
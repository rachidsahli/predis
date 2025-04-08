import requests
import pandas as pd

# URL
API_URL = "https://data.enedis.fr/api/records/1.0/search/"

# Params de la requête
params = {
    "dataset": "bilan-electrique-demi-heure",
    "rows": 100,
    "sort": "horodate"
}

# Interrogation de l'API
def get_data():
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        records = [record["fields"] for record in data["records"]]
        return pd.DataFrame(records)
    else:
        print(f"Erreur API : {response.status_code}")
        return None

# Head
df = get_data()
if df is not None:
    print(df.head())

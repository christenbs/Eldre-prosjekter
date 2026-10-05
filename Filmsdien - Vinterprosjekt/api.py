import os

import requests as req

def søk_etter_filmer(søk):
    api_key = os.environ.get("OMDB_API_KEY")
    if not api_key:
        raise RuntimeError("Set the OMDB_API_KEY environment variable to search for movies.")

    resultat = req.get(
        "https://www.omdbapi.com/",
        params={"i": "tt3896198", "apikey": api_key, "s": søk},
        headers={"User-Agent": "Christen"},
        timeout=10,
    )
    data = resultat.json()
    svar = data["Search"]
    return svar

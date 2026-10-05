# Filmsiden

# En side som representerer filmer fra IMDB topp 250 og TMDBs api

## Kjøre appen

Opprett et virtuelt miljø, aktiver det og installer avhengighetene:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Set `OMDB_API_KEY` in your shell before searching for movies. Get a key from
[OMDb](https://www.omdbapi.com/apikey.aspx); do not commit the key to the repository.

```sh
export OMDB_API_KEY="your-api-key"
```

Start deretter Flask fra prosjektmappen:

```sh
flask run
```

Alternativt kan appen startes med `python app.py`.

## Søkefunksjon
Det kan søkes etter filmer fra TMDBs api

## Anbefalt
Bruekren kan se anbefalte filmer fra IMDBs topp 250 liste

## Ratingsystem
På hjemmesiden kan brukeren lage sin egen toppliste fra IMDBs topp 250 liste<br>
Ved å trykke på knappen (pil opp), øker filmens poeng med 1. Deretter rangeres filmene ut ifra gitt poeng

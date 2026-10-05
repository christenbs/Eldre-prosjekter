from flask import Flask, jsonify, render_template, request, url_for
from random import randint, sample
from favoritt import Favoritt

app = Flask(__name__)

from jsonapp import json_filmer
filmer = json_filmer()

from api import søk_etter_filmer
søkeliste = []

def tilfeldig_3nr():
    nummerliste = []
    while len(nummerliste) < 3:
        tall = randint(0, 249)
        if tall not in nummerliste:
            nummerliste.append(tall)
    return nummerliste

def tilfeldig_2nr():
    return sample(range(len(filmer)), 2)

def hent_tilfeldige_filmer(unntatt=()):
    unntatte_navn = set(unntatt)
    kandidater = [film for film in filmer if film["navn"] not in unntatte_navn]
    return sample(kandidater, 2)

favoritter = []
for film in filmer:
    ny_favoritt = Favoritt(film["navn"])
    favoritter.append(ny_favoritt)

def øk_favorittpoeng(filmnavn):
    for film in favoritter:
        if film._navn == filmnavn:
            film.øk_poeng()
            return film.hent_poeng()
    return None

def hent_favorittliste():
    return sorted(
        (
            {"navn": film.hent_navn(), "poeng": film.hent_poeng()}
            for film in favoritter
            if film.hent_poeng() > 0
        ),
        key=lambda film: film["poeng"],
        reverse=True,
    )

@app.route("/")
def rute_index():
    tilfeldig = tilfeldig_2nr()
    valgte_filmer = [filmer[nummer] for nummer in tilfeldig]
    return render_template(
        "index.html",
        valgte_filmer=valgte_filmer,
        favorittpoeng={film.hent_navn(): film.hent_poeng() for film in favoritter},
        favoritter=hent_favorittliste(),
    )

@app.route("/sok", methods=["GET", "POST"])
def rute_sok():
    try:
        if request.method == "POST":
            svar = request.form["sok"]
            filmer = søk_etter_filmer(svar)
            søkeliste.clear()
            for film in filmer:
                søkeliste.append(film)
        return render_template("sok.html", søkeliste=søkeliste)
    except:
        return render_template("error.html")

@app.route("/anbefalt")
def rute_anbefalt():
    anbefalt_nummer = tilfeldig_3nr()
    return render_template("anbefalt.html", filmer=filmer, anbefalt_nummer=anbefalt_nummer)

@app.route("/øk-favorittpoeng/<filmnavn>", methods=["POST"])
def rute_øk_faovrittpoeng(filmnavn):
    poeng = øk_favorittpoeng(filmnavn)
    if poeng is None:
        return jsonify({"error": "Filmen ble ikke funnet."}), 404
    gjeldende_filmer = request.form.getlist("current_films")
    neste_filmer = hent_tilfeldige_filmer(unntatt=gjeldende_filmer)
    return jsonify(
        {
            "favoritter": hent_favorittliste(),
            "filmer": [
                {
                    "navn": film["navn"],
                    "bilde": film["bilde"],
                    "poeng": next(
                        favoritt.hent_poeng()
                        for favoritt in favoritter
                        if favoritt.hent_navn() == film["navn"]
                    ),
                    "vote_url": url_for(
                        "rute_øk_faovrittpoeng", filmnavn=film["navn"]
                    ),
                }
                for film in neste_filmer
            ],
        }
    )

if __name__ == "__main__":
    app.run(debug=True)
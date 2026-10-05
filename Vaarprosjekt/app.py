from flask import Flask, render_template
import json

app = Flask(__name__)

fil_forere = open("json/forere.json")
forere = json.load(fil_forere)

fil_lag = open("json/lag.json")
lag = json.load(fil_lag)

fil_baner = open("json/baner.json")
baner = json.load(fil_baner)

sainz = dict(list(forere.items())[3:4])

favorittForere = []
favorittBaner = []
favorittLag = []

@app.route("/")
def rute_index():
    return render_template("index.html", forer=forere, sainz=sainz)

@app.route("/forerene")
def rute_forerene():
    return render_template("forerene.html", forere=forere, favoritter=favorittForere)

@app.route("/baner")
def rute_baner():
    return render_template("baner.html", baner=baner)

@app.route("/lag")
def rute_lag():
    return render_template("lag.html", lag=lag, favoritter=favorittLag)

@app.route("/favoritter")
def rute_favoritter():
    return render_template("favoritter.html", favorittForere = favorittForere, favorittLag = favorittLag, favorittBaner = favorittBaner, forere=forere, lag=lag, baner=baner)

@app.route("/bane/<id>")
def rute_banene(id):
    bane = baner[id]
    return render_template("banene.html", id=id, bane=bane, favoritter=favorittBaner)

@app.route("/forer/legg-til/<id>")
def rute_leggTilFavorittForer(id):
    favorittForere.append(id)
    return rute_forerene()

@app.route("/forer/slett/<id>")
def rute_slettFavorittForer(id):
    favorittForere.remove(id)
    return rute_forerene()

@app.route("/bane/legg-til/<id>")
def rute_leggTilFavorittBane(id):
    favorittBaner.append(id)
    return rute_banene(id)

@app.route("/bane/slett/<id>")
def rute_slettFavorittBane(id):
    favorittBaner.remove(id)
    return rute_banene(id)

@app.route("/lag/legg-til/<id>")
def rute_leggTilFavorittLag(id):
    favorittLag.append(id)
    return rute_lag()

@app.route("/lag/slett/<id>")
def rute_slettFavorittLag(id):
    favorittLag.remove(id)
    return rute_lag()

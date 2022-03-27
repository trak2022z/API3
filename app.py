import random
from flask import Flask, redirect, render_template, request
import urllib.request
import urllib.parse
import json

app = Flask(__name__)

notatki = []

if __name__ == "__main__":
        app.run()

@app.route('/')
def index():
    liczba = random.randint(1, 10)
    return render_template("index.html", tytul="Astronomia z NASA", liczba=liczba, notatki=notatki)

@app.route('/zegnaj')
def zegnaj():
    return "<h1>Żegnaj!</h1>"

@app.route('/witaj')
def witaj():
    name = request.args.get("name")
    if not name:
        return render_template("error.html", tytul="Astronomia z NASA")
    return render_template("witaj.html", tytul="Astronomia z NASA", name=name)

@app.route('/dodaj', methods=["GET", "POST"])
def dodaj():
    if request.method == "GET":
        return render_template("dodaj.html")
    else:
        # notatka do nazwa formularza z pliku dodaj.html
        todo = request.form.get("notatka")
        notatki.append(todo)
        return redirect("/")

def error2(tekst):
    return render_template("error2.html", tekst=tekst)

json_url = "https://api.nasa.gov/planetary/apod?api_key=YR5F3thlEB7JDyxl1XVLX0OaXrhIXYDkeUbJ9XSb"

def read_json(url):
    u = urllib.request.urlopen(url)
    dane = u.read().decode() # Konwertuje u (tablice bajtow), na string uzywajac funkcji decode() function

    try:
        js = json.loads(dane)
        return js
    except:
        js = None
        error2("Nie można załadować pliku JSON z serwerów NASA.")

@app.route('/apod')
def apod():
    r = read_json(json_url) # Zwraca slownik
    dt = r["date"]
    expl = r["explanation"]
    tit = r["title"]
    ur = r["url"]

    return render_template("apod.html", dt=dt, expl=expl, tit=tit, ur=ur)
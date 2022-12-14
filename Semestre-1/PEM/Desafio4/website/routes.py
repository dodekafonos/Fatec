from flask import Blueprint, render_template, request, url_for
from .database import insert

routes = Blueprint('routes', __name__)

@routes.route("/")
def index():
    return render_template("index.html")

@routes.route("/quemsomos")
def quemsomos():
    return render_template("quemsomos.html")


@routes.route("/contato", methods=["GET", "POST"])
def contato():

    if request.method == "POST":
        email = request.form.get("email")
        assunto = request.form.get("assunto")
        desc = request.form.get("desc")
        insert(email, assunto, desc)
        return render_template("contato.html")
    
    return render_template("contato.html")
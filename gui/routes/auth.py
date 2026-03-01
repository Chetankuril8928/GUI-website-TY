from flask import Blueprint, request, redirect, render_template, session
from db import get_db

auth_routes = Blueprint("auth", __name__)

@auth_routes.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        db = get_db()
        user = db.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password)).fetchone()

        if user:
            session["user"] = username
            return redirect("/dashboard")
        else:
            return "Invalid Login ❌"

    return render_template("login.html")

@auth_routes.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")

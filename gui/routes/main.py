from flask import Blueprint, render_template, session, redirect

main_routes = Blueprint("main", __name__)

@main_routes.route("/")
def home():
    return render_template("index.html")

@main_routes.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")
    return render_template("dashboard.html")

@main_routes.route("/calendar")
def calendar():
    return render_template("calendar.html")

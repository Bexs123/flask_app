from flask import Flask, render_template, Blueprint, redirect, url_for

my_view = Blueprint("my_view", __name__)

@my_view.route("/")
def index():
    return render_template("index.html")

@my_view.route("/teams")
def teams():
    return render_template("teams.html")

@my_view.route("/cars")
def cars():
    return render_template("cars.html")

@my_view.route("/calender")
def calender():
    return render_template("calender.html")

@my_view.route("/circuits")
def circuits():
    return render_template("circuits.html")

@my_view.route("/driver")
def driver():
    return render_template("driver.html")

@my_view.route("/home")
@my_view.route("/js")
@my_view.route("/javascript")
def about_redirect():
    return redirect(url_for("my_view.index"))
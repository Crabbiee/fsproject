from flask import Flask, render_template, Blueprint, redirect, url_for

my_view = Blueprint('my_view', __name__)

# PAGE ROUTES
@my_view.route('/')
def index():
    return render_template("index.html")

@my_view.route('/pigeon')
def pigeon():
    return render_template("pigeon.html")

@my_view.route('/pelican')
def pelican():
    return render_template("pelican.html")

@my_view.route('/capybara')
def capybara():
    return render_template("capybara.html")

@my_view.route('/crab')
def crab():
    return render_template("crab.html")

# REDIRECTS
@my_view.route('/home')
def home_redirect():
    return redirect(url_for("my_view.index"))
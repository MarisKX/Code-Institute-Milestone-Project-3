import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from datetime import timedelta
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# sets timeout for user session
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(seconds=30)

mongo = PyMongo(app)


@app.route("/")
def home():
    car_sale_items = mongo.db.cars_for_sale.find()
    return render_template("home.html", car_sale_items=car_sale_items)


# MANAGER DASHBOARD FUNCTIONS! # MANAGER DASHBOARD FUNCTIONS! # MANAGER DASHBOARD FUNCTIONS!

# INITIAL SCREEN # INITIAL SCREEN # INITIAL SCREEN # INITIAL SCREEN # INITIAL SCREEN


@app.route("/manager-dashboard/")
def dashboard():
    return render_template("manager-dashboard/login.html")


# MANAGER MAIN SCREEN # MANAGER MAIN SCREEN # MANAGER MAIN SCREEN # MANAGER MAIN SCREEN 


@app.route("/manager-dashboard/dashboard/")
def manager_dashboard():
    if "user" in session:
        return render_template("manager-dashboard/dashboard.html")
    else:
        flash("Your session has expired!", category="info")
        return render_template("manager-dashboard/login.html")


# REGISTRATION # REGISTRATION # REGISTRATION # REGISTRATION # REGISTRATION

@app.route("/manager-dashboard/register-user", methods=["GET", "POST"])
def manager_register():
    if request.method == "POST":
        # check if registering user exists and has rights to register new users
        super_user = mongo.db.managing_users.find_one(
            {"username": request.form.get("super-username").lower(), "settings":"yes"})

        # check if username already exists in db
        existing_user = mongo.db.managing_users.find_one(
            {"username": request.form.get("username").lower()})

        if super_user:
            if existing_user:
                flash("Username already exists! Chose another one!", category="error")
                return redirect(url_for("manager_register"))
            if check_password_hash(super_user["password"], request.form.get("super-password")):
                register = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(request.form.get("password"))
                }
                mongo.db.managing_users.insert_one(register)
                flash("Welcome on board, {}".format(
                    request.form.get("username")), category="success")
                return redirect(url_for("manager_login"))
            flash("Invalid Supervisor login/password", category="error")
            return redirect(url_for("manager_register"))
        flash("You don't have rights to register new Users or Your username and/or password is incorrect!", category="error")
        return redirect(url_for("manager_register"))
        

    return render_template("manager-dashboard/register-user.html")


# LOGIN # LOGIN # LOGIN # LOGIN # LOGIN # LOGIN # LOGIN # LOGIN # LOGIN # LOGIN

@app.route("/manager-dashboard/login", methods=["GET", "POST"])
def manager_login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.managing_users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")), category="success")
                    session.permanent = True # sets session parameter to True
                    return redirect(url_for("manager_dashboard", username=session["user"]))
            else:
                # invalid password match
                flash("Invalid Username and/or Password", category="error")
                return redirect(url_for("manager_login"))

        else:
            # username doesn't exist
            flash("Invalid Username and/or Password", category="error")
            return redirect(url_for("manager_login"))

    return render_template("manager-dashboard/login.html")


# LOGOUT FUNCTION # LOGOUT FUNCTION # LOGOUT FUNCTION # LOGOUT FUNCTION

@app.route("/manager-dashboard/logout")
def manager_logout():
    # remove user from session cookie
    flash("You have been logged out", category="info")
    session.pop("user")
    return redirect(url_for("dashboard"))


# CARS FOR SALE FUNCTIONS # CARS FOR SALE FUNCTIONS # CARS FOR SALE FUNCTIONS # CARS FOR SALE FUNCTIONS 

@app.route("/manager-dashboard/cars-for-sale/")
def cars_for_sale():
    if "user" in session:
        return render_template("manager-dashboard/cars-for-sale.html")
    else:
        flash("Your session has expired!", category="info")
        return render_template("manager-dashboard/login.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

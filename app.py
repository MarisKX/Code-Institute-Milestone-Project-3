import os
import random
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from datetime import timedelta
from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# sets timeout for user session
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=15)

mongo = PyMongo(app)


@app.route("/")
def home():
    all_car_sale_items = list(mongo.db.cars_for_sale.find({"active":"yes"}))
    car_sale_items = random.sample(all_car_sale_items, k=3)
    return render_template("home.html", car_sale_items=car_sale_items)


# CARS FOR SALE PUBLIC SIDE

@app.route("/for-sale")
def for_sale():
    all_car_sale_items = list(mongo.db.cars_for_sale.find({"active":"yes"}))
    car_sale_items = random.sample(all_car_sale_items, k=6)
    return render_template("for-sale.html", car_sale_items=car_sale_items)


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
        carsfs = mongo.db.cars_for_sale.find()
        return render_template("manager-dashboard/cars-for-sale.html", carsfs=carsfs)
    else:
        flash("Your session has expired!", category="info")
        return render_template("manager-dashboard/login.html")


# ADD CAR FOR SALE # ADD CAR FOR SALE # ADD CAR FOR SALE # ADD CAR FOR SALE # ADD CAR FOR SALE 

@app.route("/manager-dashboard/add-car-for-sale/", methods=["GET", "POST"])
def add_car_for_sale():
    if "user" in session:
        if request.method == "POST":
            apk = request.form.get("apk") if request.form.get("apk") else "no"
            new_car_sale = {
                "car_id": request.form.get("car-id"),
                "created": request.form.get("created"),
                "make": request.form.get("make"),
                "model": request.form.get("model"),
                "picture1": request.form.get("picture1"),
                "picture2": request.form.get("picture2"),
                "picture3": request.form.get("picture3"),
                "picture4": request.form.get("picture4"),
                "apk": apk,
                "year": request.form.get("year"),
                "engine": request.form.get("engine"),
                "fuel": request.form.get("fuel"),
                "milage": request.form.get("milage"),
                "gearbox_type": request.form.get("gearbox-type"),
                "gears": request.form.get("gears"),
                "milage": request.form.get("milage"),
                "body": request.form.get("body"),
                "doors": request.form.get("doors"),
                "notes": request.form.get("notes"),
                "price": request.form.get("price"),
                "sold": "no",
                "active": "yes",
                "created_by": session["user"],
            }
            mongo.db.cars_for_sale.insert_one(new_car_sale)
            flash("New Car for Sale Added Successfully", category="success")
            return redirect(url_for("cars_for_sale"))
        car_id = str(mongo.db.cars_for_sale.count_documents({}) + 1)
        return render_template("manager-dashboard/add-car-for-sale.html", car_id=car_id)
    else:
        flash("Your session has expired!", category="info")
        return render_template("manager-dashboard/login.html")

# EDIT CAR FOR SALE # EDIT CAR FOR SALE # EDIT CAR FOR SALE # EDIT CAR FOR SALE # EDIT CAR FOR SALE 

@app.route("/manager-dashboard/edit-car-for-sale/<edit_id>", methods=["GET", "POST"])
def edit_car_for_sale(edit_id):
    if "user" in session:
        if request.method == "POST":
            apk = request.form.get("apk") if request.form.get("apk") else "no"
            edit_car = {
                "car_id": request.form.get("car-id"),
                "make": request.form.get("make"),
                "model": request.form.get("model"),
                "picture1": request.form.get("picture1"),
                "picture2": request.form.get("picture2"),
                "picture3": request.form.get("picture3"),
                "picture4": request.form.get("picture4"),
                "apk": apk,
                "year": request.form.get("year"),
                "engine": request.form.get("engine"),
                "fuel": request.form.get("fuel"),
                "milage": request.form.get("milage"),
                "gearbox_type": request.form.get("gearbox-type"),
                "gears": request.form.get("gears"),
                "milage": request.form.get("milage"),
                "body": request.form.get("body"),
                "doors": request.form.get("doors"),
                "notes": request.form.get("notes"),
                "price": request.form.get("price"),
                "sold": "no",
                "active": "yes",
                "edited_by": session["user"],
                "edited": request.form.get("edited"),
            }
            # USED SUPPORTED METHOD FOR CURRENT PYMONGO VERSION (old type - update with parameter without $set)
            mongo.db.cars_for_sale.update_one({"_id": ObjectId(edit_id)}, {"$set": edit_car}) 
            flash("Car Info Updated Successfully", category="success")
            return redirect(url_for("cars_for_sale"))

        car = mongo.db.cars_for_sale.find_one({"_id": ObjectId(edit_id)})
        return render_template("manager-dashboard/edit-car-for-sale.html", car=car)
    else:
        flash("Your session has expired!", category="info")
        return render_template("manager-dashboard/login.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

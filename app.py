import os
import random
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

# SETS TIMOUT FOR USER SESSION

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=15)

mongo = PyMongo(app)

# PUBLIC HOME PAGE # PUBLIC HOME PAGE # PUBLIC HOME PAGE # PUBLIC HOME PAGE


@app.route("/")
def home():
    if mongo.db.cars_for_sale.count_documents(
        {"active": "yes"}) < 10 or mongo.db.cars_for_rent.count_documents(
            {"available": "yes"}) < 3:
        return render_template("coming-soon.html")
    else:
        all_car_sale_items = list(mongo.db.cars_for_sale.find({
            "active": "yes"}))
        car_sale_items = random.sample(all_car_sale_items, k=3)
        all_car_rent_items = list(mongo.db.cars_for_rent.find({
            "available": "yes"}))
        car_rent_items = random.sample(all_car_rent_items, k=3)
        return render_template(
            "home.html",
            car_sale_items=car_sale_items,
            car_rent_items=car_rent_items)


# CARS FOR SALE PUBLIC SIDE # CARS FOR SALE PUBLIC SIDE

@app.route("/for-sale/", methods=["GET", "POST"])
def for_sale():
    if request.method == "POST":
        search_keyword = request.form.get("make")
        if mongo.db.cars_for_sale.count_documents(
                {"make": search_keyword}) != 0:

            search_results = mongo.db.cars_for_sale.find(
                {"make": search_keyword, "active": "yes"}).sort("model", 1)
            car_makes = mongo.db.car_makes.find().sort("make", 1)
            all_car_sale_items_list = list(mongo.db.cars_for_sale.find(
                {"active": "yes"}))
            car_sale_items = random.sample(all_car_sale_items_list, k=10)

            return render_template(
                "search-results.html",
                search_results=search_results,
                car_sale_items=car_sale_items,
                car_makes=car_makes)

        flash("Select Your search criteria")
    car_makes = mongo.db.car_makes.find().sort("make", 1)
    all_car_sale_items_list = list(mongo.db.cars_for_sale.find(
        {"active": "yes"}))
    car_sale_items = random.sample(all_car_sale_items_list, k=10)
    return render_template(
        "for-sale.html",
        car_sale_items=car_sale_items,
        car_makes=car_makes)


@app.route("/for-sale/details/<car_id>")
def carfs_details(car_id):
    carfs = mongo.db.cars_for_sale.find({"_id": ObjectId(car_id)})
    return render_template("car-details.html", carfs=carfs)

# CARS FOR RENT PUBLIC SIDE # CARS FOR RENT PUBLIC SIDE


@app.route("/for-rent/", methods=["GET", "POST"])
def for_rent():
    if request.method == "POST":
        search_keyword = request.form.get("make")
        if mongo.db.cars_for_rent.count_documents(
                {"make": search_keyword}) != 0:

            search_results = mongo.db.cars_for_rent.find(
                {"make": search_keyword}).sort("model", 1)
            car_makes_rent = mongo.db.car_makes_rent.find().sort("make", 1)
            all_car_rent_items_list = list(mongo.db.cars_for_rent.find(
                {"available": "yes"}))
            car_rent_items = random.sample(all_car_rent_items_list, k=3)

            return render_template(
                "search-results-rent.html",
                search_results=search_results,
                car_rent_items=car_rent_items,
                car_makes_rent=car_makes_rent)
        flash("Select Your search criteria")
    car_makes_rent = mongo.db.car_makes_rent.find().sort("make", 1)
    all_car_rent_items_list = list(mongo.db.cars_for_rent.find(
        {"available": "yes"}))
    car_rent_items = random.sample(all_car_rent_items_list, k=3)

    return render_template(
        "for-rent.html",
        car_rent_items=car_rent_items,
        car_makes_rent=car_makes_rent)


@app.route("/for-rent/details/<car_id>")
def carfr_details(car_id):
    carfr = mongo.db.cars_for_rent.find({"_id": ObjectId(car_id)})
    return render_template("car-rent-details.html", carfr=carfr)


# MANAGER DASHBOARD FUNCTIONS! # MANAGER DASHBOARD FUNCTIONS!

# INITIAL SCREEN # INITIAL SCREEN # INITIAL SCREEN # INITIAL SCREEN


@app.route("/manager-dashboard/")
def dashboard():
    return render_template("manager-dashboard/login.html")


# MANAGER MAIN SCREEN # MANAGER MAIN SCREEN # MANAGER MAIN SCREEN


@app.route("/manager-dashboard/dashboard/")
def manager_dashboard():
    if "user" in session:
        all_cars_count = mongo.db.cars_for_sale.count_documents(
            {"active": "yes"})
        for_sale_cars_count = mongo.db.cars_for_sale.count_documents(
            {"active": "yes", "sold": "no"})
        sold_cars_count = mongo.db.cars_for_sale.count_documents(
            {"sold": "yes"})
        sold_by_user = mongo.db.cars_for_sale.count_documents(
            {"sold_by": session["user"]})
        salesman = session["user"]
        all_rental_cars = mongo.db.cars_for_rent.count_documents(
            {"archived": "no"})
        avail_rental_cars = mongo.db.cars_for_rent.count_documents(
            {"available": "yes"})
        created_by_user = mongo.db.cars_for_rent.count_documents(
            {"created_by": session["user"]})

        return render_template(
            "manager-dashboard/dashboard.html",
            all_cars_count=all_cars_count,
            for_sale_cars_count=for_sale_cars_count,
            sold_cars_count=sold_cars_count,
            sold_by_user=sold_by_user,
            salesman=salesman,
            all_rental_cars=all_rental_cars,
            avail_rental_cars=avail_rental_cars,
            created_by_user=created_by_user)
    else:
        flash("Your session has expired!", category="info")
        return render_template("manager-dashboard/login.html")


# REGISTRATION # REGISTRATION # REGISTRATION # REGISTRATION # REGISTRATION

@app.route("/manager-dashboard/register-user", methods=["GET", "POST"])
def manager_register():
    if request.method == "POST":
        # check if registering user exists and has rights to register new users
        super_user = mongo.db.managing_users.find_one(
            {"username": request.form.get(
                "super-username").lower(), "settings": "yes"})

        # check if username already exists in db
        existing_user = mongo.db.managing_users.find_one(
            {"username": request.form.get("username").lower()})

        if super_user:
            if existing_user:
                flash(
                    "Username already exists! Chose another one!",
                    category="error")

                return redirect(url_for("manager_register"))
            if check_password_hash(super_user[
                    "password"], request.form.get("super-password")):
                register = {
                    "username": request.form.get("username").lower(),
                    "password": generate_password_hash(request.form.get(
                        "password")),
                    "car_sales": "no",
                    "car_rent": "no",
                    "settings": "no",
                    "superuser": "no"
                    }
                mongo.db.managing_users.insert_one(register)
                flash("Welcome on board, {}".format(
                    request.form.get("username")), category="success")
                return redirect(url_for("manager_login"))
            flash("Invalid Supervisor login/password", category="error")
            return redirect(url_for("manager_register"))
        flash(
            "You don't have rights to register new Users" +
            "or Your username and/or password is incorrect!",
            category="error")
        return redirect(url_for("manager_register"))

    return render_template("manager-dashboard/register-user.html")


# LOGIN # LOGIN # LOGIN # LOGIN # LOGIN # LOGIN # LOGIN # LOGIN # LOGIN

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
                        request.form.get("username")), category="welcome")
                session.permanent = True   # sets session parameter to True
                return redirect(url_for(
                    "manager_dashboard",
                    username=session["user"]))
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


# CARS FOR SALE FUNCTIONS # CARS FOR SALE FUNCTIONS # CARS FOR SALE FUNCTIONS

# MAIN ROUTE # MAIN ROUTE # MAIN ROUTE # MAIN ROUTE # MAIN ROUTE # MAIN ROUTE

@app.route("/manager-dashboard/cars-for-sale/")
def cars_for_sale():
    if "user" in session:
        carsfs = mongo.db.cars_for_sale.find()
        db_user = mongo.db.managing_users.find_one(
            {"username": session["user"]})
        return render_template(
            "manager-dashboard/cars-for-sale.html",
            carsfs=carsfs,
            db_user=db_user)
    else:
        flash("Your session has expired!", category="info")
        return render_template("manager-dashboard/login.html")


# ADD CAR FOR SALE # ADD CAR FOR SALE # ADD CAR FOR SALE # ADD CAR FOR SALE

@app.route("/manager-dashboard/add-car-for-sale/", methods=["GET", "POST"])
def add_car_for_sale():
    if "user" in session:
        sales_cars_count = mongo.db.car_count.find_one({"type": "sales"})
        current_count = int(sales_cars_count["car_count"])
        car_id = str(current_count + 1)

        if request.method == "POST":
            apk = request.form.get("apk") if request.form.get("apk") else "no"
            form_car_make = request.form.get("make")
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
                "body": request.form.get("body"),
                "doors": request.form.get("doors"),
                "notes": request.form.get("notes"),
                "price": request.form.get("price"),
                "sold": "no",
                "active": "yes",
                "created_by": session["user"],
            }
            new_car_count = {
                "car_count": car_id,
            }
            mongo.db.cars_for_sale.insert_one(new_car_sale)
            mongo.db.car_count.update_one({"type": "sales"}, {
                "$set": new_car_count})
            if mongo.db.car_makes.count_documents({
                    "make": form_car_make}) == 0:
                insert_car_make = {
                    "make": form_car_make,
                }
                mongo.db.car_makes.insert_one(insert_car_make)
            else:
                pass
            flash("New Car for Sale Added Successfully", category="success")
            return redirect(url_for("cars_for_sale"))

        return render_template(
            "manager-dashboard/add-car-for-sale.html",
            car_id=car_id)
    else:
        flash("Your session has expired!", category="info")
        return render_template("manager-dashboard/login.html")


# SHOW DETAILS/STATS # SHOW DETAILS/STATS # SHOW DETAILS/STATS

@app.route("/manager-dashboard/car-details/<car_id>", methods=["GET", "POST"])
def car_details(car_id):
    if "user" in session:
        selected_car = mongo.db.cars_for_sale.find({"_id": ObjectId(car_id)})
        return render_template(
            "manager-dashboard/car-details.html",
            selected_car=selected_car)
    else:
        flash("Your session has expired!", category="info")
        return render_template("manager-dashboard/login.html")

# EDIT CAR FOR SALE # EDIT CAR FOR SALE # EDIT CAR FOR SALE


@app.route(
    "/manager-dashboard/edit-car-for-sale/<edit_id>",
    methods=["GET", "POST"])
def edit_car_for_sale(edit_id):
    if "user" in session:
        db_user = mongo.db.managing_users.find_one(
            {"username": session["user"]})
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
                "body": request.form.get("body"),
                "doors": request.form.get("doors"),
                "notes": request.form.get("notes"),
                "price": request.form.get("price"),
                "sold": "no",
                "active": "yes",
                "edited_by": session["user"],
                "edited": request.form.get("edited"),
            }
            # USED SUPPORTED METHOD FOR CURRENT PYMONGO VERSION
            # (old type - update with parameter without $set)
            mongo.db.cars_for_sale.update_one(
                {"_id": ObjectId(edit_id)}, {"$set": edit_car})
            flash("Car Info Updated Successfully", category="success")
            return redirect(url_for("cars_for_sale"))

        car = mongo.db.cars_for_sale.find_one({"_id": ObjectId(edit_id)})
        return render_template(
            "manager-dashboard/edit-car-for-sale.html",
            car=car,
            db_user=db_user)
    else:
        flash("Your session has expired!", category="info")
        return render_template("manager-dashboard/login.html")

# MARK AS SOLD # MARK AS SOLD # MARK AS SOLD # MARK AS SOLD # MARK AS SOLD


@app.route("/manager-dashboard/mark-as-sold/<car_id>", methods=["GET", "POST"])
def mark_as_sold(car_id):
    if "user" in session:
        if request.method == "POST":
            confirm_as_sold = {
                "sold": "yes",
                "sold_at": request.form.get("sold_at"),
                "price": request.form.get("final-price"),
                "sold_by": session["user"],
            }
            # USED SUPPORTED METHOD FOR CURRENT PYMONGO VERSION
            # (old type - update with parameter without $set)
            mongo.db.cars_for_sale.update_one(
                {"_id": ObjectId(car_id)}, {"$set": confirm_as_sold})
            flash("Car Marked as Sold Successfully", category="success")
            return redirect(url_for("cars_for_sale"))

        car = mongo.db.cars_for_sale.find_one({"_id": ObjectId(car_id)})
        return render_template("manager-dashboard/mark-as-sold.html", car=car)
    else:
        flash("Your session has expired!", category="info")
        return render_template("manager-dashboard/login.html")

# CARS FOR RENT FUNCTIONS # CARS FOR RENT FUNCTIONS # CARS FOR RENT FUNCTIONS

# MAIN ROUTE # MAIN ROUTE # MAIN ROUTE # MAIN ROUTE # MAIN ROUTE # MAIN ROUTE


@app.route("/manager-dashboard/cars-for-rent/")
def cars_for_rent():
    if "user" in session:
        carsfr = mongo.db.cars_for_rent.find()
        db_user = mongo.db.managing_users.find_one(
            {"username": session["user"]})
        return render_template(
            "manager-dashboard/cars-for-rent.html",
            carsfr=carsfr,
            db_user=db_user)
    else:
        flash("Your session has expired!", category="info")
        return render_template("manager-dashboard/login.html")

# ADD CAR FOR RENT # ADD CAR FOR RENT # ADD CAR FOR RENT # ADD CAR FOR RENT


@app.route("/manager-dashboard/add-car-for-rent/", methods=["GET", "POST"])
def add_car_for_rent():
    if "user" in session:
        rental_car_count = mongo.db.car_count.find_one({"type": "rental"})
        current_count = int(rental_car_count["car_count"])
        car_rent_id = str(current_count + 1)

        if request.method == "POST":
            form_car_make = request.form.get("make")
            new_car_rent = {
                "car_id": request.form.get("car-rent-id"),
                "created": request.form.get("created"),
                "make": request.form.get("make"),
                "model": request.form.get("model"),
                "picture1": request.form.get("picture1"),
                "picture2": request.form.get("picture2"),
                "picture3": request.form.get("picture3"),
                "picture4": request.form.get("picture4"),
                "year": request.form.get("year"),
                "engine": request.form.get("engine"),
                "fuel": request.form.get("fuel"),
                "gearbox_type": request.form.get("gearbox-type"),
                "body": request.form.get("body"),
                "doors": request.form.get("doors"),
                "milage_limit": request.form.get("milage-limit"),
                "notes": request.form.get("notes"),
                "price": request.form.get("price"),
                "available": "no",
                "archived": "no",
                "created_by": session["user"],
            }
            new_car_count = {
                "car_count": car_rent_id,
            }
            mongo.db.cars_for_rent.insert_one(new_car_rent)
            mongo.db.car_count.update_one(
                {"type": "rental"}, {"$set": new_car_count})
            if mongo.db.car_makes_rent.count_documents(
                    {"make": form_car_make}) == 0:
                insert_car_make = {
                    "make": form_car_make,
                }
                mongo.db.car_makes_rent.insert_one(insert_car_make)
            else:
                pass
            flash("New Car for Rent Added Successfully", category="success")
            return redirect(url_for("cars_for_rent"))

        return render_template(
            "manager-dashboard/add-car-for-rent.html",
            car_rent_id=car_rent_id)
    else:
        flash("Your session has expired!", category="info")
        return render_template("manager-dashboard/login.html")

# SHOW DETAILS/STATS # SHOW DETAILS/STATS # SHOW DETAILS/STATS


@app.route(
    "/manager-dashboard/car-details-rent/<car_id>",
    methods=["GET", "POST"])
def rental_car_details(car_id):
    if "user" in session:
        selected_rental_car = mongo.db.cars_for_rent.find(
            {"_id": ObjectId(car_id)})
        return render_template(
            "manager-dashboard/car-details-rent.html",
            selected_rental_car=selected_rental_car)
    else:
        flash("Your session has expired!", category="info")
        return render_template("manager-dashboard/login.html")

# EDIT CAR FOR RENT # EDIT CAR FOR RENT # EDIT CAR FOR RENT # EDIT CAR FOR RENT


@app.route(
    "/manager-dashboard/edit-car-for-rent/<edit_id>",
    methods=["GET", "POST"])
def edit_car_for_rent(edit_id):
    if "user" in session:
        db_user = mongo.db.managing_users.find_one(
            {"username": session["user"]})
        if request.method == "POST":
            edit_car = {
                "car_id": request.form.get("car-rent-id"),
                "make": request.form.get("make"),
                "model": request.form.get("model"),
                "picture1": request.form.get("picture1"),
                "picture2": request.form.get("picture2"),
                "picture3": request.form.get("picture3"),
                "picture4": request.form.get("picture4"),
                "year": request.form.get("year"),
                "engine": request.form.get("engine"),
                "fuel": request.form.get("fuel"),
                "gearbox_type": request.form.get("gearbox-type"),
                "body": request.form.get("body"),
                "doors": request.form.get("doors"),
                "milage_limit": request.form.get("milage-limit"),
                "notes": request.form.get("notes"),
                "price": request.form.get("price"),
                "archived": "no",
                "edited_by": session["user"],
                "edited": request.form.get("edited"),
            }
            # USED SUPPORTED METHOD FOR CURRENT PYMONGO VERSION
            # (old type - update with parameter without $set)
            mongo.db.cars_for_rent.update_one(
                {"_id": ObjectId(edit_id)}, {"$set": edit_car})
            flash("Car Info Updated Successfully", category="success")
            return redirect(url_for("cars_for_rent"))

        car = mongo.db.cars_for_rent.find_one({"_id": ObjectId(edit_id)})
        return render_template(
            "manager-dashboard/edit-car-for-rent.html",
            car=car,
            db_user=db_user)
    else:
        flash("Your session has expired!", category="info")
        return render_template("manager-dashboard/login.html")

# CHANGE AVAILABLITY # CHANGE AVAILABLITY # CHANGE AVAILABLITY


@app.route("/manager-dashboard/change-availability/<rent_id>")
def change_availability(rent_id):
    if "user" in session:
        rental_car = mongo.db.cars_for_rent.find({"_id": ObjectId(rent_id)})
        for i in rental_car:
            if i["available"] == "yes":
                details = {
                    "available": "no",
                }
                mongo.db.cars_for_rent.update_one(
                    {"_id": ObjectId(rent_id)},
                    {"$set": details})
                flash(
                    "{} is marked as Unavailable"
                    .format(i["make"] + " (" + i["car_id"] + ")"))
                return redirect(url_for("cars_for_rent"))
            else:
                details = {
                    "available": "yes",
                }
                mongo.db.cars_for_rent.update_one(
                    {"_id": ObjectId(rent_id)},
                    {"$set": details})
                flash(
                    "{} is marked as Available"
                    .format(i["make"] + " (" + i["car_id"] + ")"))
                return redirect(url_for("cars_for_rent"))
                flash("Welcome, {}".format(
                            request.form.get("username")), category="welcome")
    else:
        flash("Your session has expired!", category="info")
        return render_template("manager-dashboard/login.html")


# MOVE RENTAL CAR TO AND FROM ARCHIVE # MOVE RENTAL CAR TO AND FROM ARCHIVE

@app.route("/manager-dashboard/rent-archive/<rent_id>")
def rent_archive(rent_id):
    if "user" in session:
        rental_car = mongo.db.cars_for_rent.find({"_id": ObjectId(rent_id)})
        for i in rental_car:
            if i["archived"] == "yes":
                details = {
                    "archived": "no",
                }
                mongo.db.cars_for_rent.update_one(
                    {"_id": ObjectId(rent_id)},
                    {"$set": details})
                flash(
                    "{} is removed from arhive"
                    .format(i["make"] + " (" + i["car_id"] + ")"))
                return redirect(url_for("cars_for_rent"))
            else:
                details = {
                    "archived": "yes",
                }
                mongo.db.cars_for_rent.update_one(
                    {"_id": ObjectId(rent_id)},
                    {"$set": details})
                flash(
                    "{} is moved to arhive"
                    .format(i["make"] + " (" + i["car_id"] + ")"))
                return redirect(url_for("cars_for_rent"))
    else:
        flash("Your session has expired!", category="info")
        return render_template("manager-dashboard/login.html")

# DELETE RENTAL CAR # DELETE RENTAL CAR # DELETE RENTAL CAR # DELETE RENTAL CAR


@app.route(
    "/manager-dashboard/delete-rental-car/<rent_id>",
    methods=["GET", "POST"])
def delete_rental_car(rent_id):
    if "user" in session:
        car = mongo.db.cars_for_rent.find({"_id": ObjectId(rent_id)})
        deleted_car = mongo.db.cars_for_rent.find_one(
            {"_id": ObjectId(rent_id)})
        make = str(deleted_car["make"])
        carid = str(deleted_car["car_id"])
        if request.method == "POST":
            rental_car_count = mongo.db.car_count.count_documents(
                {"make": make})
            if rental_car_count > 1:
                pass
            else:
                mongo.db.car_makes_rent.delete_one({"make": make})
            mongo.db.cars_for_rent.delete_one({"_id": ObjectId(rent_id)})
            flash("{} is deleted".format(make + " (" + carid + ")"))
            return redirect(url_for("cars_for_rent"))
        return render_template(
            "manager-dashboard/delete-rental-car.html",
            car=car)
    else:
        flash("Your session has expired!", category="info")
        return render_template("manager-dashboard/login.html")

# SETTINGS AREA # SETTINGS AREA # SETTINGS AREA # SETTINGS AREA # SETTINGS AREA


@app.route("/manager-dashboard/settings/<username>", methods=["GET", "POST"])
def manager_settings(username):
    if "user" in session:
        user = mongo.db.managing_users.find({"username": session["user"]})
        all_users = list(mongo.db.managing_users.find())
        if request.method == "POST":
            if "change-password" in request.form:
                current_user = mongo.db.managing_users.find_one(
                    {"username": username})
                if check_password_hash(current_user[
                    "password"],
                        request.form.get("old_password")):
                    new_password = {
                        "password": generate_password_hash(request.form.get(
                            "new_password"))
                    }
                    mongo.db.managing_users.update_one(
                        {"username": session["user"]},
                        {"$set": new_password})
                    flash(
                        "Password changed for {}"
                        .format(session["user"]), category="success")

                    return redirect(url_for(
                        "manager_settings",
                        username=username))
                flash(
                    "Wrong password for {}"
                    .format(session["user"]),
                    category="welcome")

                return render_template(
                    "manager-dashboard/settings.html",
                    user=user)
            elif "user-rights" in request.form:
                for i in all_users:
                    upd_username = i["username"]
                    if i["superuser"] == "yes" or upd_username == session[
                            "user"]:
                        continue
                    else:
                        car_sales = "yes" if request.form.get(
                            "checkbox_sales " + upd_username + "") else "no"
                        car_rent = "yes" if request.form.get(
                            "checkbox_rent " + upd_username + "") else "no"
                        settings = "yes" if request.form.get(
                            "checkbox_settings " + upd_username + "") else "no"
                        update_rights = {
                            "car_sales": car_sales,
                            "car_rent": car_rent,
                            "settings": settings,
                        }
                        mongo.db.managing_users.update_one(
                            {"username": upd_username},
                            {"$set": update_rights})
                flash(
                    "Acces rights changed for {}"
                    .format(session["user"].capitalize()), category="success")
                return redirect(url_for("manager_settings", username=username))
            elif "delete-user" in request.form:
                print("Here")
                user_delete = request.form.get("user")
                print(user_delete)
                mongo.db.managing_users.delete_one({"username": user_delete})
                flash(
                    "{} deleted"
                    .format(user_delete.capitalize()),
                    category="success")
                return redirect(url_for("manager_settings", username=username))
        return render_template(
            "manager-dashboard/settings.html",
            user=user,
            all_users=all_users)
    else:
        flash("Your session has expired!", category="info")
        return render_template("manager-dashboard/login.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

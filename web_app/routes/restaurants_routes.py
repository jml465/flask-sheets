# code template from s2t2 Customizations #9. Credit: Prof. Rossetti

from flask import Blueprint, render_template, current_app #, session

from app.models.restaurants import Restaurants

restaurants_routes = Blueprint("restaurants_routes", __name__)

@restaurants_routes.route("/restaurants")
def restaurants():
    restaurants = Restaurants.all()
    return render_template("restaurants.html", restaurants=restaurants)
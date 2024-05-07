# code template from s2t2 Customizations #9. Credit: Prof. Rossetti
from app.db import BaseModel

class Restaurants(BaseModel):

    SHEET_NAME = "restaurants"

    COLUMNS = ["name", "cuisine", "star_rating", "neighborhood"]

    SEEDS = [
        {"name": "La Grande Boucherie", "cuisine": "French", "star_rating": 4, "neighborhood": "Downtown"},
        {"name": "Jont", "cuisine": "French/Japanese", "star_rating": 5, "neighborhood": "U Street Corridor"},
        {"name": "Oyamel", "cuisine": "Meixcan", "star_rating": 4.5, "neighborhood": "Penn Quarter"},
        {"name": "Filomena", "cuisine": "Italian", "star_rating": 4.8, "neighborhood": "Georgetown"},
        {"name": "Taberna del Alabardero", "cuisine": "Traditional Spanish", "star_rating": 4.8, "neighborhood": "Downtown"},
        {"name": "Jaleo", "cuisine": "Spanish", "star_rating": 4.7, "neighborhood": "Penn Quarter"},
        {"name": "El Secreto de Rosita", "cuisine": "Latin American", "star_rating": 4.5, "neighborhood": "Downtown"},
        {"name": "The Pembroke", "cuisine": "Global, International", "star_rating": 4.5, "neighborhood": "Dupont Circle"},
        {"name": "Zaytinya", "cuisine": "Mediterranean", "star_rating": 4.8, "neighborhood": "Penn Quarter"},
        {"name": "dLena", "cuisine": "Latin American", "star_rating": 4.6, "neighborhood": "Mount Vernon Square"},
        {"name": "Xiquet by Danny Lledo", "cuisine": "Spanish", "star_rating": 5, "neighborhood": "Georgetown"},
        {"name": "Kaliwa", "cuisine": "Asian", "star_rating": 3.4, "neighborhood": "Southwest Waterfront"},
    ]


if __name__ == "__main__":

    restaurants = Restaurants.all()
    print("FOUND", len(restaurants), "RESTAURANTS")
    if any(restaurants):
        for restaurant in restaurants:
            print(restaurant.name, restaurant.cuisine, restaurant.star_rating, restaurant.neighborhood)
    else:
        Restaurant.seed()
from datetime import datetime
from myapp import db

# Restaurant model
class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique= True, nullable = False)
    address = db.Column(db.String(100),nullable = False)

    # define a relationship with pizza
    pizza = db.relationship('Pizza', secondary='restaurant_pizza', back_populates='restaurants')

    # Define a relationship with restaurant-pizza
    restaurant_pizza = db.relationship('RestaurantPizza', back_populates='restaurant')


    def __repr__(self):
        return f"Restaurant('{self.name}', '{self.address}')"

# Pizza model
class Pizza(db.Model):
    id = db.Column(db.Integer,primary_key= True)
    name = db.Column(db.String(50), unique= True, nullable = False)
    ingredients =db.Column(db.String(200), nullable= False)
    created_at = db.Column(db.DateTime, nullable = False, default= datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable = False, default= datetime.utcnow)

    # define a relationship with restaurant
    restaurants = db.relationship('Restaurant', secondary='restaurant_pizza', back_populates='pizza')

     # Define a relationship with restaurant-pizza
    restaurant_pizza = db.relationship('RestaurantPizza', back_populates='pizza')


    def __repr__(self):
        return f"Pizza('{self.name}', '{self.ingredients}')"

# restaurant_pizza(associstion table)

class RestaurantPizza(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    price = db.Column(db.Float, nullable=False, server_default='1', server_onupdate='1', info={"check": "price >= 1 and price <= 30"})
    created_at = db.Column(db.DateTime, nullable = False, default= datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable = False, default= datetime.utcnow)

#    Define a foreignkey  with pizza and restaurant
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)

# define relationship with pizza and restaurant
    restaurant = db.relationship('Restaurant', back_populates='restaurant_pizza')
    pizza = db.relationship('Pizza', back_populates='restaurant_pizza')

    def __repr__(self):
        return f"RestaurantPizza(Price: {self.price})"




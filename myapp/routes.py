from flask import Blueprint, jsonify, request
from myapp.models import Restaurant, Pizza, RestaurantPizza
from myapp import db

# create a blueprint
main_blueprint = Blueprint('main', __name__)

# create routes
# Get restaurant
@main_blueprint.route('/restaurant', methods=['GET'])
def get_restaurants():
    # query all the restaurants from the database
    restaurants = Restaurant.query.all()

    # create a list of restaurant to have a dictionary inside(a dictionary inside a list)
    restaurant_list = []

    for restaurant in restaurants:
        # create a dictionary and append to the list
        restaurant_dict={
            'id':restaurant.id,
            'name':restaurant.name,
            'address':restaurant.address

        }
        # append the dict to list
        restaurant_list.append(restaurant_dict)

        # return the list as a json
    return jsonify(restaurant_list)

# get restaursnt by id
@main_blueprint.route('/restaurant/<int:id>', methods=['GET'])
def get_restaurant(id):
        restaurant = Restaurant.query.get(id)

        # rep the restaurant data as a dict
        if restaurant:
             restaurant_data = {
                'id':restaurant.id,
                'name':restaurant.name,
                'address':restaurant.address

             }
            #  return as json data with a status code of success
             return jsonify(restaurant_data), 200
        else:
            #  have an error response if no restaurant of that id is specified
             error_response = {'error': 'Restaurant not found'}
             return jsonify(error_response), 404
        

@main_blueprint.route('/restaurant/<int:id>', methods=['DELETE'])       
def delete_restaurant(id):
    # Fetch the restaurant by id
    restaurant = Restaurant.query.get(id)

    if restaurant is None:
        # Handle the case where the restaurant doesn't exist
        return jsonify({'message': 'Restaurant not found'}), 404

    try:
        # Delete associated records in the restaurant_pizza table
        RestaurantPizza.query.filter_by(restaurant_id=id).delete()

        # Delete the restaurant
        db.session.delete(restaurant)
        db.session.commit()

        return jsonify({'message': 'Restaurant deleted successfully'}), 200
    except Exception as e:
        # Handle any exceptions that may occur during the deletion
        db.session.rollback()
        return jsonify({'message': 'An error occurred while deleting the restaurant'}), 500
         
@main_blueprint.route('/pizza', methods=['GET'])
def get_pizza():
    #  query the database
    pizzas = Pizza.query.all()

    # create a list of dict
    pizzas_list = []
    # create a dict
    for pizza in pizzas:
         pizza_data = {
              'name': pizza.name,
              'ingredients':pizza.ingredients
              
         }

         pizzas_list.append(pizza_data)
        #  return list as json

    return jsonify(pizzas_list)

@main_blueprint.route('/restaurant_pizzas', methods =['POST'])
def create_restaurant_pizza():
    try:
        # Parse JSON data from the request
        data = request.get_json()

        # Extract restaurant_id, pizza_id, and any other relevant data
        restaurant_id = data['restaurant_id']
        pizza_id = data['pizza_id']
        price = data['price']

        # Check if the restaurant and pizza exist in the database
        restaurant = Restaurant.query.get(restaurant_id)
        pizza = Pizza.query.get(pizza_id)

        if not restaurant or not pizza:
            return jsonify({'error': 'Restaurant or pizza not found'}), 404

        # Create a new RestaurantPizza and associate it
        new_restaurant_pizza = RestaurantPizza(restaurant=restaurant, pizza=pizza, price=price)

        # Add the new RestaurantPizza to the database session
        db.session.add(new_restaurant_pizza)

        # Commit the transaction to save the new association
        db.session.commit()

        return jsonify({'message': 'RestaurantPizza created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500







     
    

             
        


             





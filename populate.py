from myapp import app, db
from myapp.models import Restaurant, Pizza, RestaurantPizza

def populate_database():
    with app.app_context():
        # instance of our models
        restaurant1 = Restaurant(name='Dominos Pizza',address='Kileleshwa, 5th Avenue')
        restaurant2 = Restaurant(name='Pizza inn',address='Gardencity, Homeland, Nrb 100')
        restaurant3 = Restaurant(name='Oven Bites inn',address='Trm, Homeland, Nrb 100')
        restaurant4 = Restaurant(name='Power Pizza',address='Gardencity, Homeland, Nrb 100')
        restaurant5 = Restaurant(name='Pizza Express',address='Gardencity, Homeland, Nrb 100')

        pizza1 = Pizza(name='Cheese', ingredients='Dough, Tomato Sauce, Cheese')
        pizza2 = Pizza(name='Pepperoni', ingredients='Dough, Tomato Sauce, Cheese')
        pizza3 = Pizza(name='Barbeque', ingredients='Dough, Tomato Sauce, Cheese')
        pizza4 = Pizza(name='Cheese and onion', ingredients='Dough, Tomato Sauce, Cheese')
        pizza5 = Pizza(name='Pineaple', ingredients='Dough, Tomato Sauce, Cheese')

        # create aninstance of the association table
        restaurant_pizza1 = RestaurantPizza(price=5, restaurant=restaurant1, pizza=pizza1)
        restaurant_pizza2  = RestaurantPizza(price=8, restaurant=restaurant2, pizza=pizza2)
        restaurant_pizza3 = RestaurantPizza(price=7, restaurant=restaurant3, pizza=pizza3)
        restaurant_pizza4  = RestaurantPizza(price=9, restaurant=restaurant4, pizza=pizza4)
        restaurant_pizza5  = RestaurantPizza(price=10, restaurant=restaurant5, pizza=pizza5)

        # Add data to the database
        db.session.add(restaurant1)
        db.session.add(restaurant2)
        db.session.add(restaurant3)
        db.session.add(restaurant4)
        db.session.add(restaurant5)
        db.session.add(pizza1)
        db.session.add(pizza2)
        db.session.add(pizza3)
        db.session.add(pizza4)
        db.session.add(pizza5)
        db.session.add(restaurant_pizza1)
        db.session.add(restaurant_pizza2)
        db.session.add(restaurant_pizza3)
        db.session.add(restaurant_pizza4)
        db.session.add(restaurant_pizza5)
        
        try:
            # commit changes to db
            db.session.commit()
            print("Data added successfully")
        except Exception as e:
            db.session.rollback()
            print(f'Failed: {str(e)}')


    #  db.session.query(Pizza).delete()
    #  db.session.query(Restaurant).delete()
    #  db.session.query(RestaurantPizza).delete()
    #  db.session.commit()



if __name__ == '__main__':
    populate_database()



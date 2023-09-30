from myapp import app

class TestApp:
    def test_restaurant_view(self):
     client = app.test_client(self)
     response = client.get('/restaurant')
     assert response.status_code == 200

    def test_pizza_view(self):
     client = app.test_client(self)
     response = client.get('/pizza')
     assert response.status_code == 200

    def test_restaurant_pizza_view(self):
     client = app.test_client(self)
     response = client.get('/restaurant_pizzas')
     assert response.status_code == 200
from myapp import app,db
from myapp.models import Restaurant, Pizza, RestaurantPizza
from myapp.routes import main_blueprint

# Register the blueprint
app.register_blueprint(main_blueprint)

@app.route('/') 
def home():
    return 'Hello world!'

if __name__ == '__main__':
    app.run(debug = True)

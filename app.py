from app.models import db
from app import create_app

app = create_app('DevelopmentConfig')  # Initialize the Flask app with the development configuration

with app.app_context():
    db.drop_all() #Dropping all our database tables
    db.create_all() #Creating our database tables


app.run(debug=True)
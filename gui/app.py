from flask import Flask
from routes.main import main_routes
from routes.auth import auth_routes
from routes.api import api_routes

app = Flask(__name__)
app.secret_key = "secret123"

app.register_blueprint(main_routes)
app.register_blueprint(auth_routes)
app.register_blueprint(api_routes)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask
from routes import factorial_routes, io_routes

app = Flask(__name__)

app.register_blueprint(factorial_routes)
app.register_blueprint(io_routes)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

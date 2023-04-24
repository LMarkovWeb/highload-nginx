from flask import Blueprint, jsonify
from utils import factorial, create_files

factorial_routes = Blueprint('factorial_routes', __name__)
io_routes = Blueprint('io_routes', __name__)

@factorial_routes.route("/fac/<int:n>")
@factorial_routes.route("/fac/<int:n>/")
def get_factorial(n):
    fact = factorial(n)
    return jsonify({"factorial": fact})

@io_routes.route("/io/<int:n>")
@io_routes.route("/io/<int:n>/")
def create_files_api(n):
    result = create_files(n)
    return jsonify({"Result": result})

from flask import Blueprint, jsonify
from utils import factorial, create_files
import socket
import random
import time

hostname = socket.gethostname()

factorial_routes = Blueprint('factorial_routes', __name__)
io_routes = Blueprint('io_routes', __name__)

@factorial_routes.route("/fac/<int:n>")
@factorial_routes.route("/fac/<int:n>/")  # 1-100_000
def get_factorial(n):
    fact = factorial(n)
    return jsonify({"factorial": fact, "hostname": hostname})

@factorial_routes.route("/fac/<int:n>")
@factorial_routes.route("/fac/<int:n>/")  # 1-100_000
def get_factorial_latency(n):
    fact = factorial(n)
    time.sleep(5)
    return jsonify({"factorial": fact, "hostname": hostname})

@factorial_routes.route("/fac/<int:n>")
@factorial_routes.route("/fac/<int:n>/")  # 1-100_000
def get_factorial_random_latency(n):
    fact = factorial(n)
    if random.random() <= 0.01:
        time.sleep(1)
    return jsonify({"factorial": fact, "hostname": hostname})

@io_routes.route("/io/<int:n>")
@io_routes.route("/io/<int:n>/")
def create_files_api(n):
    result = create_files(n)
    return jsonify({"Result": result})

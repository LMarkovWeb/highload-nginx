from flask import Blueprint, jsonify
from utils import factorial
import socket
import random
import time

hostname = socket.gethostname()

factorial_routes = Blueprint('factorial_routes', __name__)

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


from flask import Blueprint, jsonify
from utils import factorial
import socket
import random
import time

hostname = socket.gethostname()

factorial_routes = Blueprint('factorial_routes', __name__)

@factorial_routes.route("/fac/<int:n>")
@factorial_routes.route("/fac/<int:n>/") 
def get_factorial(n):
    fact = factorial(n)
    return jsonify({"factorial": fact, "hostname": hostname})

@factorial_routes.route("/facl/<int:n>")
@factorial_routes.route("/facl/<int:n>/") 
# Эмитация долгого выполения запроса. 
def get_factorial_latency(n):
    fact = factorial(n) 
    time.sleep(1) 
    return jsonify({"factorial": fact, "hostname": hostname})

# Эмитация долгого выполения запроса случайным образом
# Генерируем случайное число в диапазоне от 0 до 1 и проверяем, 
# если это число меньше или равно 0.01 (вероятность 1%), то задержка 1 сек.
@factorial_routes.route("/faclr/<int:n>")
@factorial_routes.route("/faclr/<int:n>/")  
def get_factorial_random_latency(n):
    fact = factorial(n)
    if random.random() <= 0.01:
        time.sleep(1)
    return jsonify({"factorial": fact, "hostname": hostname})


from decimal import Decimal
import os
import tempfile

def factorial(n):
    fact = Decimal(1)
    for i in range(1, n+1):
        fact = fact * i
    return str(fact)

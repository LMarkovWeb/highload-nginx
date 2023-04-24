from decimal import Decimal
import os
import tempfile

def factorial(n):
    fact = Decimal(1)
    for i in range(1, n+1):
        fact = fact * i
    return str(fact)

def create_files(n):
    testdir = tempfile.mkdtemp()

    for i in range(n):
        with open(os.path.join(testdir, f"file_{i}.txt"), "w") as f:
            f.write("Some data")

    for i in range(n):
        with open(os.path.join(testdir, f"file_{i}.txt"), "a") as f:
            for j in range(n):
                f.write("Some more data\n")

    result_string = f"{n} files were created and written."
    return result_string

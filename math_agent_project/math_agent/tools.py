# math_agent/tools.py
def add(a: float, b: float):
    return {"result": a + b}

def subtract(a: float, b: float):
    return {"result": a - b}

def multiply(a: float, b: float):
    return {"result": a * b}

def divide(a: float, b: float):
    if b == 0:
        return {"error": "Cannot divide by zero"}
    return {"result": a / b}


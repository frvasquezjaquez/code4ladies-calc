from fastapi import FastAPI
from calc import Calc

app = FastAPI()
calc = Calc()


@app.get("/status")
def read_root():
    return {
        "status": "funcionando"
    }

@app.get("/sumar")
def read_sumar(num1: int, num2: int):
    return {
        "total": calc.sumar(num1, num2)
    }
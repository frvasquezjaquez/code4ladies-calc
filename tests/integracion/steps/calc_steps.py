from behave import *
import api
from fastapi.testclient import TestClient

@given("que deseo sumar dos numeros")
def step_implementation(context):
    context.app =  TestClient(api.app)

@when('yo ingrese los numeros {num1} y {num2}')
def step_implementation(context, num1, num2):
    context.response = context.app.get(f'/sumar?num1={num1}&num2={num2}')
    assert 200 == context.response.status_code

@then('El resultado {result} debe ser la suma de ambos')    
def step_implementation(context, result):
    response_object = context.response.json()
    assert str(result) == str(response_object.get("total"))
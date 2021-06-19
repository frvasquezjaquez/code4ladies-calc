# Calculadora API

## Funcionalidades
    * Sumar 2 numeros
    * Restar 2 Numeros
    * Multiplicar 2 Numeros
    * Dividir 2 numneros
 
# Requirements
- Docker
- Python3


# Tests

## Run unittest + Coverage
```
coverage run --source calc calc_unittest.py
coverage report -m --fail-under=80 #Falla sino llegamos al 80% de coverage
```


## Run Integration Tests
```
behave tests/Integracion
```


# Run Static Code Analysis 
```
pylint calc.py --fail-under=7 
```
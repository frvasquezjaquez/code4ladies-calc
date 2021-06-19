"""
Clase para Calcular numeros
"""
class Calc:
    """ Definicion de Clase de Calculadora """

    def sumar(self, num1, num2):
        """
        Funcion para sumar dos numeros

        inputs:
        num1: Primer valor para sumar
        num2: Segundo valor para sumar
        """

        if num1 < 0 or num2 < 0:
            return "Invalid"
        return num1 - num2

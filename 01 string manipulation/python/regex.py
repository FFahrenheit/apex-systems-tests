"""
Areglo de "Hola%SOY*eL/aRREgLo!1"
Converir todo lo que sea mayuscula a minuscula y todo lo que no sea letras o numero en "_"
"""

from executer import Executer
import re

def main():
    tests = [
        "Hola%SOY*eL/aRREgLo!1"
    ]

    execute = Executer(tests, change_str)
    execute.run()


def change_str(string: str):
    return re.sub("[^0-9a-zA-Z]+",'_', string).lower()

if __name__ == "__main__":
    main()
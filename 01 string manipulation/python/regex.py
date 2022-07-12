"""
Areglo de "Hola%SOY*eL/aRREgLo!1"
Converir todo lo que sea mayuscula a minuscula y todo lo que no sea letras o numero en "_"

[^0-9a-zA-Z]+   <-- Que matchee de 1 a n caracteres pegados
[$$$$$$] 1 match, 1 caracter o más

[^0-9a-zA-Z]{1} <-- Que matchee solo un caracter pegado
[$][$][$][$][$][$]
"""

from executer import Executer
import re

def main():
    tests = [
        "Hola%SOY*eL/aRREgLo!1",
        "#!)#!)#)!$|||..",
        "asddfmfs",
        "123456SJSJHFIFA",
        ""
    ]

    execute = Executer(tests, change_str)
    execute.run()


def change_str(string: str):
    return re.sub("[^0-9a-zA-Z]{1}",'_', string).lower()

if __name__ == "__main__":
    main()
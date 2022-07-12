"""
Areglo de "Hola%SOY*eL/aRREgLo!1"
Converir todo lo que sea mayuscula a minuscula y todo lo que no sea letras o numero en "_"
"""

from re import A
from executer import Executer

def main():
    tests = [
        "Hola%SOY*eL/aRREgLo!1"
    ]

    execute = Executer(tests, change_str)
    execute.run()


def change_str(string: str):
    out = ''
    for char in string:
        ascii = ord(char)
        if ascii >= 65 and ascii <= 90:
            out += chr(ascii + 32)
        elif (ascii >= 97 and ascii <= 122) or (ascii >= 48 and ascii <= 57):
            out += char
        else:
            out += '_'

    return out

if __name__ == "__main__":
    main()
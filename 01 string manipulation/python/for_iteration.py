"""
Areglo de "Hola%SOY*eL/aRREgLo!1"
Converir todo lo que sea mayuscula a minuscula y todo lo que no sea letras o numero en "_"
"""

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
        if not char.isalnum():
            out += '_'
        elif char.isupper():
            out += char.lower()
        else:
            out += char
    
    return out

if __name__ == "__main__":
    main()
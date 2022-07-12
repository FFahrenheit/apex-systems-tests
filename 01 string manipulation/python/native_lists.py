"""
Areglo de "Hola%SOY*eL/aRREgLo!1"
Converir todo lo que sea mayuscula a minuscula y todo lo que no sea letras o numero en "_"
"""

from executer import Executer

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
    out = ''

    lower = "abcdefghijklmnopqrtsuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"                      #Rangos
    alphanumeric = lower + upper + numbers

    for char in string:
        if char in upper:
            out += chr(ord(char) + 32)
            out = out.lower()
        elif char not in alphanumeric:
            out += '_'
        else: 
            out += char
    
    return out

if __name__ == "__main__":
    main()
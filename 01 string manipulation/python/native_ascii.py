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

    a = "123"
    a += "456" # a = "123456"

    for char in string:             # Lo mismo
        ascii = ord(char)
        if ascii >= 65 and ascii <= 90:     # Checar si es letra mayuscula
            out += chr(ascii + 32)
        elif (ascii >= 97 and ascii <= 122) or (ascii >= 48 and ascii <= 57):       #Si es minuscula O numerico
            out += char
        else:
            out += '_'

    return out

if __name__ == "__main__":
    main()
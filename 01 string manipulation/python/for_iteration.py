"""
Areglo de "Hola%SOY*eL/aRREgLo!1"
Converir todo lo que sea mayuscula a minuscula y todo lo que no sea letras o numero en "_"

Input: "Cadena"
    Minuscula, mayuscula -> mantiene
--  Mayuscula -> Minuscula
    Cualquier otro -> _


"""

from executer import Executer

def main():
    tests = [
        "Hola%SOY*eL/aRREgLo!1",
        "#!)#!)#)!$|||..",
        "asddfmfs",
        "123456SJSJHFIFA",
        "",
        "ñññññÑÑÑÑÑ"
    ]

    execute = Executer(tests, change_str)
    execute.run()

# Lo mas sencillo y simple
# Usas funciones nativas de Python - !!!
# No te metes con codigo ASCII
# Eficiente, rapido, legible
def change_str(string: str):
    out = ''                        # Cadena vacia, generar la salida

    for char in string:
        if char.isalnum() == False:
            out += '_'              # Si no es letra o numero
        elif char.isupper():        # Si es mayuscula
            out += char.lower()     # Convertir a minuscula
        else:
            out += char
    
    return out

if __name__ == "__main__":
    main()
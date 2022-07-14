def main():
    tests = [
        [2, 3, 1, 1, 2, 4, 2, 0, 1, 1],
        [0, 1, 3, 5, 2, 7, 9, 1],
        [1, 1, 1, 1, 1, 0, 2],
        [3, 4, 2, 1, 1, 100],
        [1, 3, 6, 8, 2, 7, 1, 2, 1, 2, 6, 1, 2, 1, 2]
    ]

    for test in tests:
        steps = minimum_jumps(test)
        print(f"Cells: {test}\nSteps: {steps}\n")

"""
Greedy, explorar todos los caminos y obtener el mas corto
"""
def minimum_jumps(cells : list[int]):
    jumps = min_jump(cells, 0, len(cells) - 1)
    return -1 if jumps == float('inf') else jumps

def min_jump(cells : list[int], start : int, end : int):
    # Si nuestro inicio es el fin, entonces 0, porque estamos ahi
    # Si nuestro inicio esta despues del fin, entonces 0, porque no podemos regresar y ya lo pasamos
    if start >= end:
        return 0

    MAX = float('inf')
    # Cantidad minima de saltos desde inicio hasta fin
    min_jumps = MAX

    # Empezamos desde la segunda celda (i=1), ya que para la primera ya sabemos que es 0 (i=0)
    # Esto se repite tambien para los subproblemas, ya que no tiene sentido empezar en 0, porque es nuestro origen
    i = 1
    # Mientras haya un salto hasta nuestro origen y nuestro origen este antes que el fin
    while i <= cells[start] and i < end:
        
        # Calculamos los saltos que nos costaria desde nuestro nuevo origen hasta el final (Sumandole este salto)
        jumps_to_end = min_jump(cells, start + i, end) + 1

        # Elegimos el que sea mas corto, el actual o el nuevo calculado
        min_jumps = min(min_jumps, jumps_to_end)

        # Evaluamos el camino desde el siguiente punto de origen
        i+=1
    
    return min_jumps
    
if __name__ == '__main__':
    main()
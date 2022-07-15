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
Bottom up
"""
def minimum_jumps(cells : list[int]):
    MAX = len(cells) + 1
    jumps = [MAX for _ in cells]
    jumps[0] = 0

    # Saltamos el primer salto porque ya estamos ahi
    for i in range(1, len(cells)):
        # Desde el inicio hasta nuestro salto
        for j in range(i):
            # Podemos llegar desde j hasta i?       [j i - - -], [j - - - - i]
            # Si la posicion de origen + los posibles saltos son mayores que la posicion destino ...
            # Y para empezar, podemos llegar a la posicion de origen
            if (j + cells[j]) >= i and jumps[j] != MAX:
                # Elegimos el camino mas corto, ya sea el que ya esta puesto
                # O (lo que necesitamos para llegar al origen) + el salto desde el origen
                jumps[i] = min(jumps[i], jumps[j] + 1) 
    
    return -1 if jumps[-1] == MAX else jumps[-1]
    
if __name__ == '__main__':
    main()
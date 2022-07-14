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
    
    jumps = []
    for _ in range(len(cells)):
        jumps.append(MAX)


    # Ignoramos el primer salto porque ya estamos ahi (0 saltos para llegar al inicio)
    jumps[0] = 0    
    for idx_destiny in range(1, len(cells)):
        # Desde el inicio hasta nuestro salto
        for idx_origin in range(0, idx_destiny):
            # Podemos llegar desde j hasta i?       [j i - - -], [j - - - - i]
            # Si la posicion de origen + los posibles saltos son mayorres que la posicion destino ...
            # Y para ], podemos llegar a la posicion de destino
            possible_jumps = cells[idx_origin]
            is_reachable = jumps[idx_origin] != MAX
            
            if (idx_origin + possible_jumps) >= idx_destiny and is_reachable:
                # Elegimos el camino mas corto, ya sea el que ya esta puesto
                # O (lo que necesitamos para llegar al origen) + el salto desde el origen
                jumps_to_reach_origin = jumps[idx_origin]
                jumps[idx_destiny] = min(jumps[idx_destiny], jumps_to_reach_origin + 1) 
    
    solution = jumps[len(cells) - 1]
    if solution == MAX:
        return -1
    else:
        return solution
    
if __name__ == '__main__':
    main()
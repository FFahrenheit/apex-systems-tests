def main():
    tests = [
        [ [1, 4, 5], 9],
        [ [1, 2, 5, 10], 13],
        [ [2, 5, 10], 3],
        [ [1, 2, 5, 10, 15], 33],
        [ [1, 5, 7, 9, 11], 6],
        [ [1, 5, 7, 9, 11], 25],
        [ [1, 5, 7, 9, 11], 2]
    ]

    for test in tests:
        coins, ammount = test
        result = coin_change(coins, ammount)
        print(f"Coins: {coins}\nAmmount: {ammount}\nResult: {result}\n")

"""
Solucion bottom up
1. Crear un arreglo de ammount + 1 espacios
    este arreglo define la forma mas facil de dar n de cambio
    (desde 0 de cambio, hasta ammount de cambio [resultado])
2. Rellenar el arreglo de ammount + 1, para identificar que no hay forma de dar el cambio (por ahora)
    Rellenamos la primera posicion con 0, ya que dar $0 de cambio es dar 0 monedas, siempre va a ser así
3. Por cada moneda que tengamos para dar cambio, vamos a recorrer el arreglo
    empezando en el valor de la moneda, ya que no podemos dar cambio de menos de $n con monedas de $n (e.g. dar $3 con monedas de $5)
    hasta el final del arreglo de cambios 
4. Ahora bien, para determinar la forma de dar cambio, por cada moneda en cada posicion, compararemos si:
    El valor actual (en un inicio ammount + 1 (infinito) o 0 para la posicion 0) 
        vs 
    El arreglo de cambios en su posicion [indice actual - moneda actual] + 1
        e.g. para $8 en la moneda de $5  [      8       -       5      ] + 1
    El que sea menor sera el nuevo valor en el arreglo de cambios
5. Retornaremos el valor en la posicion [ammount] del arreglo de cambios, pero si es mayor a ammount (no hay forma de dar cambio), retornaremos -1
"""
def coin_change(coins : list[int], ammount : int):
    changes = [ ammount + 1 for _ in range(ammount + 1) ]
    changes[0] = 0

    # [1, 2, 5, 10]
    for coin in coins:
        # Recorrer el arreglo de cambios
                      # inicio, fin
        for i in range(coin, ammount + 1):
            changes[i] = min(
                changes[i],             # Actual 
                changes[i - coin] + 1)  # Moneda + lo que se necesita para llegar al target teniendo la moneda
                                        # e.g. moneda = 5, i = 10:    1 + changes[10-5] = 1 + changes[5] ...
    
    return changes[ammount] if changes[ammount] <= ammount else -1
    
if __name__ == '__main__':
    main()
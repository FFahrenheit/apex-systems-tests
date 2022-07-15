(()=>{
    const tests = [
        [2, 3, 1, 1, 2, 4, 2, 0, 1, 1],
        [0, 1, 3, 5, 2, 7, 9, 1],
        [1, 1, 1, 1, 1, 0, 2],
        [3, 4, 2, 1, 1, 100],
        [1, 3, 6, 8, 2, 7, 1, 2, 1, 2, 6, 1, 2, 1, 2]
    ];

    tests.forEach(test => {
        const jumps = minimumJumps(test);
        console.log(`Cells: ${test}\nJumps: ${jumps}\n`);
    });
})();

function minimumJumps(cells){
    const MAX = cells.length + 1;
    // const MAX = Number.MAX_VALUE;

    let jumps = [];

    cells.forEach( _ =>{
        jumps.push(MAX);
    });
    jumps[0] = 0;

    // Desde el destino
    // empezar en 1 (no tiene sentido empezar en 0, ya que es origen)
    // hasta el final del arreglo
    for(let destiny = 1; destiny < cells.length; destiny++){    //i

        // Repetir desde el origen
        // Empezando en 0 
        // Hasta una posicion antes de nuestro destino (origen != destino)
        for(let origin = 0; origin < destiny; origin++){        //j

            const possibleJumps = cells[origin];                            //cells[j]
            const isOriginReachable = jumps[origin] != MAX;                 //jumps[j] != MAX
            const isDestinyReachable = (possibleJumps + origin) >= destiny  //j + saltos >= destino

            if(isOriginReachable && isDestinyReachable){   //Podemos llegar al origen y podemos llegar
                                                            // y podemos llegar al destino desde el origen
                
                const jumpsToOrigin = jumps[origin];        // jumps[j] -- saltos para llegar al origen
                jumps[destiny] = Math.min(
                    jumps[destiny],         // Los saltos para llegar al destino actuales (lo que hay en ese momentp)
                    jumpsToOrigin + 1       // Los saltos para llegar al destino desde el origen
                );
            }

        }
    }

    return jumps[cells.length - 1] == MAX ? -1 : jumps[cells.length - 1];
}
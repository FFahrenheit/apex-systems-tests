(()=>{
    const tests = [
        [2, 3, 1, 1, 2, 4, 2, 0, 1, 1],
        [0, 1, 3, 5, 2, 7, 9, 1],
        [1, 1, 1, 1, 1, 0, 2],
        [3, 4, 2, 1, 1, 100],
        [1, 3, 6, 8, 2, 7, 1, 2, 1, 2, 6, 1, 2, 1, 2]
    ]

    tests.forEach(test => {
        const jumps = minimumJumps(test);
        console.log(`Cells: ${test}\nJumps: ${jumps}\n`);
    });
})();

function minimumJumps(cells){
    const MAX = cells.length + 1;
    let jumps = [];

    cells.forEach( _ =>{
        jumps.push(MAX);
    });
    jumps[0] = 0;

    for(let destiny = 1; destiny < cells.length; destiny++){

        for(let origin = 0; origin < destiny; origin++){

            const possibleJumps = cells[origin];
            const isOriginReachable = jumps[origin] != MAX;
            const isDestinyReachable = (possibleJumps + origin) >= destiny 

            if( isOriginReachable && isDestinyReachable){
                const jumpsToOrigin = jumps[origin];
                jumps[destiny] = Math.min(jumps[destiny], jumpsToOrigin + 1)
            }

        }
    }

    return jumps[cells.length - 1] == MAX ? -1 : jumps[cells.length - 1];
}
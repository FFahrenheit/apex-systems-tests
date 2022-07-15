(()=>{
    const tests = [
        [2, 3, 1, 1, 2, 4, 2, 0, 1, 1],
        [0, 1, 3, 5, 2, 7, 9, 1],
        [1, 1, 1, 1, 1, 0, 2],
        [3, 4, 2, 1, 1, 100],
        [1, 3, 6, 8, 2, 7, 1, 2, 1, 2, 6, 1, 2, 1, 2]
    ];

    tests.forEach(test => {
        const jumps = _minimumJumps(test);
        console.log(`Cells: ${test}\nJumps: ${jumps}\n`);
    });
})();

function _minimumJumps(cells){
    const solution = minimumJumps(cells, 0, cells.length - 1);
    return solution == Infinity ? -1 : solution;
}

function minimumJumps(cells, start, end){
    if(start >= end){
        return 0;
    }

    let minJumps = Infinity;
    
    for(let i = 1; i <= cells[start] && i < end; i++){

        const jumpsToEnd = minimumJumps(cells, start + i, end) + 1;
        
        minJumps = Math.min(minJumps, jumpsToEnd);
    }

    return minJumps;
}
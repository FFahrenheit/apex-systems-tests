(()=> {
    const tests = [
        [ [1, 4, 5], 9],
        [ [1, 2, 5, 10], 13],
        [ [2, 5, 10], 3],
        [ [1, 2, 5, 10, 15], 33]
    ]

    tests.forEach(test => {
        const coins = test[0];
        const ammount = test[1];
        const result = coinChange(coins, ammount);
        console.log(`Coins: ${coins}\nAmmount: ${ammount}\nResult: ${result.coins} (${result.solution})\n`)
    });
})();
/*
    changes = [ammount + 1 for _ in range(ammount + 1) ]
    changes[0] = 0

    for coin in coins:
        for i in range(coin, ammount + 1):
            changes[i] = min(changes[i], changes[i - coin] + 1)
    
    return changes[ammount] if changes[ammount] <= ammount else -1
*/


function coinChange(coins, ammount){
    let changes = Array.from({length: ammount + 1}, (_) => ammount + 1);
    let coinChange = Array.from({length: ammount + 1}, (_) => []);
    changes[0] = 0

    coins.forEach(coin => {

        for(let i = coin; i < ammount + 1; i++){
            const actual = changes[i];
            const newChange = changes[i - coin] + 1;
            
            if(newChange < actual){
                changes[i] = newChange;
                let changeCombination = coinChange[i - coin].map(x => x);
                changeCombination.push(coin);
                coinChange[i] = changeCombination;
            }
        }
        
    });

    return changes[ammount] > ammount ? 
        { solution: -1, coins: [] } : 
        { solution: changes[ammount], coins: coinChange[ammount]};

}
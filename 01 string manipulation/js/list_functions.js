const executer = (tests, callback) => {
    tests.forEach(test => {
        const start = performance.now();
        const result = callback(test);
        const end = performance.now();
        console.log(`Input: ${test}\nOutput:${result}\nTime: ${end - start}ns\n`);
    });
}

(()=> {
    const tests = [
        "Hola%SOY*eL/aRREgLo!1"
    ];

    executer(tests, replaceString);
})();

function replaceString(string){
    return Array.from(string)
                .map(char => {
                    const ascii = char.charCodeAt(0);
                    if(ascii >= 65 && ascii <= 90){
                        return String.fromCharCode(ascii + 32);
                    }
                    else if( (ascii >= 97 && ascii <= 122) || (ascii >= 48 && ascii <= 57)){
                        return char;
                    }else{
                        return '_';
                    }
                })
                .join('');
}
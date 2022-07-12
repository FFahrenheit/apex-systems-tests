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
    return string.replace(/[^0-9a-zA-Z]+/g, '_')
                .replace(/[A-Z]+/g, (chr) => chr.toLowerCase());
}
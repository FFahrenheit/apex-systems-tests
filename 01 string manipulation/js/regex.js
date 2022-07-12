const executer = (tests, callback) => {
    tests.forEach(test => {
        // const start = performance.now();
        const result = callback(test);
        // const end = performance.now();
        console.log(`Input: ${test}\nOutput:${result}\nTime: 0ns\n`);
    });
}

(()=> {
    const tests = [
        "Hola%SOY*eL/aRREgLo!1",
        "#!)#!)#)!$|||..",
        "asddfmfs",
        "123456SJSJHFIFA",
        "",
        "ñññññÑÑÑÑÑ"
    ];

    executer(tests, replaceString);
})();

function replaceString(string){
    return string.replace(/[^0-9a-zA-Z]{1}/g, '_').toLowerCase();
}
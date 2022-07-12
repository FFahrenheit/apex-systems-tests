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
    let out = '';
    // for(let i=0; i< string.length ; i++)
    for(const c of string){
        const ascii = c.charCodeAt(0);
        if(ascii >= 65 && ascii <= 90){
            out += String.fromCharCode(ascii + 32);
        }
        else if( (ascii >= 97 && ascii <= 122) || (ascii >= 48 && ascii <= 57)){
            out += c;
        }else{
            out += '_';
        }
    }
    return out;
}
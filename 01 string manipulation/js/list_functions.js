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
        "Hola%SOY*eL/aRREgLo!1",
        "#!)#!)#)!$|||..",
        "asddfmfs",
        "123456SJSJHFIFA",
        "",
        "ñññññÑÑÑÑÑ"
    ];

    executer(tests, replaceString);
})();


// let calificaciones = [9.4, 5.5, 6.3, 8.8, 9.1, 9.9, 10];
// let resultado = calificaciones.map(cal => Math.round(cal));

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
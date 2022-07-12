const executer = (tests, callback) => {
    tests.forEach(test => {
        const start = window.performance.now();
        const result = callback(test);
        const end = window.performance.now();
        console.log(`Input: ${test}\nOutput:${result}\nTime: ${end - start}ns\n`);
    });
}
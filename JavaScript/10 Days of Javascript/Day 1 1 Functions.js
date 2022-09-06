'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}
/*
 * Create the function factorial here
 */
/* 
//well this is after I already know python... 
function factorial(n) {
    if ( n == 0) {
        return 1
    } else {
        return n * factorial(n-1)
    }
}
*/
function factorial(n) {
    let x = 1;
    
    for (let i =1; i < n; i++) {
        x = x + (x * i);
    }
    return x;
    
}

function main() {
    const n = +(readLine());
    
    console.log(factorial(n));
}
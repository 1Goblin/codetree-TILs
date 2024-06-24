const fs = require("fs")
let n = fs.readFileSync(0).toString().trim().split(" ")

let a = Number(n[0]);
let b = Number(n[1]);

console.log(a+b);
console.log(a-b);
console.log(parseInt(a/b));
console.log(a%b);
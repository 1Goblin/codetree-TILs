const fs = require("fs");
let n = fs.readFileSync(0).toString().split("\n");

a = Number(n[0])
b = Number(n[1])

c = a+b;
console.log(c.toFixed(2))
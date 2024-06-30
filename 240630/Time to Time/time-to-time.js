const fs = require("fs")
let input = fs.readFileSync(0).toString().trim().split(" ").map(Number)

let a = (input[0]*60) + input[1]
let b = (input[2]*60) + input[3]
let c = b-a

console.log(c)
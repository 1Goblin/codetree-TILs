const fs = require("fs")
let input = fs.readFileSync(0).toString().trim().split(" ").map(Number)

let minV = Number.MIN_SAFE_INTEGER

for(let i of input){
    if(i > minV){
        minV = i
    }
}

console.log(minV)
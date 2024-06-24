const fs = require("fs")
let input = fs.readFileSync(0).toString().split("\n")

let str = "";
let sum = 0

for(let i=0; i<4; i++){
    str = input[i].split(" ").map(Number)
    sum = 0
    for(let j =0; j<4; j++){
        sum+= str[j]
    }
    console.log(sum)
}
const fs = require("fs")
let input = fs.readFileSync(0).toString().trim().split(" ").map(Number)

let sum = 0
let m = 0
let cnt = 0

for(let elem of input){
    if(elem >= 250){
        break
    }
    sum+=elem
    cnt++
}

let avg = (sum/cnt).toFixed(1)

console.log(sum, avg)
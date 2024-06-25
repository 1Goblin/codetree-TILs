const fs = require("fs")
let input = fs.readFileSync(0).toString().trim().split("\n")

let sum = 0
let arr = []
for(let i =0; i<4; i++){
    sum = 0
    arr = input[i].split(" ").map(Number)
    for(let j = 0; j<4; j++){
        sum+=arr[j]
    }
    console.log(sum)
}
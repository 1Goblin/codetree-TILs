const fs = require("fs")

let input = fs.readFileSync(0).toString().trim().split("\n")

let n = Number(input[0])
let arr = input[1].split(" ").map(Number)

let check = Array(9).fill(0)

for(let i of arr){
    check[i-1]++
}

for(let i of check){
    console.log(i)
}
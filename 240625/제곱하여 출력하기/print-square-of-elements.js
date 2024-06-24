const fs = require("fs")
let input = fs.readFileSync(0).toString().trim().split("\n")


let n = Number(input[0])
let arr = input[1].split(" ").map(Number)


let str = ""
for(let i of arr){
    str+=(i*i)+" "
}

console.log(str)
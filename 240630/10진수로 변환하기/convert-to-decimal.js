const fs = require("fs")
let input = fs.readFileSync(0).toString().trim()

let arr = input


let num = 0

for(let i = 0; i<arr.length; i++){
    num = num*2 + Number(arr[i])
}

console.log(num)
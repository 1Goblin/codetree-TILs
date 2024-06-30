const fs = require("fs")
let input = fs.readFileSync(0).toString().trim()

let [m1,d1,m2,d2] = input.split(" ").map(Number)

const num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

let a = num_of_days[m1] - d1
let b = 0

for(let i=m1+1; i<m2; i++){
    b += num_of_days[i]
}

console.log(a+b+d2+1)
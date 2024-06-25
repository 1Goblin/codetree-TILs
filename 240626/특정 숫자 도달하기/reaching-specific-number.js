const fs = require("fs")
let input = fs.readFileSync(0).toString().trim().split(" ").map(Number)

let sum = 0
let m = 0

for(let i=0; i<10; i++){
    if(input[i] >= 250){
        for(let j=0; j<i; j++){
            sum+=input[j]
        }
        m = sum/i
        break
    }
}

console.log(sum, m.toFixed(1))
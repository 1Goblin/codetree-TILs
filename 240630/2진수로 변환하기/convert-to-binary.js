const fs = require("fs")
let input = fs.readFileSync(0).toString().trim()

let n = Number(input)

let arr = []

while(true){
    if(n < 2){
        arr.push(n)
        break
    }

    arr.push(n%2)
    n = Math.floor(n/2)

}

let str=""

for(let i= arr.length-1; i>=0; i--){
    str+=arr[i]
}

console.log(str)
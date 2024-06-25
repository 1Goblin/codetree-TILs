const fs = require("fs")
let arr = fs.readFileSync(0).toString().trim().split(" ").map(Number)


for(let i =2; i<10; i++){
    arr.push((arr[i-2]+arr[i-1])%10)
}

let str=""

for(let i =0; i<10; i++){
    str+=arr[i]+" "
}

console.log(str)
const fs = require("fs")
let input = fs.readFileSync(0).toString().trim().split("\n")

let [n,m] = input[0].split(" ").map(Number)
let arr = input[1].split(" ").map(Number)

let cnt = 0

for(let i=0 ;i<n; i++){
    if(arr[i] == m){
        cnt++
    }
}

console.log(cnt)
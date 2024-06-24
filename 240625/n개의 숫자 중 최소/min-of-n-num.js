const fs = require("fs")
let input = fs.readFileSync(0).toString().trim().split("\n")

let n = Number(input[0]);
let arr = input[1].split(" ").map(Number);

let minV = Number.MAX_SAFE_INTEGER

let cnt = 0

for(let i=0; i<n; i++){
    if(arr[i]===minV){
        cnt++
    }
    if(arr[i]<minV){
        minV=arr[i]
        cnt = 1
    }
    
}

console.log(minV, cnt)
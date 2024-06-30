const fs = require("fs")
let input = fs.readFileSync(0).toString().trim().split("\n")

let [n, k] = input[0].split(" ").map(Number)

let arr = Array(n+1).fill(0)

for(let i =1; i<k+1; i++){
    let [a,b] = input[i].split(' ').map(Number)
    for(let j=a; j<b+1; j++){
        arr[j] += 1
    }
}

let maxV=0


for(let i=0; i<n+1; i++){
    if(arr[i] > maxV){
        maxV = arr[i]
    }
}
console.log(maxV)
const fs = require("fs")
let input = fs.readFileSync(0).toString().trim().split("\n")

let n = Number(input[0])
let arr = input[1].split(" ").map(Number)

let sum = 0
for(let i =0; i<n; i++){
    sum+=arr[i]
}
let avg = (sum/n).toFixed(1)

console.log(avg)

if(avg>=4.0){
    console.log("Perfect")
}else if(avg>=3.0){
    console.log("Good")
}else{
    console.log("Poor")
}
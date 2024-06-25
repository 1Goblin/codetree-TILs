const fs = require("fs")
let input = fs.readFileSync(0).toString().trim().split(" ")

let n = Number(input[0])
let m = Number(input[1])

let arr = Array(n).fill(0).map(() => Array(m).fill(0))

let cnt = 1

for(let i = 0; i<n; i++){
    for(let j =0; j<m; j++){
        arr[i][j] = cnt
        cnt++
    }
}

let str=""
for(let i =0; i<n; i++){
    str =""
    for(let j =0; j<m; j++){
        str+=arr[i][j]+" "
    }
    console.log(str)
}
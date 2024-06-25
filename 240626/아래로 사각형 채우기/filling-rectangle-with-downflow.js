const fs = require("fs")
let input = fs.readFileSync(0).toString().trim()

let n = Number(input)

let arr = Array(n).fill(0).map(()=>Array(n).fill(0))

let cnt = 1

for(let i = 0; i<n; i++){
    for(let j =0; j<n; j++){
        arr[j][i] = cnt;
        cnt++
    }
}


let str =""

for(let i=0; i<n; i++){
    str = ""
    for(let j=0; j<n; j++){
        str+=arr[i][j]+" "
    }
    console.log(str)
}
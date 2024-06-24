const fs = require("fs")

let n = fs.readFileSync(0).toString().trim()

let arr = ['L', 'E', 'B', 'R', 'O', 'S']

let ans = -1

for(let i=0; i<arr.length; i++){
    if(arr[i] === n){
        ans = i
        break
    }
}

if(ans === -1){
    console.log("None")
}
else{
    console.log(ans)
}
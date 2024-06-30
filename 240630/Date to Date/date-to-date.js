const fs = require("fs")
let input = fs.readFileSync(0).toString().trim()

let [m1,d1,m2,d2] = input.split(" ").map(Number)

const num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

let c = 0

if(m1 !== m2){
    for(let i =m1+1; i<m2; i++){
        c+=num_of_days[i] 
    }
    c += num_of_days[m1] - d1 + d2
}else{
    c = d2 - d1
}


console.log(c+1)
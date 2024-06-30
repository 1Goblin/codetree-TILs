const fs = require("fs")
let input = fs.readFileSync(0).toString().trim().split("\n")

const OFFSET = 100;
const MAX_R = 200;

const n = Number(input[0])
const segement = []

for(let i =1; i<=n; i++){
    segement.push(input[i].split(' ').map(Number))
}

const checked = Array(MAX_R + 1).fill(0)

segement.forEach(segement =>{
    let [x1, x2] = segement

    x1+=OFFSET
    x2+=OFFSET

    for(let i = x1; i<x2; i++){
        checked[i] += 1;
    }
})

console.log(Math.max(...checked))
const fs = require("fs")
let input = fs.readFileSync(0).toString().trim().split("\n")

const OFFSET = 100
const MAXSIZE = 201

let n = Number(input[0])

let segments = []

for(let i=1; i<input.length; i++){
    segments.push(input[i].split(' '))
}

let checked = Array(MAXSIZE).fill(0).map(() => Array(MAXSIZE).fill(0))


segments.forEach(element => {
    let [x1,y1, x2, y2] = element.map(Number)
    
    x1+=OFFSET
    x2+=OFFSET
    y1+=OFFSET
    y2+=OFFSET

    for(let i =x1; i<x2; i++){
        for(let j=y1; j<y2; j++){
            checked[i][j] +=1
        }
    }
})

let area = 0
for(let i=0; i<MAXSIZE; i++){
    for(let j=0; j<MAXSIZE; j++){
        if(checked[i][j] >=1){
            area+=1
        }
    }
}

console.log(area)
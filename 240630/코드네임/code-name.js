class Spy{
    constructor(codeName, score){
        this.codeName = codeName
        this.score = score
    }
}

const fs = require('fs')
let input = fs.readFileSync(0).toString().trim().split('\n')

spys = []

for(let i = 0; i<5; i++){
    let [c,s] = input[i].split(' ')
    spys.push(new Spy(c,s))
}

minS = 0

for(let i =1; i<5; i++){
    if(Number(spys[minS].score) > Number(spys[i].score)){

        minS = i
    }
}

console.log(spys[minS].codeName, spys[minS].score)
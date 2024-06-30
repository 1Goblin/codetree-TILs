class Spy{
    constructor(codeName, score){
        this.codeName = codeName
        this.score = score
    }
}

const fs = require('fs')
let input = fs.readFileSync(0).toString().trim().split('\n')

let Spys = Array(5).fill(new Spy());

for(let i=0; i<5; i++){

    let [c,s] = input[i].split(' ')
    Spys[i] = new Spy(c,s)
}
Spys.sort()
console.log(`${Spys[0].codeName} ${Spys[0].score}`)
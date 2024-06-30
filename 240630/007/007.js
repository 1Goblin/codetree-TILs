const fs = require("fs")
let input = fs.readFileSync(0).toString().trim().split(' ')

let scode = input[0]
let place = input[1]
let time = Number(input[2])

class point{

    constructor(s,p,t){
        this.s = s
        this.p = p
        this.t = t
    }
}

let p1 = new point(scode, place, time)

console.log(`secret code : ${p1.s}`)
console.log(`meeting point : ${p1.p}`)
console.log(`time : ${p1.t}`)
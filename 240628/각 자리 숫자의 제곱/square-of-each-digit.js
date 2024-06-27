const fs = require("fs")
let input = Number(fs.readFileSync(0).toString().trim())

const a = (n) => {

    if(parseInt(n/10)===0){
        return n**2
    }


    return a(parseInt(n/10)) + parseInt((n%10))**2
}

console.log(a(input))
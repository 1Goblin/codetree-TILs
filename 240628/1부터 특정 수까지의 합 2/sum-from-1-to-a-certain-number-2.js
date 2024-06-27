const fs = require("fs")
let n = Number(fs.readFileSync(0).toString().trim())

const print = (n) =>{

    if(n===1){
        return 1
    }


    return print(n-1) + n
}

console.log(print(n))
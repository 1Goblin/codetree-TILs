const fs = require("fs")
let input = fs.readFileSync(0).toString().trim()

let n = Number(input)

const print = (n) =>{

    if(n<1){
        return
    }

    console.log("HelloWorld");

    return print(n-1)
}

print(n)
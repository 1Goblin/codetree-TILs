const fs = require("fs")
let n = Number(fs.readFileSync(0).toString().trim())

const starts = (n) =>{

    if(n === 0){
        return
    }

    starts(n-1);

    for(let i = 0; i<n; i++){
        process.stdout.write("*")
    }
    console.log()
}

starts(n)
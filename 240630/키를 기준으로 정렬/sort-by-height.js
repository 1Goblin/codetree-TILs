class Student{
    constructor(name, height, weight){
        this.name = name
        this.height = height
        this.weight = weight
    }
}


const fs = require('fs')
let input = fs.readFileSync(0).toString().trim().split('\n')

let n = Number(input[0])

let students = []

for(let i=1; i<n+1; i++){
    let [n, h, w] = input[i].split(' ')
    students.push(new Student(n, Number(h), Number(w)))
}

students.sort((a,b)=>{
    return a.height - b.height
})

for(let i=0; i<n; i++){
    console.log(students[i].name, students[i].height, students[i].weight)
}
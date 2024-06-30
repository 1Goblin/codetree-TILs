class Student{
    constructor(name, kor, eng, math){
        this.name = name
        this.kor = kor
        this.eng = eng
        this.math = math
    }
}

const fs = require('fs')
let input = fs.readFileSync(0).toString().trim().split('\n')

let n = Number(input[0])
let students = []
for(let i =1; i<n+1; i++){
    let [n,k,e,m] = input[i].split(' ')
    students.push(new Student(n,Number(k),Number(e),Number(m)))
}


students.sort((a,b) =>{
    if(a.kor == b.kor){
        if(a.eng == b.eng){
            return b.math - a.math
        }
        return b.eng - a.eng
    }
    return b.kor - a.kor
})

for(let i = 0; i<n; i++){
    console.log(students[i].name, students[i].kor, students[i].eng, students[i].math)
}
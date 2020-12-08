const fs = require('fs');

let data = fs.readFileSync('day8input.txt', 'utf8');
const instructions = data.split(/\r?\n/)
const visited = instructions.map(_ => false)

function execute(instructions, visited){
    let accumulator = 0
    let index = 0
    while (visited[index] !== true){
        let command = instructions[index].split(" ")[0]
        let number = Number(instructions[index].split(" ")[1])
        console.log(command, number);
        switch (command){
            case 'acc':
                accumulator += number
                visited[index] = true
                index++
                console.log("acc : index = ", index, "accumulator = ", accumulator);
                break;
            case 'nop':
                visited[index] = true
                index++
                console.log("nop: index = ", index, "accumulator = ", accumulator);
                break;
            case 'jmp':
                visited[index] = true
                index = Math.abs(index + number)
                console.log("jmp : index = ", index, "accumulator = ", accumulator);
                break;
        }
        console.log("------------");
    }
    console.log("BROKE", visited[index] = true);
    return accumulator
}

console.log(execute(instructions, visited))

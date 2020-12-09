const fs = require('fs');
const { on } = require('process');

let data = fs.readFileSync('day8input.md', 'utf8');
const baseInstructions = data.split(/\r?\n/).map(i => i.split(" "))
const visited = baseInstructions.map(_ => false)

function execute(instructions, visited){
    let accumulator = 0
    let index = 0
    while (1){
        if (index === instructions.length){
            return ["part2", accumulator]
        }
        else if (visited[index] === true){
            return ["part1", accumulator]
        }
        let command = instructions[index][0]
        let number = Number(instructions[index][1])
        switch (command){
            case 'acc':
                accumulator += number
                visited[index] = true
                index++
                break;
            case 'nop':
                visited[index] = true
                index++
                break;
            case 'jmp':
                visited[index] = true
                index = Math.abs(index + number)
                break;
        }
        if (index > instructions.length){
            return ["error", 0]
        }
    }
}


function part2(instructions){
    for (let i = 0; i < instructions.length; i++){
        let cmd = instructions[i][0]
            if (cmd === "jmp"){
                cachedCmd = cmd
                copy = instructions.map((ins, index) => index === i ? ["nop", ins[1]] : ins)
                result = execute(copy, instructions.map(i => false))
                if (result[0] === "part2"){
                    return result
                }
            instructions[i][0] = cachedCmd

            }
            else if (cmd === "nop"){
                cachedCmd = cmd
                copy = instructions.map((ins, index) => index === i ? ["jmp", ins[1]] : ins)
                result = execute(instructions, instructions.map(i => false))
                if (result[0] === "part2"){
                    return result
                }
            instructions[i][0] = cachedCmd
        }
    }
}

console.log(execute(baseInstructions, visited))
console.log(part2(baseInstructions));

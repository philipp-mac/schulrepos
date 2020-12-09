const fs = require('fs');
const { on } = require('process');

let data = fs.readFileSync('day8input.md', 'utf8');
const baseInstructions = data.split(/\r?\n/).map(i => i.split(" "))
const visited = baseInstructions.map(_ => false)

function execute(instructions, visited){
    let accumulator = 0
    let index = 0
    while (true){
        if (index === instructions.length + 1){
            return ["part2", accumulator]
        }
        else if (visited[index] === true){
            return ["part1", accumulator]
        }
        if (instructions[index] === undefined || instructions === undefined || instructions[index][0] === undefined){
            console.log(" UNDEFINED ,", instructions);
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
                index = index + number
                break;
        }
    }
}

function findAllVisited(instructions, visited){
    let index = 0
    while (visited[index] != true){
        let command = instructions[index][0]
        let number = Number(instructions[index][1])
        switch (command){
            case 'acc':
                visited[index] = true
                index++
                break;
            case 'nop':
                visited[index] = true
                index++
                break;
            case 'jmp':
                visited[index] = true
                index = index + number
                break;
        }
    }
    return instructions.map((hit, index) => visited[index] == true ? hit : null).filter(item => item !== null)
}

function part2(instructions, visited){
    for (let i = 0; i < instructions.length; i++){
        let cmd = instructions[i][0]
            if (cmd === "jmp"){
                cachedCmd = cmd
                instructions[i][0] = "nop"
                console.log(instructions.length);
                result = execute(instructions, instructions.map(i => false))
                if (result[0] === "part2"){
                    return result
                }
            instructions[i][0] = cachedCmd

            }
            else if (cmd === "nop"){
                cachedCmd = cmd
                instructions[i][0] = "jmp"
                result = execute(instructions, instructions.map(i => false))
                if (result[0] === "part2"){
                    return result
                }
            instructions[i][0] = cachedCmd
        }
    }
}

// console.log(execute(instructions, visited))

let onlyVisitedInstructions = findAllVisited(baseInstructions, baseInstructions.map(i => false))
console.log(onlyVisitedInstructions);
console.log(part2(onlyVisitedInstructions, onlyVisitedInstructions.map(i => false)))

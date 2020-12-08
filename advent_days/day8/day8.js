const fs = require('fs');

let data = fs.readFileSync('day8input.txt', 'utf8');
const instructions = data.split(/\r?\n/)
const visited = instructions.map(_ => false)

function execute(instructions, visited){
    let steps = 0
    let accumulator = 0
    let index = 0
    while (index < instructions.length){
        let command = instructions[index].split(" ")[0]
        let number = Number(instructions[index].split(" ")[1])
        switch (command){
            case 'acc':
                accumulator += number
                visited[index] = true
                steps++
                index++
                break;
            case 'nop':
                visited[index] = true
                index++
                steps++
                break;
            case 'jmp':
                visited[index] = true
                steps++
                index = index + number
                break;
        }
    if 
    if (steps > 10000){
        return false
        }
    }
    console.log("wppp");
    return accumulator
}

function autoFixProgram(instructions) {
    // test each instruction until the program is fixed
    for (let i = 0; i < instructions.length; i++) {
        const ins = instructions[i].split(" ");
        console.log(ins);

        // skip ACCs
        if (ins[0] === 'acc') {
            continue;
        }

        // backup modified instruction to restore after
        const insBackup = ins[0];

        try {
            // flip the instruction from jmp -> nop or vice versa
            ins[0] = (ins[0] === 'jmp') ? 'nop' : 'jmp';
            console.log(ins[0]);

            // if program exited cleanly, then it is fixed
            const result = execute(instructions, instructions.map(i => false));
            if (result != false) {
                return result;
            }

        } finally {
            // fix up the instruction before looping or exiting
            ins[0] = insBackup;
        }
    }
}

// console.log(execute(instructions, visited))
console.log(autoFixProgram(instructions))

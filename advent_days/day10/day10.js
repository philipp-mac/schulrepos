const fs = require('fs');

let data = fs.readFileSync('day10input.md', 'utf8');
joltVals = data.split(/\r?\n/).map(item => parseInt(item))
joltVals.unshift(0)
joltVals.push(Math.max(...joltVals) + 3)


function swap(list, a, b){
    let temp = list[b]
    list[b] = list[a]
    list[a] = temp
}


function bubbleSort(list){
    let keepGoing = true
    while (keepGoing){
        keepGoing = false
        for (let n = 1; n < list.length; n++){
            if (list[n] < list [n - 1]){
                swap(list, n, n-1)
                keepGoing = true
            }
        }
    }
    return list
}


function getDifferences(list){
    list = bubbleSort(list)
    let oneJoltDiff = 0
    let threeJoltDiff = 0
    for (let i = 1; i < list.length; i++){
        if (list[i] - list[i - 1] === 1){
            oneJoltDiff++
        }
        else if (list[i] - list[i - 1] === 3){
            threeJoltDiff++
        }
    }
    return oneJoltDiff * threeJoltDiff
}


// function findArrangements(list){
//     let ways = new Proxy({}, {
//         get: (target, name) => name in target ? target[name] : 0
//       })
//     ways[0] = 1
//     list.forEach(v => 
//         ways[v] = ways[v - 1] + ways[v - 2] + ways[v - 3])
//     console.log(ways[0]);
//     return ways[list[-1]]
// }


console.log(getDifferences(joltVals))
// console.log(findArrangements(joltVals));
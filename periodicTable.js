const fetch = require('node-fetch')
const prompt = require('prompt-sync')({ sigint: true })
const fs = require('fs')
const path = require('path')

const avogadroNumber = 6.02214076e+23
const STPMolarVolume = 22.4

async function main() {
    const ATOMIC_NUMBER = prompt('Enter atomic number (or press enter for don\'t know): ')
    const SYMBOL = !Number.isInteger(Number(ATOMIC_NUMBER)) || ATOMIC_NUMBER.length === 0 ? prompt('Enter symbol (or press enter for don\'t know): ') : null
    const RES = !SYMBOL ? await fetch(`https://neelpatel05.pythonanywhere.com/${Number(ATOMIC_NUMBER) ? `element/atomicnumber?atomicnumber=${ATOMIC_NUMBER}` : ``}`) : await fetch(`https://neelpatel05.pythonanywhere.com/element/symbol?symbol=${SYMBOL}`)
    const DATA = await RES.json()
    console.table({ 1: 'Element data', 2: 'Calculator', 3: 'Credit and Program log' })
    const OPERATOR = Number(prompt('Enter operator: '))
    Array.isArray(DATA) ? DATA.map(data => data.atomicMass = parseFloat(data.atomicMass)) : !DATA.message ? DATA.atomicMass = parseFloat(DATA.atomicMass) : null

    switch (OPERATOR) {
        case 1: Array.isArray(DATA) ? DATA.forEach(data => console.table(data)) : console.table(DATA); break
        case 2:
            console.table({ 1: { from: 'amount', to: 'mass' }, 2: { from: 'mass', to: 'amount' }, 3: { from: 'volume', to: 'amount' }, 4: { from: 'amount', to: 'volume' }, 5: { from: 'volume', to: 'mass' }, 6: { from: 'mass', to: 'volume' }, 7: { from: 'mol', to: 'amount' }, 8: { from: 'amount', to: 'mol' } })
            const SUB_OPERATOR = Number(prompt('Enter sub operator: '))

            switch (SUB_OPERATOR) {
                case 1: console.log(parseFloat(DATA.atomicMass) * Number(prompt('Enter amount: '))); break
                case 2: console.log((1 / parseFloat(DATA.atomicMass)) * Number(prompt('Enter mass: '))); break
                case 3: console.log(Number(prompt('Enter volume: ')) / STPMolarVolume); break
                case 4: console.log(Number(prompt('Enter amount: ')) * STPMolarVolume); break
                case 5: console.log(parseFloat(DATA.atomicMass) * (Number(prompt('Enter volume: ')) / STPMolarVolume)); break
                case 6: console.log((Number(prompt('Enter mass: ')) * STPMolarVolume) / parseFloat(DATA.atomicMass)); break
                case 7: console.log(Number(prompt('Enter mol: ')) * avogadroNumber); break
                case 8: console.log(Number(prompt('Enter amount: ')) / avogadroNumber); break
                default: console.error(new TypeError(`${SUB_OPERATOR} operator is out of ranges`))
            }
            break
        case 3: console.log(fs.readFileSync(path.join(__dirname, 'program_log.md'), { encoding: 'utf-8', flag: 'r' })); break
        default: console.error(new TypeError(`${OPERATOR} operator is out of ranges`))
    }
}

main()
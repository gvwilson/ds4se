const fs = require('fs')
const acorn = require('acorn')

const data = fs.readFileSync(process.argv[2], 'utf-8')
const ast = acorn.parse(data, {
  locations: true,
  onComment: [],
  ecmaVersion: 8
})
console.log(JSON.stringify(ast, null, 2))

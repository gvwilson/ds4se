const fs = require('fs')
const acorn = require('acorn')
const walk = require('acorn-walk')

const countFile = (path) => {
  if (! fs.lstatSync(path).isFile()) {
    return {path: path, lines: null, functions: null}
  }

  const data = fs.readFileSync(path, 'utf-8')
  const lines = data.trimEnd().split('\n').length

  try {
    const ast = acorn.parse(data, {
      ecmaVersion: 8,
      sourceType: 'module'
    })

    const state = {functions: 0}
    walk.simple(ast, {
      FunctionDeclaration: (node, state) => {
        state.functions += 1
      },
      FunctionExpression: (node, state) => {
        state.functions += 1
      },
      ArrowFunctionExpression: (node, state) => {
        state.functions += 1
      }
    }, null, state)
    
    return {
      path: path,
      lines: lines,
      functions: state.functions
    }
  } catch (err) {
    return {
      path: path,
      lines: lines,
      functions: null
    }
  }
}

console.log('Path,Lines,Functions')
fs.readFileSync('/dev/stdin', 'utf-8').trimEnd().split('\n')
  .map(path => countFile(path))
  .forEach(({path, lines, functions}) => {
    console.log(`${path},${lines},${functions}`)
  })

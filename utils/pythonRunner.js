const { spawn } = require('child_process')

const pythonRunner = (pythonFile, args) => {
  return new Promise((resolve, reject) => {
    const python = spawn('python', [pythonFile, ...args])
    var FIM = []
    // var dataToSend
    python.stdout.on('data', (data) => {
      console.log('Pipe data from python script...')
      //dataToSend = data.toString()
      FIM.push(data)
    })

    python.on('close', (code) => {
      console.log(`child process all stdio with code ${code}`)
      console.log(FIM)
      resolve(FIM.join(''))
    })
  })
}

module.exports = pythonRunner

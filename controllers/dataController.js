const path = require('path')
const Data = require('../models/dataModel')
const pythonRunner = require('../utils/pythonRunner')
const util = require('util')
const { json } = require('express/lib/response')

const algorithms = [
  { algorithm: 'apriori', path: 'apriori/apriori.py' },
  { algorithm: 'fpgrowth', path: 'fpgrowth/fpgrowth.py' },
]


exports.processData = async (req, res, next) => {
  let file
  let fileFullPath
  let URL
  try {
    file = req.files.file
    const fileName = file.name
    const size = file.data.length
    const extension = path.extname(fileName)
    const allowedExtension = /csv/

    if (!allowedExtension.test(extension)) throw 'Unsupported Extension!'
    if (size > 50000000) throw 'File must be less than 5MB'

    const md5 = file.md5
    URL = '../public/uploads/' + md5 + extension

    fileFullPath = path.join(__dirname, URL)

    console.log(fileFullPath)

    fileFullPath = path.normalize(fileFullPath)
    console.log('Normalize : ' + fileFullPath)
    await util.promisify(file.mv)(fileFullPath)
  } catch (err) {
    console.log(err)
    res.status(500).json({
      message: err,
    })
  }
  const algorithm = req.body.algorithm.toLowerCase()
  const support = req.body.support
  const confidence = req.body.confidence

  scriptPath = ''

  switch (algorithm) {
    case 'apriori':
      scriptPath = 'apriori/apriori.py'
      break
    case 'fpgrowth':
      scriptPath = 'fpgrowth/fpgrowth.py'
      break
  }

  const startTime = Date.now()
  const datas = await pythonRunner('./scripts/python/' + scriptPath, [
    '-f',
    fileFullPath,
    '-s',
    support,
    '-c',
    confidence,
  ])

  const endTime = Date.now()

  const runTime = (endTime - startTime) / 1000
  console.log(runTime)
  console.log("Datas" + datas)
  
  let datasToJson;
  try{
  datasToJson = JSON.parse(datas)
  datasToJson.runTime = runTime
  //console.log(datasToJson)
  }catch(err){
  console.log(err)
  datasToJson = {
    "message" : "No frequent item set"
  }
}
  res.json(datasToJson)
  //res.send(datas)
}

exports.compareAllAlgorithms = async (req, res, next) => {
  let file
  let fileFullPath
  let URL
  try {
    file = req.files.file
    const fileName = file.name
    const size = file.data.length
    const extension = path.extname(fileName)
    const allowedExtension = /csv/

    if (!allowedExtension.test(extension)) throw 'Unsupported Extension!'
    if (size > 50000000) throw 'File must be less than 5MB'

    const md5 = file.md5
    URL = '../public/uploads/' + md5 + extension

    fileFullPath = path.join(__dirname, URL)

    console.log(fileFullPath)

    fileFullPath = path.normalize(fileFullPath)
    console.log('Normalize : ' + fileFullPath)
    await util.promisify(file.mv)(fileFullPath)
  } catch (err) {
    console.log(err)
    res.status(500).json({
      message: err,
    })
  }
  //const algorithm = req.body.algorithm.toLowerCase()
  const support = req.body.support
  const confidence = req.body.confidence

  const runTimeAlgorithms = []

  for (let algorithm of algorithms) {
    const startTime = Date.now()
    const datas = await pythonRunner('./scripts/python/' + algorithm.path, [
      '-f',
      fileFullPath,
      '-s',
      support,
      '-c',
      confidence,
    ])

    const endTime = Date.now()

    const runTime = (endTime - startTime) / 1000
    runTimeAlgorithms.push({ algorithm: algorithm.algorithm, runTime: runTime })
  }

  res.json(runTimeAlgorithms)
  //res.send(datas)
}
exports.test = async (req, res, next) => {
  const datas = await pythonRunner('./scripts/python/apriori/apriori.py', [
    // '-f',
    // './public/uploads/tesco2.csv',
    // '-s',
    // '0.1',
    // '-c',
    // '0.1',
  ])

  //console.log(datas)
  //res.send(datas)
  datasToJson = JSON.parse(datas)
  res.json(datasToJson)
}

const path = require('path')
const Data = require('../models/dataModel')
const pythonRunner = require('../utils/pythonRunner')
const util = require('util')

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
  const algorithm = req.body.algorithm
  const support = req.body.support
  const confidence = req.body.confidence

  const datas = await pythonRunner('./scripts/python/utils.py', [
    '-f',
    fileFullPath,
    '-s',
    support,
    '-c',
    confidence,
  ])

  console.log(datas)
  // res.json(datas)
  res.send(datas)
}

exports.test = async (req, res, next) => {
  const datas = await pythonRunner('./scripts/python/utils.py', [
    '-f',
    './public/uploads/tesco2.csv',
    '-s',
    '0.1',
    '-c',
    '0.1',
  ])

  console.log(datas)
  res.send(datas)
}

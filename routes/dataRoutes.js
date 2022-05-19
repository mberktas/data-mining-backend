const express = require('express')
const router = express.Router()
const dataController = require('../controllers/dataController')

//router.post('/mining', dataController.mining)

router.get('/test', dataController.test)
router.post('/data', dataController.processData)
router.post('/compare', dataController.compareAllAlgorithms)
module.exports = router



const express = require('express')
const router = express.Router()
const dataController = require('../controllers/dataController')

//router.post('/mining', dataController.mining)

router.post('/test', dataController.test)
router.post('/data', dataController.processData)
module.exports = router

const express = require('express')
const bodyParser = require('body-parser')
const cors = require('cors')
const fileUplaod = require('express-fileupload')

const app = express()

const AppError = require('./utils/appError')
const dataRoutes = require('./routes/dataRoutes')

app.use(fileUplaod())
app.use(cors())
app.use(bodyParser.urlencoded({ extended: true }))

app.use('/api/', dataRoutes)

app.use('*', (req, res, next) => {
  const err = new AppError(404, 'fail', 'undefined route')
  next(err, req, res, next)
})

app.listen(3000)

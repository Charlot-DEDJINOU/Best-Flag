const express = require('express');
const app = express();
const apiRoutes = require('./routes/api');
const routemap = require('express-routemap');

app.use(express.json());
// app.use(cors)
app.use(express.urlencoded({ extended: true }));

app.use('/api', apiRoutes);

routemap(app);

module.exports = app;
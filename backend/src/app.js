const express = require('express');
const app = express();
const cors = require('cors');
const swaggerUi = require('swagger-ui-express');
const swaggerSpec = require('./config/swaggerOptions');

const apiRoutes = require('./routes/api');
const routemap = require('express-routemap');

app.use(express.json());
app.use(express.urlencoded({ extended: true }));


app.use(cors({
    origin: '*',
    credentials: false
}));

app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerSpec));
app.use('/api', apiRoutes);

routemap(app);

module.exports = app;
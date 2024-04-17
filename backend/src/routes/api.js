const express = require('express');
const router = express.Router();
const authMiddleware = require('../middlewares/authMiddleware');
const userController = require('../controllers/userController');
const infoController = require('../controllers/infoController');
const cryptController = require('../controllers/cryptController')

router.get('/', infoController.getInfos);
router.post(process.env.REGISTER_ROUTE, userController.register);
router.post('/login', userController.login);

router.use(authMiddleware);

router.get('/ascii', cryptController.getAsciiKey);
router.put('/user', infoController.getMoreInfos);
router.post('/offset', cryptController.getAuthorization);
router.put(process.env.UPDATE_ROUTE, userController.update);

module.exports = router;
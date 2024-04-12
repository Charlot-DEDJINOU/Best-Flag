const express = require('express');
const router = express.Router();
const authMiddleware = require('../middlewares/authMiddleware');
const userController = require('../controllers/userController');

router.get('/', userController.getInfos)
router.post(process.env.REGISTER_ROUTE, userController.register);
router.post('/login', userController.login);

router.use(authMiddleware);

router.get('/ascii', userController.getAsciiKey)
router.get('/update', userController.getMoreInfos);
router.put(process.env.UPDATE_ROUTE, userController.update);

module.exports = router;
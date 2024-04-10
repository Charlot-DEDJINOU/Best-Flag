const express = require('express');
const router = express.Router();
const authMiddleware = require('../middlewares/authMiddleware');
const userController = require('../controllers/userController');

router.get('/', userController.getInfos)
router.post('/aqwzsedcvfrtgbnhyujkiolmp', userController.register);
router.post('/login', userController.login);

router.use(authMiddleware);

router.get('/update', userController.getMoreInfos);
router.put('/bjkloirtghdbchauiomsfhwad', userController.update);

module.exports = router;
const express = require('express');
const router = express.Router();
const authMiddleware = require('../middlewares/authMiddleware');
const cryptController = require('../controllers/cryptController')



router.use(authMiddleware);

router.get('/ascii', cryptController.getAsciiKey);
router.post('/offset', cryptController.getAuthorization);

module.exports = router;
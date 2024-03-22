const User = require('../models/userModel');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');

exports.register = async (req, res) => {
    try {
      const { username, password } = req.body;
      const hashedPassword = await bcrypt.hash(password, 10);
      const newUser = await User.create({
        username,
        password: hashedPassword,
      });
      res.status(201).json({ message: 'User created successfully', user: newUser });
    } catch (error) {
      res.status(500).json({ error: error.message });
    }
}

exports.login = async (req, res) => {
    try {
      const { username, password } = req.body;
      const user = await User.findOne({ where: { username } });
      if (!user) {
        return res.status(401).json({ message: 'Authentication failed' });
      }
      const isMatch = await bcrypt.compare(password, user.password);
      if (!isMatch) {
        return res.status(401).json({ message: 'Authentication failed' });
      }
      const token = jwt.sign({ userId: user.id }, 'secretKey', { expiresIn: '15m' });
      res.status(200).json({ message: 'Authentication successful', token });
    } catch (error) {
      res.status(500).json({ error: error.message });
    }
}
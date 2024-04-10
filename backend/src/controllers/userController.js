const User = require('../models/userModel');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');

exports.register = async (req, res) => {
    try {
      const { username, password } = req.body;
      const hashedPassword = await bcrypt.hash(password, 10);
      const newUser = new User({
        username,
        password: hashedPassword,
      });
      await newUser.save();
      res.status(201).json({ message: 'User created successfully', user: newUser });
    } catch (error) {
      res.status(500).json({ error: error.message });
    }
}

exports.login = async (req, res) => {
    try {
      const { username, password } = req.body;
      const user = await User.findOne({ username });
      if (!user) {
        return res.status(401).json({ message: 'Authentication failed' });
      }
      const isMatch = await bcrypt.compare(password, user.password);
      if (!isMatch) {
        return res.status(401).json({ message: 'Authentication failed' });
      }
      const token = jwt.sign({ userId: user._id }, 'secretKey', { expiresIn: '15m' });
      res.status(200).json({ message: 'Authentication successful', token, user });
    } catch (error) {
      res.status(500).json({ error: error.message });
    }
}

exports.update = async (req, res) => {
  try {
      const { id } = req.params; 
      const { username, password, admin } = req.body;

      const user = await User.findById(id);
      if (!user) {
          return res.status(404).json({ message: 'User not found' });
      }

      user.username = username;
      user.admin = admin;
      user.password = await bcrypt.hash(password, 10);

      await user.save();

      res.status(200).json({ message: 'User updated successfully', user });
  } catch (error) {
      res.status(500).json({ error: error.message });
  }
};


exports.getInfos = async (req, res) => {
    res.status(200).json({
      "/login" : "Route pour la connexion",
      "/aqwzsedcvfrtgbnhyujkiolmp" : "Route pour la creation de compte"
    })
}

exports.getMoreInfos = async (req, res) => {
  res.status(200).json({
    "/login" : "Route pour la connexion",
    "/aqwzsedcvfrtgbnhyujkiolmp" : "Route pour la creation de compte",
    "/bjkloirtghdbchauiomsfhwad" : "Route pour la mise d'un utilisateur",
    "Exemple Objet user" : {
        username : "Charlot DEDJINOU",
        password : "Nerys@apzoeiruty#2004@04#25"
    }
  })
}
const User = require('../models/userModel');

exports.update = async (req, res) => {
  try {
      const { id } = req.params; 
      const { admin } = req.body;

      const user = await User.findById(id);
      if (!user) {
          return res.status(404).json({ message: 'User not found.' });
      }

      user.admin = admin;
      await user.save();

      res.status(200).json({ message: 'User updated successfully', user });
  } catch (error) {
      res.status(500).json({ error: error.message });
  }
};
const app = require('./src/app');
const sequelize = require('./src/config/sequelize');

// Synchronisation du modèle avec la base de données
sequelize.sync({ force: false })
  .then(() => {
    console.log('Database synchronized');
    app.listen(8000, () => {
      console.log('Server is running on port 8000');
    });
  })
  .catch((error) => {
    console.error('Database synchronization error:', error);
});
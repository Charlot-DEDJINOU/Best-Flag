exports.getInfos = async (req, res) => {
    res.status(200).json({
      "/login" : "Route pour la connexion",
      [process.env.REGISTER_ROUTE] : "Route pour la creation de compte"
    })
}

exports.getMoreInfos = async (req, res) => {
  res.status(200).json({
      "/login": "Route pour la connexion",
      [process.env.REGISTER_ROUTE]: "Route pour la création de compte",
      [process.env.UPDATE_ROUTE]: "Route pour la mise à jour d'un utilisateur",
      "Exemple Objet user": {
          username: "Charlot DEDJINOU",
          password: "Nerys@apzoeiruty#2004@04#25",
          admin : false
      }
  });
};
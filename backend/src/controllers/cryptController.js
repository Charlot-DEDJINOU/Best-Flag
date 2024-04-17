const User = require('../models/userModel');

exports.getAsciiKey = async (req, res) => {
    res.status(200).json({
      "key" : process.env.ASCII_KEY
    })
}
  
exports.getAuthorization = async (req, res) => {

    const { key1, key2, id } = req.body;
    const authorization = [true,false,false,false]

    if(process.env.KEY_1 == key1) 
        authorization[1] = true
    if(process.env.KEY_2 == key2)
        authorization[2] = true

    const user = await User.findById(id);
    if(user.admin)
        authorization[3] = true

    if(authorization[0] === true && authorization[1] === true && authorization[2] === true && authorization[3] ===  true)
        res.status(200).json({ message : process.env.OFFSET, authorization });
    else {
        let num = 0
        for(let item of authorization) {
            if(item) num += 1
        }
        res.status(200).json({ message : `Encore ${4 - num} autorisations.`, authorization })
    }
}
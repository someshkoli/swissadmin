const mongoose = require('mongoose'); 

const pcSchema = mongoose.Schema({
    name:  String,
    username: String,
    password: String,
    lab: String,
    address: String
});

module.exports = mongoose.model("PC",pcSchema);
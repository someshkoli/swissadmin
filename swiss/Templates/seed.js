const PC = require("./models/pcModel");
const mongoose = require("mongoose");

mongoose.connect("mongodb://localhost/pcsDB", { useNewUrlParser: true });

let data = [
    {
        name: "Test PC 1",
        lab: "1",
        address: "192.168.0.1"
    },
    {
        name: "Test PC 2",
        lab: "4",
        address: "192.168.0.2"
    }
]

const seed = () => {
    data.forEach(seed => {
        PC.create(seed, (err,pcData) => {
            if(err) {
                console.log(err);
            } else {
                console.log("Added PC successfully!");
            }
        });
    })
}

seed()

module.exports = seed;
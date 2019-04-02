const express = require("express");
const app = express();
const mongoose = require("mongoose");
const path = require("path");
const PC = require("./models/pcModel");

//========================
// MongoDB setup
//========================
mongoose.connect("mongodb://localhost/pcsDB", { useNewUrlParser: true });

//=======================
// View engine setup
//=======================
app.set('views', path.resolve(__dirname, 'views'));
app.set('view engine', 'ejs');

app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(express.static(path.join(__dirname, 'public')));

//======================
//     ROUTES
//======================

app.get("/", (req,res) => {
    PC.find({},(err,pcs) => {
        if(err) return console.log(err);
        console.log(pcs)
        res.render("index", {pcs:pcs});
    });
});

app.get("/info/:id", (req,res) => {
    PC.find({_id: req.params.id}, (err,pcs) => {
        if(err) return console.log(err);
        res.render("info", {pcs:pcs});
    });
});

//======================
//   STARTING SERVER
//======================

app.listen(3000, () => {
    console.log('App listening on port 3000!');
});
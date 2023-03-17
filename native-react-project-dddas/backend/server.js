const express = require('express');
const cors = require('cors');
const mongoose = require('mongoose');

require('dotenv').config(); // configures for .env file

const app = express(); // for express server
const port = process.env.PORT || 5000;

app.use(cors()); // cors middleware, allow to parse json files
app.use(express.json());

const uri = process.env.ATLAS_URI; // get mongodb uri from dotenv
mongoose.connect(uri, { useNewUrlParser: true }); // start connection
const connection = mongoose.connection;
connection.once('open', () => {
    console.log("MongoDB database connection established successfully");
})

const alertRouter = require('./routes/alerts');
const usersRouter = require('./routes/users');

app.use('/alerts', alertRouter); // at /alerts, load alerts
app.use('/users', usersRouter);

app.listen(port, () => { // starts server
    console.log(`Server is running on port: ${port}`);
});
//The packages this server is using
const express = require('express');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 5000;

app.use(express.json()); //Remove if we're not going to use json

// Endpoints go here
app.get('/', function (req, res) {
    //Do stuff
    res.send('Hello World'); //send something back as a test
});


// Start the server
app.listen(PORT, () => console.log('Server is running on port ' + PORT));

//Note: to run server type 'npm run start' in terminal
// If dev type 'npm run dev' in terminal for nodemon server
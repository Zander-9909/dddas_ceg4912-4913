const router = require('express').Router();
const bcrypt = require('bcrypt');
const saltRounds = 10;
let User = require('../models/user.model');

router.route('/').get((req, res) => {
    User.find()
        .then(users => res.json(users))
        .catch(err => res.status(400).json('Error: ' + err));
});


router.route('/add').post((req, res) => {
    const { username, firstName, lastName, email, password } = req.body; // destructuring the request body

    bcrypt.hash(password, saltRounds, (err, hash) => {
        if (err) {
            console.error(err);
            return res.status(500).json({ message: 'Server error' });
        }

        const newUser = new User({ username, firstName, lastName, email, password: hash }); // create a new user object with the hashed password

        newUser.save()
            .then(() => res.json('User added!'))
            .catch(err => res.status(400).json('Error: ' + err));
    });
});

// http://localhost:5000/users/add
// {
// 	"username":"boryukenneth",
// 	"firstName":"Kenneth",
// 	"lastName":"Chen",
// 	"email":"kchen158@uottawa.ca",
// 	"password":"dddas0"
// }

router.route('/signin').post(async (req, res) => {
    const { username, password } = req.body;

    try {
        const user = await User.findOne({ username });
        if (!user) {
            return res.status(400).json({ message: 'User not found' });
        }

        const isMatch = await bcrypt.compare(password, user.password); // unhashing
        if (!isMatch) {
            return res.status(401).json({ message: 'Incorrect password' });
        }

        res.status(200).json({ message: 'Signin successful', user });
    } catch (error) {
        console.error(error);
        
        res.status(500).json({ message: 'Server error' });
    }
});

// http://localhost:5000/users/signin
// {
// 	"username":"boryukenneth",
// 	"password":"dddas0"
// }

module.exports = router;
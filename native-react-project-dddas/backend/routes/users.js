const router = require('express').Router();
const bcrypt = require('bcrypt');
let User = require('../models/user.model');


router.route('/').get((req, res) => {
    User.find()
        .then(users => res.json(users))
        .catch(err => res.status(400).json('Error: ' + err));
});

router.route('/add').post((req, res) => {
    const { username, firstName, lastName, email, password } = req.body; // destructuring the request body

    const newUser = new User({ username, firstName, lastName, email, password }); // creating a new user object with properties from the request body

    newUser.save()
        .then(() => res.json('User added!'))
        .catch(err => res.status(400).json('Error: ' + err));
});

router.route('/signin').post(async (req, res) => {
    const { username, password } = req.body;

    try {
        const user = await User.findOne({ username });
        if (!user) {
            return res.status(400).json({ message: 'User not found' });
        }

        const isMatch = await bcrypt.compare(password, user.password);
        if (!isMatch) {
            return res.status(400).json({ message: 'Incorrect password' });
        }

        res.status(200).json({ message: 'Signin successful', user });
    } catch (error) {
        console.error(error);
        
        res.status(500).json({ message: 'Server error' });
    }
});


module.exports = router;
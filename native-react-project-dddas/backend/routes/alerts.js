const router = require('express').Router();
let Alert = require('../models/alert.model');

router.route('/').get((req, res) => {
    Alert.find()
        .then(alerts => res.json(alerts))
        .catch(err => res.status(400).json('Error: ' + err));
});

router.route('/add').post((req, res) => {
    const username = req.body.username;
    const date = Date.parse(req.body.date);
    const alerts = req.body.alerts;

    const newAlert = new Alert({
        username,
        date,
        alerts,
    });

    newAlert.save()
        .then(() => res.json('Alert added!'))
        .catch(err => res.status(400).json('Error: ' + err));
});

router.route('/:id').get((req, res) => {
    Alert.findById(req.params.id)
        .then(alert => res.json(alert))
        .catch(err => res.status(400).json('Error: ' + err));
});

router.route('/:id').delete((req, res) => {
    Alert.findByIdAndDelete(req.params.id)
        .then(() => res.json('Alert deleted.'))
        .catch(err => res.status(400).json('Error: ' + err));
});

router.route('/update/:id').post((req, res) => {
    Alert.findById(req.params.id)
        .then(alert => {
            alert.username = req.body.username;
            alert.description = req.body.description;
            alert.duration = Number(req.body.duration);
            alert.date = Date.parse(req.body.date);

            alert.save()
                .then(() => res.json('Alert updated!'))
                .catch(err => res.status(400).json('Error: ' + err));
        })
        .catch(err => res.status(400).json('Error: ' + err));
});

module.exports = router;
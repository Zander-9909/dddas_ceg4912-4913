const mongoose = require('mongoose');

const Schema = mongoose.Schema;

const alertSchema = new Schema({
    username: { type: String, required: true },
    date: { type: Date, required: true },
    alert: [{
        time: { type: String, required: true },
        date: { type: Date, required: true },
        isActive: { type: Boolean, default: true },
    }]
}, {
    timestamps: true,
});

const Alert = mongoose.model('Alert', alertSchema);

module.exports = Alert;
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const PORT = 3000;

// Middleware
app.use(bodyParser.json());
app.use(cors());

// MongoDB Connection
const MONGO_URI = 'mongodb+srv://kalu4134:R9AT3CMwdtUuWF4X@cluster0.thv3w.mongodb.net/playlistDB?retryWrites=true&w=majority';
mongoose.connect(MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Connected to MongoDB'))
    .catch(err => console.log(err));

// MongoDB Schema and Model
const playlistSchema = new mongoose.Schema({
    name: String,
    url: String
});

const Playlist = mongoose.model('Playlist', playlistSchema);

// Routes

// Get all playlists
app.get('/api/playlists', async (req, res) => {
    const playlists = await Playlist.find();
    res.json(playlists);
});

// Add a playlist
app.post('/api/playlists', async (req, res) => {
    const { name, url } = req.body;
    const newPlaylist = new Playlist({ name, url });
    await newPlaylist.save();
    res.json({ message: 'Playlist added successfully' });
});

// Delete a playlist
app.delete('/api/playlists/:id', async (req, res) => {
    const { id } = req.params;
    await Playlist.findByIdAndDelete(id);
    res.json({ message: 'Playlist deleted successfully' });
});

// Start Server
module.exports = app;

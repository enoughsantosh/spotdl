const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');

const app = express();
app.use(express.json());
app.use(cors());

// MongoDB Atlas connection string
const MONGO_URI = 'mongodb+srv://kalu4134:R9AT3CMwdtUuWF4X@cluster0.mongodb.net/playlistDB?retryWrites=true&w=majority';

mongoose.connect(MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Connected to MongoDB Atlas'))
    .catch((error) => console.error('Error connecting to MongoDB Atlas:', error));

// Playlist Schema
const playlistSchema = new mongoose.Schema({
    Id: { type: String, unique: true },
    title: String,
    cover: String,
});

const Playlist = mongoose.model('Playlist', playlistSchema);

// API Routes
app.post('/api/playlists', async (req, res) => {
    const { Id, title, cover } = req.body;
    try {
        const exists = await Playlist.findOne({ Id });
        if (exists) return res.status(400).send('Playlist already exists');

        const playlist = new Playlist({ Id, title, cover });
        await playlist.save();
        res.status(201).send('Playlist saved successfully');
    } catch (error) {
        res.status(500).send('Error saving playlist');
    }
});

app.get('/api/playlists', async (req, res) => {
    try {
        const playlists = await Playlist.find();
        res.status(200).json(playlists);
    } catch (error) {
        res.status(500).send('Error fetching playlists');
    }
});

app.delete('/api/playlists/:id', async (req, res) => {
    const { id } = req.params;
    try {
        await Playlist.findOneAndDelete({ Id: id });
        res.status(200).send('Playlist deleted successfully');
    } catch (error) {
        res.status(500).send('Error deleting playlist');
    }
});

const PORT = 5000;
app.listen(PORT, () => console.log(`Server running on http://localhost:${PORT}`));

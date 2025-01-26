
import os
from flask import Flask, request, jsonify, send_file
from spotdl.search import search_song
from spotdl.download.downloader import download_songs

app = Flask(__name__)

# Ensure downloads directory exists
DOWNLOAD_DIR = 'downloads'
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

@app.route('/download', methods=['POST'])
def download_song():
    try:
        # Get song ID from request
        data = request.json
        song_id = data.get('song_id')
        
        if not song_id:
            return jsonify({"error": "No song ID provided"}), 400
        
        # Search for the song
        search_result = search_song(song_id)
        
        if not search_result:
            return jsonify({"error": "Song not found"}), 404
        
        # Download the song
        download_result = download_songs([search_result], output_path=DOWNLOAD_DIR)
        
        if not download_result:
            return jsonify({"error": "Download failed"}), 500
        
        # Get the downloaded file path
        downloaded_file = os.path.join(DOWNLOAD_DIR, os.listdir(DOWNLOAD_DIR)[0])
        
        # Return the file
        return send_file(downloaded_file, as_attachment=True)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


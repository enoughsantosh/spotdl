import os
import spotdl
from flask import Flask, request, send_file

app = Flask(__name__)

def download_spotify_track(url, download_directory="downloads"):
    # Ensure the download directory exists
    if not os.path.exists(download_directory):
        os.makedirs(download_directory)

    # Download the track or playlist
    os.system(f"spotdl {url} --output {download_directory}")

@app.route("/download", methods=["GET"])
def download():
    track_url = request.args.get("url")
    if not track_url:
        return {"error": "No URL provided"}, 400
    
    # Download the track
    download_spotify_track(track_url)

    # Get the downloaded file's name (assuming the file is named after the track)
    track_name = track_url.split("/")[-1] + ".mp3"
    file_path = os.path.join("downloads", track_name)

    # Check if the file exists and return it
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return {"error": "File not found"}, 404

if __name__ == "__main__":
    app.run(debug=True)

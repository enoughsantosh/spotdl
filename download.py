import os
import subprocess
from flask import Flask, request, send_file

app = Flask(__name__)

def download_spotify_track(url, download_directory="downloads"):
    if not os.path.exists(download_directory):
        os.makedirs(download_directory)

    # Use subprocess to run the spotdl command
    command = f"spotdl {url} --output {download_directory}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    # Log the command output to help with debugging
    print(result.stdout)
    print(result.stderr)

@app.route("/download", methods=["GET"])
def download():
    track_url = request.args.get("url")
    if not track_url:
        return {"error": "No URL provided"}, 400

    # Download the track
    download_spotify_track(track_url)

    # Extract track name from URL (this is just an example, adjust as necessary)
    track_name = track_url.split("/")[-1] + ".mp3"
    file_path = os.path.join("downloads", track_name)

    # Check if the file exists
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return {"error": "File not found"}, 404
@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Spotify Downloader API! Use /download?url=<spotify_track_url> to download a track."
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)

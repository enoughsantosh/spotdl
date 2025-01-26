import os
import spotdl
from http.server import BaseHTTPRequestHandler

# Set the cache directory for spotdl
os.environ["SPOTDL_CACHE_DIR"] = "./.spotdl_cache"

def download_spotify_track(track_id, download_directory="downloads"):
    # Construct the full Spotify track URL using the track ID
    url = f"https://open.spotify.com/track/{track_id}"

    # Ensure the download directory exists
    if not os.path.exists(download_directory):
        os.makedirs(download_directory)

    # Ensure the cache directory exists
    if not os.path.exists(os.environ["SPOTDL_CACHE_DIR"]):
        os.makedirs(os.environ["SPOTDL_CACHE_DIR"])

    # Download the track
    os.system(f"spotdl {url} --output {download_directory}")

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Get the track ID from the query parameters
        query = self.path.split("?")
        if len(query) > 1:
            params = query[1]
            track_id = params.split("=")[1]  # Extracting track_id parameter

            # Call the download function
            try:
                download_spotify_track(track_id)
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(b"Track downloaded successfully!")
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(f"Error: {str(e)}".encode())
        else:
            self.send_response(400)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Missing track_id parameter.")

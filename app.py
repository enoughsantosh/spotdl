from fastapi import FastAPI, Request
import requests

app = FastAPI()

def fetch_first_video(query):
    search_url = f"https://ytsearch-three.vercel.app/search?query={query}"
    try:
        response = requests.get(search_url)
        response.raise_for_status()
        data = response.json()
        if data.get("success") and data.get("results"):
            first_result = data["results"][0]
            return {
                "title": first_result["title"],
                "channel": first_result["channel"],
                "video_id": first_result["video_id"],
                "thumbnail": first_result["thumbnail"]
            }
        else:
            return {"error": "No results found."}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def fetch_audio(video_id):
    music_url = "https://y2-indol.vercel.app/api/convert"
    payload = {"link": f"https://www.youtube.com/watch?v={video_id}"}
    try:
        response = requests.post(music_url, json=payload, headers={"Content-Type": "application/json"})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

@app.post("/search-and-convert")
async def search_and_convert(request: Request):
    data = await request.json()
    query = data.get("query")
    if not query:
        return {"error": "Query is required"}
    
    video_data = fetch_first_video(query)
    if "error" in video_data:
        return video_data
    
    audio_data = fetch_audio(video_data["video_id"])
    return {
        "video": video_data,
        "audio": audio_data
    }

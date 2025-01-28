# YouTube Search and Convert API

A simple API that searches YouTube for a given query and returns video information along with a downloadable audio URL.

## API Endpoint

```
POST https://spot-steel.vercel.app/search-and-convert
```

## Features

- Search YouTube videos by query
- Get video details (title, channel, video ID, thumbnail)
- Generate downloadable audio URL for the first search result
- Automatic conversion to MP3 format

## Usage

### Request

- Method: `POST`
- Content-Type: `application/json`
- Endpoint: `https://spot-steel.vercel.app/search-and-convert`

Request body:
```json
{
  "query": "Your search query here"
}
```

### Example Request

```bash
curl -X POST 'https://spot-steel.vercel.app/search-and-convert' \
-H 'Content-Type: application/json' \
-d '{
  "query": "Line without a hook"
}'
```

### Response

The API returns a JSON object containing two main sections:
1. `video`: Information about the found YouTube video
2. `audio`: Details about the converted audio file

Example response:
```json
{
  "video": {
    "title": "Ricky Montgomery - Line Without a Hook (Official Lyric Video)",
    "channel": "Ricky Montgomery",
    "video_id": "8JW6qzPCkE8",
    "thumbnail": "https://img.youtube.com/vi/8JW6qzPCkE8/hqdefault.jpg"
  },
  "audio": {
    "filename": "Ricky Montgomery - Line Without a Hook (Official Lyric Video) - Ricky Montgomery.mp3",
    "status": "tunnel",
    "url": "https://dl09.yt-dl.click/tunnel?id=hVzsya1sVfWVwGVceSPSQ&exp=1738008660674&sig=BKqhQS57YObHqNG-aahznudeJW27s0AHrMSQWPIa-hU&sec=0oZY4vvGEZf_odIr8_4g8v-l_LYwxr6EWjvD0InWWcU&iv=UfJEUIMV5WPZdJYTCskRQw"
  }
}
```

### Response Fields

#### Video Object
- `title`: The title of the YouTube video
- `channel`: The channel name
- `video_id`: YouTube video identifier
- `thumbnail`: URL of the video thumbnail

#### Audio Object
- `filename`: Generated filename for the audio file
- `status`: Current status of the audio conversion
- `url`: Download URL for the converted audio file

## Error Handling

The API will return appropriate HTTP status codes and error messages in case of:
- Invalid requests
- Video not found
- Conversion failures
- Server errors

## Rate Limiting

Please be mindful of rate limiting and use the API responsibly.

## Legal Notice

This API is for educational purposes only. Please ensure you have the right to download and convert any content before using this service. Respect YouTube's terms of service and content creators' rights.

## Contributing

Feel free to open issues or submit pull requests if you find any bugs or have suggestions for improvements.


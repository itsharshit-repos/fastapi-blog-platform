from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

posts: list[dict] = [
    {
        "id": 1,
        "author": "vishu",
        "title": "Fastapi is awesome!",
        "content": "This framework is really easy",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Jane doe",
        "title": "Python is great",
        "content": "Python is a great language",
        "date_posted": "April 21, 2025",
    },
]

@app.get("/", response_class=HTMLResponse)
def home():
    return f"<h1>{posts[0]['title']}</h1>"

@app.get("/api/posts")
def get_posts():
    return posts
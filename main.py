from fastapi import FastAPI

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

@app.get("/")
def home():
    return {"message": "hello world"}

@app.get("/api/posts")
def get_posts():
    return posts
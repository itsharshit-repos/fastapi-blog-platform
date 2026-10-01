from fastapi import FastAPI, Request, HTTPException, status
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

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

@app.get("/", include_in_schema=False, name="home")
@app.get("/posts", include_in_schema=False, name="posts")
def home(request: Request):
    return templates.TemplateResponse(request, 
                                      "home.html", 
                                      {"posts": posts, "title": "Home"})

@app.get("/api/posts")
def get_posts():
    return posts

@app.get("/posts/{post_id}", include_in_schema=False)
def get_post(request: Request , post_id: int):
    for post in posts:
        if post.get("id") == post_id:
            title = post["title"][:50]
            return templates.TemplateResponse(request, 
                                                  "post.html", 
                                                  {"post": post, "title": title})
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
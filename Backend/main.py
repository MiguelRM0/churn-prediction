from fastapi import FastAPI, Response, HTTPException
from pydantic import BaseModel
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pathlib import Path



app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_DIR / "Frontend" / "static"

print("Serving static files from:", STATIC_DIR)

app.mount(
    "/static", # the url path
    StaticFiles(directory = STATIC_DIR), # Directory on where to find code
    name = "static"
)


@app.get("/", response_class=HTMLResponse)
def api_root():
    with open("Frontend/static/index.html") as f:
        return f.read()


@app.get("/hello")
def hello():
    return {"message": "Hello World"}


@app.get("/api/summary")
def get_count():
    return {
        "total_customers": 1234,
        "churn_rate": 0.27
    }

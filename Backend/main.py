from fastapi import FastAPI, Response, HTTPException
from pydantic import BaseModel
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pathlib import Path
from pydantic import BaseModel

from .queries import list_tables, execute_query



app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_DIR / "frontend" / "static"

# Mount the static files directory
app.mount(
    "/static", # the url path
    StaticFiles(directory = STATIC_DIR), # Directory on where to find code
    name = "static"
)

# Serve the index.html at the root endpoint
@app.get("/", response_class=HTMLResponse)
def api_root():
    with open("frontend/static/index.html") as f:
        return f.read()

## Basic hello world endpoint
@app.get("/hello")
def hello():
    return {"message": "Hello World"}


@app.get("/api/tables")
def get_tables():
    return list_tables()

@app.get("/api/summary")
def get_count():
    return {
        "total_customers": 1234,
        "churn_rate": 0.27
    }


class SQLQuery(BaseModel):
    query: str

@app.post("/api/query")
def run_query(sql_query: SQLQuery):
    query = sql_query.query
    try:
        results = execute_query(query)
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

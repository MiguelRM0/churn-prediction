from fastapi import FastAPI, Response, HTTPException
from pydantic import BaseModel
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pathlib import Path
from backend.schemas.sqlquery import SQLQuery
from .queries import list_tables, execute_query



app = FastAPI()


# Serve the index.html at the root endpoint
@app.get("/")
def api_root():
    return {"message" : "root"}
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


@app.post("/api/query")
def run_query(sql_query: SQLQuery):
    query = sql_query.query
    try:
        results = execute_query(query)
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

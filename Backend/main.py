from fastapi import FastAPI, Response, HTTPException
from pydantic import BaseModel


app = FastAPI()


@app.get("/")
def api_root():
    return {"message" :"ima touch you IAN"}



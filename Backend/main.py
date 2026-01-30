from fastapi import FastAPI, Response, HTTPException
from pydantic import BaseModel
from fastapi import Request


app = FastAPI()

app.mount(
    "/static", # the url path

)



@app.get("/")
def api_root():
    return {"message" :"Hello World"}



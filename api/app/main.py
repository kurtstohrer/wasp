#!/usr/bin/env python3
from fastapi import Depends, FastAPI

from dependencies import get_query_token, get_token_header

from store import settings
from routers import functions, langs

app = FastAPI()


app.include_router(functions.router)
app.include_router(langs.router)

@app.get("/")
async def root():
    return {"message": "wasp"}

from fastapi import FastAPI

from app.resumes.api import route_resumes

app = FastAPI()


@app.get("/")
async def root():
    return {"/": "root page"}


app.include_router(route_resumes, prefix="/api/v1")

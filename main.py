from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from database import create_db_and_tables
from routers import score

app = FastAPI(title="No 13th Floor", version="0.1.0")

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(score.router, prefix="/score", tags=["score"])

@app.get("/health")
def health():
    return {"status": "ok", "service": "no13thfloor"}

@app.get("/")
def root():
    from fastapi.responses import RedirectResponse
    return RedirectResponse(url="/score")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

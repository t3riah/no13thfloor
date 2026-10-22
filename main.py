from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from database import create_db_and_tables
from routers import score


app = FastAPI(title="No 13th Floor", version="0.1.0")
templates = Jinja2Templates(directory="templates")


app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(score.router, prefix="/score", tags=["score"])


@app.get("/health")
def health():
    return {"status": "ok", "service": "no13thfloor"}


@app.get("/methodology")
def methodology_page(request: Request):
    return templates.TemplateResponse("methodology.html", {"request": request})


@app.get("/policy")
def policy_page(request: Request):
    return templates.TemplateResponse("policy.html", {"request": request})


@app.get("/terms")
def terms_page(request: Request):
    return templates.TemplateResponse("terms.html", {"request": request})


@app.get("/")
def root():
    from fastapi.responses import RedirectResponse
    return RedirectResponse(url="/score")


@app.on_event("startup")
def on_startup():
    create_db_and_tables()

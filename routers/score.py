from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session
from typing import List
from database import get_session
from models import Client, MetricSnapshot
from services.score_calculator import calculate_score
from services.email_service import send_score_result

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def score_form(request: Request):
    return templates.TemplateResponse("score_form.html", {"request": request})


@router.post("/", response_class=HTMLResponse)
async def score_submit(
    request: Request,
    name: str = Form(...),
    contact_email: str = Form(...),
    monthly_spend_usd: float = Form(...),
    model_size: str = Form(...),
    task_types: List[str] = Form(...),
    training_runs_per_month: int = Form(...),
    cloud_provider: str = Form(...),
    session: Session = Depends(get_session),
):
    score_data = calculate_score(
        monthly_spend_usd=monthly_spend_usd,
        model_size_key=model_size,
        task_types=task_types,
        training_runs_per_month=training_runs_per_month,
        cloud_provider=cloud_provider,
    )
    client = Client(
        name=name,
        contact_email=contact_email,
        cloud_provider=cloud_provider,
    )
    session.add(client)
    session.commit()
    session.refresh(client)
    snapshot = MetricSnapshot(
        client_id=client.id,
        period_start=score_data["period_start"],
        period_end=score_data["period_end"],
        ai_cost_usd=monthly_spend_usd,
        estimated_kwh=score_data["estimated_monthly_kwh"],
        estimated_co2_kg=score_data["estimated_monthly_co2_kg"],
        gpu_hours=score_data["gpu_hours_monthly"],
        model_family=model_size,
        score=score_data["grade"],
        oversize_ratio=score_data["oversize_ratio"],
        estimated_monthly_waste_usd=score_data["estimated_monthly_waste_usd"],
    )
    session.add(snapshot)
    session.commit()
    try:
        send_score_result(contact_email, name, score_data)
    except Exception:
        pass
    return templates.TemplateResponse("score_result.html", {
        "request": request,
        "score": score_data,
        "name": name,
    })

from datetime import datetime, timedelta

TASK_OPTIMAL_PARAMS = {
    "classification": {"optimal_b": 1, "max_b": 7},
    "summarization": {"optimal_b": 7, "max_b": 13},
    "generation": {"optimal_b": 13, "max_b": 70},
    "embedding": {"optimal_b": 0.1, "max_b": 1},
    "code_completion": {"optimal_b": 7, "max_b": 34},
}

MODEL_SIZE_MAP = {
    "lt1": 0.5,
    "1to7": 4.0,
    "7to70": 35.0,
    "gt70": 100.0,
}

US_GRID_INTENSITY_KG_KWH = 0.429
KWH_PER_GPU_HOUR = 0.4


def calculate_score(
    monthly_spend_usd: float,
    model_size_key: str,
    task_types: list,
    training_runs_per_month: int,
    cloud_provider: str,
) -> dict:
    model_size_b = MODEL_SIZE_MAP.get(model_size_key, 35.0)
    optimal_sizes = [
        TASK_OPTIMAL_PARAMS.get(t, {}).get("optimal_b", 7)
        for t in task_types
    ]
    avg_optimal = sum(optimal_sizes) / len(optimal_sizes) if optimal_sizes else 7.0
    oversize_ratio = model_size_b / avg_optimal if avg_optimal > 0 else 1.0
    baseline_monthly = avg_optimal * 0.0004 * training_runs_per_month
    estimated_waste = max(0.0, monthly_spend_usd - baseline_monthly)
    gpu_hours = model_size_b * training_runs_per_month * 0.1
    estimated_kwh = gpu_hours * KWH_PER_GPU_HOUR
    estimated_co2_kg = estimated_kwh * US_GRID_INTENSITY_KG_KWH
    if oversize_ratio <= 1.5:
        grade = "A"
    elif oversize_ratio <= 3:
        grade = "B"
    elif oversize_ratio <= 6:
        grade = "C"
    elif oversize_ratio <= 12:
        grade = "D"
    elif oversize_ratio <= 20:
        grade = "E"
    else:
        grade = "F"
    grade_colors = {
        "A": "#00F5D4", "B": "#56CFB2",
        "C": "#F7B731", "D": "#F0932B",
        "E": "#E63946", "F": "#C0392B"
    }
    now = datetime.utcnow()
    return {
        "grade": grade,
        "grade_color": grade_colors[grade],
        "oversize_ratio": round(oversize_ratio, 2),
        "optimal_model_size_b": round(avg_optimal, 2),
        "actual_model_size_b": model_size_b,
        "estimated_monthly_waste_usd": round(estimated_waste, 2),
        "estimated_annual_waste_usd": round(estimated_waste * 12, 2),
        "estimated_monthly_kwh": round(estimated_kwh, 2),
        "estimated_monthly_co2_kg": round(estimated_co2_kg, 2),
        "gpu_hours_monthly": round(gpu_hours, 2),
        "period_start": now - timedelta(days=30),
        "period_end": now,
        "methodology_note": (
            "Estimates based on public efficiency baselines and CodeCarbon "
            "open methodology. US average grid intensity (0.429 kg CO2/kWh) "
            "applied. Not formal carbon accounting."
        ),
    }

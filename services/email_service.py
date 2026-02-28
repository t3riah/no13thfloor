import resend
from config import settings
from jinja2 import Environment, FileSystemLoader

resend.api_key = settings.RESEND_API_KEY
jinja_env = Environment(loader=FileSystemLoader("templates/emails"))


def send_score_result(to_email: str, client_name: str, score_data: dict):
    template = jinja_env.get_template("score_delivery.html")
    html = template.render(name=client_name, score=score_data)
    resend.Emails.send({
        "from": settings.FROM_EMAIL,
        "to": to_email,
        "subject": f"Your No 13th Floor Score: {score_data['grade']}",
        "html": html,
    })


def send_waste_report(to_email: str, client_name: str, pdf_path: str):
    template = jinja_env.get_template("report_delivery.html")
    html = template.render(name=client_name)
    with open(pdf_path, "rb") as f:
        pdf_bytes = list(f.read())
    resend.Emails.send({
        "from": settings.FROM_EMAIL,
        "to": to_email,
        "subject": "Your No 13th Floor Waste Report",
        "html": html,
        "attachments": [{
            "filename": "No13thFloor_WasteReport.pdf",
            "content": pdf_bytes,
        }],
    })

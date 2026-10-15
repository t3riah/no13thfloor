# No 13th Floor

[![Free](https://img.shields.io/badge/Free-No%20Signup-blue)](https://no13thfloor.org)
[![Open Source](https://img.shields.io/badge/Open%20Source-MIT-yellow)](LICENSE)
[![Scoring](https://img.shields.io/badge/Scoring-Deterministic%20Rules-green)](services/score_calculator.py)

**AI model waste auditor. Free. No signup required.**

> Are you running a 70B model for a job a 7B model handles fine? You're not alone. This tool finds out.

**[Try the free audit → no13thfloor.org](https://no13thfloor.org)**

⭐ **Star this repo if No 13th Floor saved your team money** — it helps other engineers find it.

---

## What is this?

No 13th Floor is an AI efficiency scoring tool that estimates how much compute — and money — your current AI stack is wasting due to model oversizing.

You describe your use case and current model. It returns:

- A **Floor Score** (letter grade A–F)
- Estimated **monthly waste in USD**
- Estimated **annual projected waste**
- **Oversize ratio** (how many times larger your model is than optimal)
- A recommended right-sized architecture
- A curated list of cost-reduction platforms matched to your workload

No account. No credit card. No waiting. Your score renders instantly and anonymously — an email address is only asked for if you want the PDF report delivered to your inbox.

---

## How the scoring works

No LLM. No black box. The Floor Score is computed by a **deterministic, rule-based engine** (`services/score_calculator.py`) from your declared spend, model size, task types, training frequency, and cloud provider.

That is a deliberate choice:

- **Explainable** — every number on your report traces back to a visible rule, not a model's mood.
- **Instant** — no inference latency, no queue.
- **Zero marginal cost** — scoring a thousand audits costs the same as scoring one, which is why the tool can stay free forever.

---

## Why it exists

Most engineering teams default to the biggest model available "just to be safe." That instinct is understandable. It's also expensive.

A classification task that needs 3B parameters is getting 70B. A summarization job that runs fine on Mistral 7B is running on GPT-4-class APIs at 30x the cost. The waste isn't visible — it shows up as a line item in a cloud bill that everyone shrugs at.

No 13th Floor makes the waste visible. And names a number.

---

## Stack

- **Backend**: Python / FastAPI
- **Database**: SQLite via SQLModel
- **Frontend**: Jinja2 templates + static CSS (no framework)
- **Scoring**: deterministic rule-based engine (no LLM inference)
- **Reports**: WeasyPrint PDFs, delivered via Resend
- **Hosting**: Oracle Cloud (free tier)
- **Auth**: None — intentionally

---

## Self-hosting

```bash
git clone https://github.com/t3riah/no13thfloor.git
cd no13thfloor
cp .env.example .env
# Fill in SECRET_KEY; add RESEND_API_KEY only if you want email PDF reports
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

Open `http://localhost:8000/score/` and run your first audit. Email delivery is optional — the tool scores fully anonymously without it.

---

## The problem in the wild

This is not a hypothetical. These conversations happen every day:

- "We were initially using GPT-4 for everything (yeah, I know)" — r/OpenAI
- "AI support costs way higher than expected... wrong model for the task" — r/SaaS
- "It felt like overkill to use a 175B+ model just for simple logic" — r/AI_Agents
- "Why using GPT-4 for sentiment analysis ffs?" — r/OpenAI

The pattern is universal: teams reach for the biggest model first, realize the cost later, and then manually trial-and-error their way to something cheaper. No 13th Floor shortcircuits that process.

---

## Cost-reduction stack

Based on your score, the tool recommends right-sized inference platforms:

| Platform | Best for | Savings potential |
|---|---|---|
| Groq | Speed-critical tasks, real-time | Up to 90% vs GPT-4 |
| Together AI | Open-source model hosting | Up to 95% vs GPT-4 |
| Replicate | Bursty / pay-per-prediction | Eliminates idle cost |
| Vantage | AI API cost tracking | Free up to $2,500/mo |

---

## Built by

[First Principle Dynamics LLC](https://firstprincipledynamics.com/) — Miami, FL

Minority-owned. Building tools grounded in first principles thinking.

---

## Support

If this tool saved your team money, consider [buying us a coffee](https://ko-fi.com/no13thfloor). It keeps the free tier free.

---

*No 13th Floor: the floor that exists, you just weren't looking for it.*

# No 13th Floor

**AI model waste auditor. Free. No signup required.**

> Are you running a 70B model for a job a 7B model handles fine? You're not alone. This tool finds out.

**[Try the free audit → no13thfloor.org](https://no13thfloor.org)**

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

No account. No credit card. No waiting.

---

## Why it exists

Most engineering teams default to the biggest model available "just to be safe." That instinct is understandable. It's also expensive.

A classification task that needs 3B parameters is getting 70B. A summarization job that runs fine on Mistral 7B is running on GPT-4-class APIs at 30x the cost. The waste isn't visible — it shows up as a line item in a cloud bill that everyone shrugs at.

No 13th Floor makes the waste visible. And names a number.

---

## Stack

- **Backend**: Python / Flask
- **Frontend**: HTML/CSS (no framework)
- **Inference**: Groq API (Llama 3 70B)
- **Hosting**: Oracle Cloud (free tier)
- **Auth**: None — intentionally

---

## Self-hosting

```bash
git clone https://github.com/t3riah/no13thfloor.git
cd no13thfloor
cp .env.example .env
# Add your GROQ_API_KEY to .env
pip install -r requirements.txt
python app.py
```

Requires a free [Groq API key](https://groq.com/?utm_source=no13thfloor&utm_medium=readme&utm_campaign=github).

---

## The problem in the wild

This is not a hypothetical. These conversations happen every day:

- *"We were initially using GPT-4 for everything (yeah, I know)"* — r/OpenAI
- *"AI support costs way higher than expected... wrong model for the task"* — r/SaaS
- *"It felt like overkill to use a 175B+ model just for simple logic"* — r/AI_Agents
- *"Why using GPT-4 for sentiment analysis ffs?"* — r/OpenAI

The pattern is universal: teams reach for the biggest model first, realize the cost later, and then manually trial-and-error their way to something cheaper. No 13th Floor shortcircuits that process.

---

## Cost-reduction stack

Based on your score, the tool recommends right-sized inference platforms:

| Platform | Best for | Savings potential |
|---|---|---|
| [Groq](https://groq.com/?utm_source=no13thfloor&utm_medium=readme&utm_campaign=github) | Speed-critical tasks, real-time | Up to 90% vs GPT-4 |
| [Together AI](https://www.together.ai/?utm_source=no13thfloor&utm_medium=readme&utm_campaign=github) | Open-source model hosting | Up to 95% vs GPT-4 |
| [Replicate](https://replicate.com/?utm_source=no13thfloor&utm_medium=readme&utm_campaign=github) | Bursty / pay-per-prediction | Eliminates idle cost |
| [Vantage](https://www.vantage.sh/?utm_source=no13thfloor&utm_medium=readme&utm_campaign=github) | AI API cost tracking | Free up to $2,500/mo |

---

## Built by

[First Principle Dynamics LLC](https://firstprincipledynamics.com) — Miami, FL

Minority-owned. Building tools grounded in first principles thinking.

---

## Support

If this tool saved your team money, consider [buying us a coffee](https://ko-fi.com/no13thfloor). It keeps the free tier free.

---

*No 13th Floor: the floor that exists, you just weren't looking for it.*

# CompassAgent — MVP Version (Gemini AI Agent · Interactive Dashboard)

**Intern:** Aaron Wu
**Level:** 2nd-year undergrad (Northeastern, Data Science + Psychology), Intermediate Python
**Timeline:** 2–3 weeks (~45 hours)
**Paradigm:** **Interactive Dashboard** — Streamlit with CV upload, location/interest filters, and AI-generated personalized briefings on click.
**Database count:** **4** (the career-and-labor domain is self-contained; pharma databases don't naturally fit this project).

---

## The Agent

**What the agent does (autonomous workflow on click):** User uploads a CV and picks filters. Pressing "Generate briefing" triggers an autonomous Gemini workflow that calls 4 public databases, ranks matches, and writes a personalized Markdown briefing.

**Input:** CV file (PDF/DOCX) + filters (location, interest, role type).
**Output:** Personalized briefing — top jobs, salary benchmarks, PI lab matches. Saved to `briefings/{user_id}_{date}.md`, downloadable as PDF.

**Tools (4 public databases):**

1. `search_jobs_usajobs(skills, location, n=10)` — **USAJOBS API**
2. `lookup_onet_skill(skill_name)` — **O\*NET Web Services**
3. `get_oews_salary(occupation_code, state)` — **BLS OEWS**
4. `find_pi_labs_nih(topic, n=5)` — **NIH RePORTER**

**Example runs (≥3):**

- *Input:* CV (data science undergrad), filter "Boston, internship". *Output:* briefing with 5 internships, entry-level Boston bioinformatics salary, 3 matching Harvard/MIT PI labs.
- *Input:* CV (postdoc), filter "California, research scientist". *Output:* research-track roles + CA salary benchmark + 5 NIH-funded PIs.
- *Input:* CV (career switcher from finance), filter "remote, entry-level". *Output:* transferable-skill roles + skill-gap analysis + remote salary expectations.

---

## Week-by-Week

**Week 1 (~15h):** Build 4 tool functions; CV parser with spaCy.
**Week 2 (~20h):** Streamlit dashboard + Gemini agent wired up.
**Week 3 (~10h):** Test 3 real CVs + Markdown-to-PDF + 2-min demo.

## What's OUT

LinkedIn Jobs, SEC EDGAR, openFDA portfolio scoring, mock interviews, recruiter view, public dashboard.

## Stretch Goals

- 5th tool: `pull_sponsor_pipeline(sponsor)` via openFDA for sponsor R&D activity.
- Add weekly auto-refresh via GitHub Actions.

## Realistic CV Entry

*Built CompassAgent, a working interactive Streamlit dashboard with an autonomous Gemini AI agent that generates personalized biopharma job briefings.*

- Wrapped 4 public-database tools (USAJOBS, O\*NET, BLS OEWS, NIH RePORTER) into a Gemini agent using `google-generativeai` automatic function calling.
- Delivered personalized Markdown briefings tested across 3 distinct user profiles.

## Tech Stack

Python, `google-generativeai`, Streamlit, spaCy, requests, pandas, markdown-pdf, USAJOBS API, O\*NET Web Services, BLS API, NIH RePORTER API.

---

## Shared Agent Skeleton (three paradigms, one Gemini primitive)

Every intern's agent uses Gemini's automatic function calling, but the interface layer differs by paradigm. The cohort uses **one starter repo with three sub-templates** that interns clone in week 1:

- **Dossier-generator template** — CLI script: takes structured args, runs the agent workflow autonomously, writes `*.md` + `*.json` to disk. Used by Beyza, Chin Hung, Christina, Shucheng, Xiaoxue.
- **Dashboard template** — Streamlit page with selectors and tables; the agent is invoked on button-click for specific synthesis tasks. Used by Aaron, Jason, Shawn.
- **Computation-engine template** — Streamlit form (or CLI) that takes structured analytical inputs, runs the agent workflow, produces a downloadable analytical report with plots. Used by Reuben, Kening, Natalie.

**Why no chat interfaces?** Scientists need reproducible, shareable artifacts. The agent dimension (Gemini-as-orchestrator, autonomous tool-calling across multiple public databases, synthesis across sources) is preserved in all three paradigms; only the deliverable shape changes.

**Christina** (OpenRepurpose evidence-and-validation module) owns the starter repo with all three sub-templates. The shared repo should also include pre-built wrappers for the most heavily-used databases (ChEMBL, openFDA FAERS, Open Targets, ClinVar) so multiple interns don't redo the same boilerplate.

### Reference snippet — Gemini function calling (same across all three paradigms)

```python
import google.generativeai as genai
import os
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def my_tool(arg: str) -> dict:
    """One-line docstring Gemini uses to decide when to call this tool."""
    return {"result": ...}

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    tools=[my_tool, other_tool, ...],   # 4-8 tools per agent
    system_instruction=open("system_prompt.md").read(),
)
chat = model.start_chat(enable_automatic_function_calling=True)
response = chat.send_message("structured request — one shot, not a conversation")
```

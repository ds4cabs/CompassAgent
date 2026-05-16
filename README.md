# CompassAgent

**Intern:** Aaron Wu
**Project Type:** Interactive Dashboard

## Overview
CompassAgent is an AI-powered career briefing assistant for life-sciences job seekers. The project uses a Streamlit interface to upload a CV, choose filters, and generate a personalized briefing that synthesizes job matches, salary benchmarks, and research lab recommendations.

## Deliverable
- Streamlit dashboard with CV upload, location/interest filters, and "Generate briefing" button
- Autonomous Gemini workflow that calls public data tools and writes a Markdown briefing
- Downloadable briefing output in Markdown/PDF

## Core Tools
- `search_jobs_usajobs` (USAJOBS)
- `lookup_onet_skill` (O*NET)
- `get_oews_salary` (BLS OEWS)
- `find_pi_labs_nih` (NIH RePORTER)

## Tech Stack
Python, Streamlit, spaCy, pandas, requests, `google-generativeai`, markdown export

## Notes
This project is designed as a single intern dashboard with reproducible artifact generation, not a chat interface.

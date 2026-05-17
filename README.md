# CompassAgent

[![CABS: ds4cabs](https://img.shields.io/badge/CABS-ds4cabs-1f4b99?logo=github)](https://github.com/ds4cabs)
[![GitHub Pages: live](https://img.shields.io/badge/GitHub_Pages-live-brightgreen?logo=github)](https://ds4cabs.github.io/CompassAgent/)
![CABS: 2026](https://img.shields.io/badge/CABS-2026-6f42c1)
![status: MVP in progress](https://img.shields.io/badge/status-MVP_in_progress-f1c40f)
![type: Interactive Dashboard](https://img.shields.io/badge/type-Interactive_Dashboard-1f6feb)
![domain: Career Intelligence](https://img.shields.io/badge/domain-Career_Intelligence-0aa)

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

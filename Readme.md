# Biotech Lead Scoring Application

## Overview

This application helps biotech business development teams prioritize potential partnerships and collaborations by automatically scoring and ranking leads based on strategic fit indicators. The tool assigns scores to prospects based on role relevance, funding status, technology adoption, and research engagement signals.

## What It Does

- **Loads and scores** a dataset of biotech industry contacts
- **Ranks leads** from highest to lowest priority
- **Provides filtering** by search terms and score ranges
- **Exports results** as CSV for CRM integration or outreach planning
- **Visualizes metrics** including total leads, filtered counts, and average scores

## Scoring Logic & Rationale

The scoring algorithm assigns points based on attributes that indicate strong partnership potential:

| Criterion | Points | Rationale |
|-----------|--------|-----------|
| **Title Relevance** | +30 | Keywords like "toxicology," "safety," "preclinical," "hepatic," or "3D" indicate direct alignment with in vitro testing solutions |
| **Funding Stage (Series A/B)** | +20 | Companies at these stages have validated models and capital to invest in new technologies |
| **Uses In Vitro Models** | +15 | Current adoption shows openness to alternative methods and existing infrastructure |
| **Open to NAMs** | +10 | New Approach Methodologies alignment indicates progressive regulatory thinking |
| **Hub Location** | +10 | Proximity to biotech hubs (SF, Boston, San Diego, etc.) enables easier in-person collaboration |
| **Recent Publication** | +40 | Publishing activity signals active research programs and thought leadership |

**Maximum Score**: 100 (capped)

## Assumptions & Design Decisions

### Data Generation
- All leads are **entirely fictional** and generated using Python with a fixed random seed for reproducibility
- Names, companies, emails, and LinkedIn URLs are mock data created for demonstration purposes
- Geographic distribution emphasizes major biotech hubs (Bay Area, Boston, San Diego, Research Triangle)
- Funding stages and boolean attributes reflect realistic distributions in the biotech industry

### Scoring Weights
- **Publications weighted highest (40 pts)**: Active researchers are the most valuable contacts for scientific partnerships
- **Title relevance (30 pts)**: Direct role alignment is the strongest predictor of relevance
- **Funding (20 pts)**: Series A/B companies have the resources and growth trajectory for partnerships
- **Technology adoption (15 pts)**: Current users of in vitro models are easier to engage
- **Geographic/methodology signals (10 pts each)**: Useful but not determinative factors

### Simplifications
- No external APIs or web scraping
- No authentication or user management
- No database (data stored in CSV)
- Boolean fields use simple Yes/No values for clarity
- Scoring is deterministic (same input always produces same output)

## Installation & Setup

### Prerequisites
- Python 3.10 or higher
- pip package manager

### Steps

1. **Clone or download** this repository

2. **Navigate to the project directory**:
```bash
   cd lead_scoring_demo
```

3. **Install dependencies**:
```bash
   pip install -r requirements.txt
```

## Running the Application

From the project root directory, run:
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

## Using the Application

1. **Browse the ranked leads** in the main table
2. **Filter by search terms** (title, company, location) using the sidebar
3. **Adjust score range** with the slider to focus on high-priority leads
4. **Export filtered results** using the download button
5. **Review scoring methodology** in the expandable info section

## Project Structure

    lead_scoring_demo/
    ├── app.py
    ├── scoring.py
    ├── data/
    │   └── leads.csv
    ├── requirements.txt       
    └── README.md


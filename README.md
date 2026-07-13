# Campaign Decision Assistant

A decision-support system that helps marketing teams investigate campaign performance issues, detect data inconsistencies, identify compliance risks, compare historical campaign outcomes, and generate actionable recommendations through an interactive dashboard.

---

## Problem Statement

Marketing teams often work with data coming from multiple systems such as:

- Campaign platforms
- Analytics dashboards
- Ecommerce systems
- Attribution reports

When performance drops, analysts must manually inspect:

- Conversion metrics
- Attribution discrepancies
- Funnel data
- Campaign messaging
- Historical campaign performance

This process is time-consuming and prone to oversight.

The Campaign Decision Assistant automates this analysis and presents key findings in a single interface.

---

## Solution Overview

The application combines:

- Campaign Retrieval
- Performance Analysis
- Conflict Detection
- Compliance Risk Identification
- Historical Similarity Search
- Recommendation Generation

to help users quickly understand why a campaign is underperforming and what actions should be taken next.

---

## Key Features

### Campaign Analysis

Retrieves campaign information including:

- Campaign objective
- Creative variants
- Landing page details
- Campaign status
- Marketing brief

---

### Performance Metrics Review

Analyzes:

- Impressions
- Clicks
- CTR
- Conversions
- Conversion Rate
- Spend

Provides visual trend analysis through interactive charts.

---

### Ecommerce Funnel Inspection

Evaluates:

- Sessions
- Add-to-Cart events
- Checkout Starts
- Purchases

Identifies funnel drop-offs and missing data.

---

### Claim Risk Detection

Automatically flags potentially risky marketing claims.

Example:

> "Feel a Decade Younger in Weeks"

This type of statement may create compliance or advertising-policy concerns and is highlighted for review.

---

### Data Conflict Detection

Identifies inconsistencies across systems.

Example:

- Performance Metrics:
  - 173 conversions

- Ecommerce Orders:
  - 322 attributed orders

The application highlights these discrepancies to prevent incorrect business decisions.

---

### Similar Campaign Discovery

Compares current campaigns against previously approved campaigns.

Provides:

- Historical outcomes
- Performance benchmarks
- Key learnings
- Successful messaging patterns

---

### Recommendation Engine

Generates actionable recommendations such as:

- Investigate attribution mismatches
- Improve landing-page alignment
- Review compliance risks
- Restore high-performing messaging

---

### Interactive Dashboard

Built using Streamlit for rapid exploration.

Users can:

- Enter Campaign IDs
- Run analysis
- View charts
- Review risks
- Explore recommendations

---

## System Architecture

```text
                    ┌─────────────────┐
                    │  Streamlit UI   │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   FastAPI API   │
                    └────────┬────────┘
                             │
        ┌────────────────────┼────────────────────┐
        ▼                    ▼                    ▼

┌───────────────┐  ┌────────────────┐  ┌────────────────┐
│ Retrieval     │  │ Conflict       │  │ Claim Checker  │
│ Service       │  │ Detector       │  │                │
└───────────────┘  └────────────────┘  └────────────────┘

        ▼                    ▼                    ▼

┌───────────────────────────────────────────────┐
│ Similarity + Recommendation + AI Reasoner     │
└───────────────────────────────────────────────┘

                             ▼

                   Structured Analysis Output
```

---

## Project Structure

```text
CampaignDecisionAssistant
│
├── app
│   ├── api
│   │   └── analysis.py
│   │
│   ├── schemas
│   │   ├── request.py
│   │   └── analysis_response.py
│   │
│   ├── services
│   │   ├── retrieval.py
│   │   ├── conflict_detector.py
│   │   ├── claim_checker.py
│   │   ├── similarity.py
│   │   ├── recommendation.py
│   │   └── ai_reasoner.py
│   │
│   ├── server.py
│   └── __init__.py
│
├── data
│   ├── campaigns.json
│   ├── ecommerce_orders.json
│   ├── performance_metrics.csv
│   └── approved_campaigns.json
│
├── tests
│
├── app_ui.py
├── requirements.txt
└── README.md
```

---

## Technology Stack

### Backend

- FastAPI
- Python
- Pydantic

### Data Processing

- Pandas
- JSON
- CSV

### Frontend

- Streamlit

### Testing

- Pytest

---

## Installation

Clone repository:

```bash
git clone <repository-url>

cd CampaignDecisionAssistant
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Backend

```bash
uvicorn app.server:app --reload
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Run Frontend

```bash
streamlit run app_ui.py
```

Dashboard:

```text
http://localhost:8501
```

---

## API Example

### Request

```json
{
  "campaign_id": "CMP-101",
  "question": "Why are conversions low?"
}
```

### Response

```json
{
  "claim_risks": [],
  "conflicts": [],
  "recommendation": {},
  "ai_analysis": {}
}
```

---

## Sample Analysis Findings

The system can identify:

### Messaging Mismatch

A high-click advertisement may drive traffic but fail to convert if the landing page does not reinforce the same promise.

---

### Attribution Issues

Differences between conversion reports and ecommerce order counts can indicate tracking problems.

---

### Compliance Concerns

Aggressive health or anti-aging claims can create advertising-policy risks.

---

### Historical Performance Patterns

Campaigns using exaggerated promises may increase CTR but reduce overall conversion performance.

---

## Testing

Run unit tests:

```bash
pytest
```

---

## Future Enhancements

- Database Integration
- Real-Time Campaign Monitoring
- LLM-Powered Recommendation Engine
- Multi-Channel Campaign Support
- Automated Alert System
- Exportable PDF Reports
- User Authentication
- Cloud Deployment

---

## Author

Vijayalakshmi G

Campaign Decision Assistant was developed as a marketing analytics and decision-support system to demonstrate backend API development, data analysis, conflict detection, recommendation systems, and dashboard visualization using FastAPI and Streamlit.
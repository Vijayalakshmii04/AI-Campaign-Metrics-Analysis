from typing import Any

from pydantic import BaseModel


class AnalysisResponse(BaseModel):
    campaign: dict[str, Any]

    metrics: list[dict[str, Any]]

    orders: list[dict[str, Any]]

    claim_risks: list[dict[str, Any]]

    conflicts: list[dict[str, Any]]

    similar_campaigns: list[dict[str, Any]]

    recommendation: dict[str, Any]

    ai_analysis: dict[str, Any]
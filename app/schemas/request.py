from pydantic import BaseModel


class AnalysisRequest(BaseModel):
    campaign_id: str
    question: str
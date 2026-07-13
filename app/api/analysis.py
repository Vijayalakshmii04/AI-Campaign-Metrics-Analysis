from fastapi import APIRouter

from app.schemas.request import AnalysisRequest
from app.schemas.analysis_response import AnalysisResponse

from app.services.retrieval import RetrievalService
from app.services.claim_checker import ClaimChecker
from app.services.conflict_detector import ConflictDetector
from app.services.similarity import SimilarityService
from app.services.recommendation import RecommendationService
from app.services.ai_reasoner import AIReasoner


router = APIRouter()

retrieval = RetrievalService()
claim_checker = ClaimChecker()
conflict_detector = ConflictDetector()
similarity_service = SimilarityService()
recommendation_service = RecommendationService()
ai_reasoner = AIReasoner()


@router.post(
    "/analyze",
    response_model=AnalysisResponse
)
def analyze(request: AnalysisRequest):

    campaign = retrieval.get_campaign(
        request.campaign_id
    )

    if campaign is None:
        return {
            "error": "Campaign not found"
        }

    metrics = retrieval.get_metrics(
        request.campaign_id
    )

    orders = retrieval.get_ecommerce_orders(
        request.campaign_id
    )

    claim_risks = claim_checker.check(
        campaign
    )

    conflicts = conflict_detector.detect(
        metrics,
        orders
    )

    similar_campaigns = (
        similarity_service.find_similar_campaigns(
            campaign
        )
    )

    recommendation = (
        recommendation_service.generate(
            campaign,
            metrics,
            conflicts,
            similar_campaigns
        )
    )

    ai_analysis = ai_reasoner.analyze(
        campaign,
        metrics,
        orders,
        conflicts
    )

    return {
        "campaign": campaign,
        "metrics": metrics,
        "orders": orders,
        "claim_risks": claim_risks,
        "conflicts": conflicts,
        "similar_campaigns": similar_campaigns,
        "recommendation": recommendation,
        "ai_analysis": ai_analysis
    }
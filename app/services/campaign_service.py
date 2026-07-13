class CampaignService:

    def get_campaign(self, campaign_id: str):

        return {
            "campaign_id": campaign_id,
            "name": "Summer Promotion",
            "status": "ACTIVE"
        }
import json
from pathlib import Path

DATA_DIR = Path("data")


class SimilarityService:

    def find_similar_campaigns(
        self,
        campaign
    ):

        with open(
            DATA_DIR / "approved_campaigns.json",
            "r",
            encoding="utf-8"
        ) as f:

            approved = json.load(f)

        return approved
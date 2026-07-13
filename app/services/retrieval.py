import json
import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")


class RetrievalService:

    def get_campaign(self, campaign_id):

        with open(
            DATA_DIR / "campaigns.json",
            "r",
            encoding="utf-8"
        ) as f:

            campaigns = json.load(f)

        for campaign in campaigns:

            if campaign["campaign_id"] == campaign_id:
                return campaign

        return None

    def get_metrics(self, campaign_id):

        df = pd.read_csv(
            DATA_DIR / "performance_metrics.csv"
        )

        rows = df[
            df["campaign_id"] == campaign_id
        ]

        return rows.to_dict(
            orient="records"
        )
    def get_ecommerce_orders(
        self,
        campaign_id
    ):

        with open(
            DATA_DIR / "ecommerce_orders.json",
            "r",
            encoding="utf-8"
        ) as f:

            orders = json.load(f)

        return [
            order
            for order in orders
            if order["campaign_id"]
            == campaign_id
        ]
class OrderService:

    def get_orders(self, campaign_id: str):

        return [
            {
                "order_id": "ORD-001",
                "amount": 100
            }
        ]
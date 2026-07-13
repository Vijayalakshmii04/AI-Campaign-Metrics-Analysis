class ConflictDetector:

    def detect(
        self,
        metrics,
        ecommerce_orders
    ):

        conflicts = []

        ecommerce_map = {
            row["period"]: row
            for row in ecommerce_orders
        }

        for metric in metrics:

            period = metric["period"]

            ecommerce = ecommerce_map.get(
                period
            )

            if not ecommerce:
                continue

            conversions = metric[
                "conversions"
            ]

            orders = ecommerce[
                "attributed_orders"
            ]

            if conversions != orders:

                conflicts.append(
                    {
                        "type":
                        "data_conflict",

                        "period":
                        period,

                        "sources": [
                            "performance_metrics",
                            "ecommerce_orders"
                        ],

                        "description":
                        f"Conversions "
                        f"({conversions}) "
                        f"do not match "
                        f"attributed orders "
                        f"({orders})"
                    }
                )

            if ecommerce["funnel"] is None:

                conflicts.append(
                    {
                        "type":
                        "missing_data",

                        "period":
                        period,

                        "sources": [
                            "ecommerce_orders"
                        ],

                        "description":
                        "Funnel data missing"
                    }
                )

        return conflicts
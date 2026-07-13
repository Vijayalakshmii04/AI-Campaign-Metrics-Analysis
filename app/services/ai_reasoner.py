class AIReasoner:

    def analyze(
        self,
        campaign,
        metrics,
        orders,
        conflicts
    ):

        root_causes = []
        recommendations = []
        risks = []

        if len(metrics) >= 2:

            first = metrics[0]
            last = metrics[-1]

            ctr_up = (
                last["ctr_pct"]
                > first["ctr_pct"]
            )

            conversion_down = (
                last["conversion_rate_pct"]
                < first["conversion_rate_pct"]
            )

            if ctr_up and conversion_down:

                root_causes.append(
                    "Creative generated more clicks but fewer conversions."
                )

                root_causes.append(
                    "Possible message-to-landing-page mismatch."
                )

                recommendations.append(
                    "Align landing page messaging with ad promise."
                )

        for conflict in conflicts:

            if conflict["type"] == "data_conflict":

                risks.append(
                    conflict["description"]
                )

            if conflict["type"] == "missing_data":

                risks.append(
                    conflict["description"]
                )

        creatives = campaign.get(
            "creative_variants",
            []
        )

        for creative in creatives:

            text = (
                creative.get(
                    "headline",
                    ""
                )
                + " "
                + creative.get(
                    "primary_text",
                    ""
                )
            ).lower()

            if "younger" in text:

                risks.append(
                    "Potential regulatory claim risk detected."
                )

        if not recommendations:

            recommendations.append(
                "Continue monitoring campaign performance."
            )

        return {
            "root_causes": root_causes,
            "recommendations": recommendations,
            "risks": risks
        }
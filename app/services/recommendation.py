class RecommendationService:

    def generate(
        self,
        campaign,
        metrics,
        conflicts,
        similar_campaigns
    ):

        recommendations = []

        if conflicts:
            recommendations.append(
                "Investigate attribution mismatch between metrics and ecommerce orders."
            )

        if len(metrics) >= 2:

            first = metrics[0]
            second = metrics[1]

            if (
                second["ctr_pct"] >
                first["ctr_pct"]
                and
                second["conversion_rate_pct"] <
                first["conversion_rate_pct"]
            ):

                recommendations.append(
                    "Creative attracts clicks but message may not align with landing page."
                )

        return {
            "priority": "high",
            "action": "Align landing page headline with ad promise",
            "expected_impact": "Increase conversion rate",
            "root_cause":
                "Possible message-to-landing-page mismatch",

            "recommended_actions":
                recommendations
        }
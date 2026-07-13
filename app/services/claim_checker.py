class ClaimChecker:

    def check(self, campaign):

        risks = []

        creatives = campaign.get(
            "creative_variants",
            []
        )

        for creative in creatives:

            text = (
                creative.get("headline", "")
                + " "
                + creative.get(
                    "primary_text",
                    ""
                )
            ).lower()

            if "younger" in text:

                risks.append(
                    {
                        "severity": "high",
                        "reason":
                        "Potential aging reversal claim"
                    }
                )

        return risks
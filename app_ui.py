import requests
import pandas as pd
import streamlit as st
import json

st.set_page_config(
    page_title="Campaign Decision Assistant",
    layout="wide"
)

st.title("Campaign Decision Assistant")

campaign_id = st.text_input(
    "Campaign ID",
    value="CMP-101"
)

question = st.text_input(
    "Question",
    value="Why are conversions low?"
)

if st.button("Analyze"):

    try:

        response = requests.post(
            "http://127.0.0.1:8000/api/v1/analyze",
            json={
                "campaign_id": campaign_id,
                "question": question
            }
        )

        if response.status_code != 200:
            st.error(
                f"API Error: {response.status_code}"
            )
            st.stop()

        result = response.json()

        st.header("Campaign")

        campaign = result["campaign"]

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Campaign",
                campaign["name"]
            )

        with col2:
            st.metric(
                "Objective",
                campaign["objective"]
            )

        with col3:
            st.metric(
                "Channel",
                campaign["channel"]
            )

        st.header("Performance Metrics")

        metrics_df = pd.DataFrame(
            result["metrics"]
        )

        st.dataframe(
            metrics_df,
            use_container_width=True
        )

        if len(metrics_df) > 0:

            latest = metrics_df.iloc[-1]

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric(
                    "CTR %",
                    latest.get("ctr_pct", 0)
                )

            with col2:
                st.metric(
                    "Conversion %",
                    latest.get(
                        "conversion_rate_pct",
                        0
                    )
                )

            with col3:
                st.metric(
                    "Clicks",
                    latest.get("clicks", 0)
                )

            with col4:
                st.metric(
                    "Conversions",
                    latest.get(
                        "conversions",
                        0
                    )
                )

        if (
            "period" in metrics_df.columns
            and
            "conversion_rate_pct"
            in metrics_df.columns
        ):

            st.subheader(
                "Conversion Rate Trend"
            )

            chart_df = metrics_df[
                [
                    "period",
                    "conversion_rate_pct"
                ]
            ]

            chart_df = chart_df.set_index(
                "period"
            )

            st.line_chart(chart_df)

        st.header("Claim Risks")

        st.json(
            result["claim_risks"]
        )

        st.header("Data Conflicts")

        st.json(
            result["conflicts"]
        )

        st.header("Recommendation")

        st.json(
            result["recommendation"]
        )

        st.header("AI Analysis")

        st.json(
            result["ai_analysis"]
        )

        st.header("Similar Campaigns")

        similar_df = pd.DataFrame(
            result["similar_campaigns"]
        )

        st.dataframe(
            similar_df,
            use_container_width=True
        )
        st.download_button(
            label="Download Analysis",
            data=json.dumps(
                result,
                indent=2
            ),
            file_name="campaign_analysis.json",
            mime="application/json"
        )
        st.metric(
            "Spend",
            latest.get(
                "spend_inr",
                0
            )
        )
        st.metric(
            "Impressions",
            latest.get(
                "impressions",
                0
            )
        )
        st.subheader("CTR Trend")

        ctr_df = metrics_df[
            [
                "period",
                "ctr_pct"
            ]
        ]

        ctr_df = ctr_df.set_index(
            "period"
        )

        st.line_chart(ctr_df)
        st.subheader("Conversions")

        conv_df = metrics_df[
            [
                "period",
                "conversions"
            ]
        ]

        conv_df = conv_df.set_index(
            "period"
        )

        st.bar_chart(conv_df)


    except requests.exceptions.ConnectionError:

        st.error(
            "Cannot connect to FastAPI server.\n\n"
            "Start it with:\n\n"
            "uvicorn app.server:app --reload"
        )

    except Exception as e:

        st.error(
            f"Unexpected error: {str(e)}"
        )
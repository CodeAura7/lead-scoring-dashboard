import streamlit as st
import pandas as pd
from scoring import calculate_score

st.set_page_config(page_title="Biotech Lead Scoring", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("data/lead.csv")
    df["score"] = df.apply(calculate_score, axis=1)
    df = df.sort_values("score", ascending=False).reset_index(drop=True)
    df["rank"] = range(1, len(df) + 1)
    return df

def filter_data(df, search_term, score_range):
    filtered = df.copy()
    
    if search_term:
        search_lower = search_term.lower()
        mask = (
            filtered["title"].str.lower().str.contains(search_lower, na=False) |
            filtered["company"].str.lower().str.contains(search_lower, na=False) |
            filtered["person_location"].str.lower().str.contains(search_lower, na=False) |
            filtered["company_hq"].str.lower().str.contains(search_lower, na=False)
        )
        filtered = filtered[mask]
    
    filtered = filtered[
        (filtered["score"] >= score_range[0]) & 
        (filtered["score"] <= score_range[1])
    ]
    
    filtered = filtered.reset_index(drop=True)
    filtered["rank"] = range(1, len(filtered) + 1)
    
    return filtered

def main():
    st.title("🧬 Biotech Lead Scoring Dashboard")
    st.markdown("Prioritize business development leads based on strategic fit and engagement signals")
    
    df = load_data()
    
    st.sidebar.header("Filters")
    
    search_term = st.sidebar.text_input(
        "Search (title, company, location)",
        placeholder="e.g., toxicology, San Francisco"
    )
    
    score_range = st.sidebar.slider(
        "Score Range",
        min_value=0,
        max_value=100,
        value=(0, 100),
        step=5
    )
    
    filtered_df = filter_data(df, search_term, score_range)
    
    st.sidebar.markdown("---")
    st.sidebar.metric("Total Leads", len(df))
    st.sidebar.metric("Filtered Leads", len(filtered_df))
    st.sidebar.metric("Avg Score (Filtered)", f"{filtered_df['score'].mean():.1f}")
    
    display_df = filtered_df[[
        "rank", "score", "name", "title", "company", 
        "person_location", "company_hq", "email", "linkedin_url"
    ]].copy()
    
    display_df.columns = [
        "Rank", "Score", "Name", "Title", "Company",
        "Person Location", "Company HQ", "Email", "LinkedIn"
    ]
    
    st.dataframe(
        display_df,
        use_container_width=True,
        height=600,
        column_config={
            "LinkedIn": st.column_config.LinkColumn("LinkedIn"),
            "Score": st.column_config.NumberColumn(
                "Score",
                format="%d",
            ),
        }
    )
    
    csv = filtered_df[[
        "rank", "score", "name", "title", "company", 
        "person_location", "company_hq", "email", "linkedin_url",
        "funding_stage", "uses_invitro", "open_to_nams", 
        "recent_publication", "hub_location"
    ]].to_csv(index=False)
    
    st.download_button(
        label="📥 Export Filtered Results (CSV)",
        data=csv,
        file_name="filtered_leads.csv",
        mime="text/csv"
    )
    
    with st.expander("ℹ️ Scoring Methodology"):
        st.markdown("""
        **Lead scores are calculated based on:**
        
        - **+30 points**: Title relevance (toxicology, safety, preclinical, hepatic, 3D)
        - **+20 points**: Funding stage (Series A or B)
        - **+15 points**: Currently uses in vitro models
        - **+10 points**: Open to NAMs (New Approach Methodologies)
        - **+10 points**: Located near innovation hub
        - **+40 points**: Recent publication (strong research engagement signal)
        
        **Maximum Score**: 100 points (capped)
        """)

if __name__ == "__main__":
    main()
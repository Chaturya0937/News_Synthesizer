import streamlit as st
import time
from agents.controller_agent import run_agentic_pipeline

st.set_page_config(page_title="NewsSynth Pro", layout="wide")

# Sidebar for Discovery (Google News Style)
st.sidebar.title("Personalize Feed")
selected_genres = st.sidebar.multiselect(
    "Choose Interests:",
    ["Technology", "Business", "Sports", "Politics", "Science"],
    default=["Technology"]
)

st.title("📰 NewsSynth Pro: Truth-Seeking AI")

# Standard Search Bar
search_query = st.text_input("Search for specific news:", placeholder="e.g., SpaceX Launch")

if st.button("🔍 Synthesize News") or (not search_query and selected_genres):
    # Use search query if typed, otherwise use first selected genre
    target_topic = search_query if search_query.strip() else selected_genres[0]
    
    with st.spinner(f"Analyzing {target_topic}..."):
        start_time = time.time()
        results = run_agentic_pipeline(target_topic)
        end_time = time.time()

        st.success(f"Analysis complete in {end_time - start_time:.2f}s")

        for idx, article in enumerate(results, start=1):
            with st.container():
                st.markdown(f"### {idx}. {article['title']}")
                st.write(article["summary"])
                st.divider()

import streamlit as st
import time
from agents.controller_agent import run_agentic_pipeline

st.set_page_config(page_title="NewsSynth Pro", layout="wide")

# New Discovery Sidebar
st.sidebar.title("Personalize Feed")
selected_genres = st.sidebar.multiselect(
    "Choose Interests:",
    ["Technology", "Business", "Sports", "Politics", "Entertainment"],
    default=["Technology"]
)

st.title("📰 NewsSynth Pro: Truth-Seeking AI")
st.subheader("Powered by Groq + LLaMA 3.1 + Gemini 2.0")

# Existing Search Box
search_query = st.text_input("Enter a news topic:", placeholder="e.g., SpaceX Launch")

if st.button("🔍 Synthesize News"):
    # If search is empty, automatically use the first selected genre
    target_topic = search_query if search_query.strip() else selected_genres[0]
    
    with st.spinner(f"Scouting and Auditing '{target_topic}'..."):
        start_time = time.time()
        results = run_agentic_pipeline(target_topic)
        end_time = time.time()

        st.success(f"Analysis complete in {end_time - start_time:.2f}s") #

        for idx, article in enumerate(results, start=1):
            st.markdown(f"### {idx}. {article['title']}")
            st.write(article["summary"])
            st.divider() #

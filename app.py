import streamlit as st
import time
from agents.controller_agent import run_agentic_pipeline

# Page configuration
st.set_page_config(
    page_title="Agentic AI News Synthesizer",
    layout="wide"
)

# Title
st.title("📰 Agentic AI News Synthesizer")
st.subheader("Powered by Groq + LLaMA 3.1")

st.markdown(
    """
    This application fetches live news and generates concise summaries using
    an **Agentic AI system** with autonomous agents.
    """
)

# Input box
topic = st.text_input(
    "Enter a news topic:",
    placeholder="e.g., Artificial Intelligence, Agriculture, Sports"
)

# Button
if st.button("🔍 Generate News Summary"):
    if not topic.strip():
        st.warning("Please enter a valid topic.")
    else:
        with st.spinner("Fetching news and generating summaries..."):
            start_time = time.time()

            results = run_agentic_pipeline(topic)

            end_time = time.time()

        st.success("Done!")

        st.info(f"⏱️ Total Execution Time: {end_time - start_time:.2f} seconds")

        # Display results
        for idx, article in enumerate(results, start=1):
            st.markdown(f"### {idx}. 📰 {article['title']}")
            st.write(article["summary"])
            st.divider()

# Footer
st.markdown("---")
st.caption("Minor Project | Agentic AI News Synthesizer")

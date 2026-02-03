from agents.controller_agent import run_agentic_pipeline

results = run_agentic_pipeline("machine learning")

for r in results:
    print("\n📰", r["title"])
    print("✍️", r["summary"])



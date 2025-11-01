import requests
import json
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))


# config
APIFY_URL = "https://api.apify.com/v2/datasets/TceF9McOaOqTyF4r6/items?format=json"
DIGEST_FILE = "superclanek_digest.txt"
AI_FILE = "superclanek_ai.txt"
MAX_SUMMARY_ARTICLES = 3

# Load dataset
print("Loading dataset from Apify...")
data = requests.get(APIFY_URL).json()
print(f"Loaded {len(data)} articles.")

# Deduplicate (using url)
seen_urls = set()
unique_articles = []
for a in data:
    url = a.get("url")
    if url and url not in seen_urls:
        unique_articles.append(a)
        seen_urls.add(url)

print(f"Filtered down to {len(unique_articles)} unique articles.")

# Create readable digest
with open(DIGEST_FILE, "w", encoding="utf-8") as f:
    for a in unique_articles:
        title = a.get("headers", {}).get("title", "No title")
        timestamp = a.get("metadata", {}).get("datePublished", "No date")
        category = a.get("metadata", {}).get("articleSection", "No category")
        summary = a.get("text", "").strip().replace("\n", " ")
        url = a.get("url", "")

        f.write("---\n")
        f.write(f"📰 {title}\n")
        f.write(f"📅 {timestamp} | 🏷️ {category}\n")
        f.write(f"{summary}\n")
        f.write(f"🔗 {url}\n\n")

print(f"Readable digest saved to {DIGEST_FILE}.")

# create superčlánek
texts_for_ai = [a.get("text", "") for a in unique_articles[:MAX_SUMMARY_ARTICLES] if a.get("text")]

merged_text = "\n\n".join(texts_for_ai)
prompt = f"""
You are a neutral journalist AI.
Create a single, unbiased summary article ("superčlánek") combining these sources:
{merged_text}
"""

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[{"role": "user", "content": prompt}]
)

superclanek = response.choices[0].message.content

with open(AI_FILE, "w", encoding="utf-8") as f:
    f.write(superclanek)

print(f"AI-summarized superčlánek saved to {AI_FILE}.\n")
print("📰 SUPERČLÁNEK (preview):\n")
print(superclanek[:500] + "...")  # preview first 1000 characters

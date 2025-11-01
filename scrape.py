import requests
import json
from urllib.parse import urlparse

# -----------------------------
# CONFIGURATION
# -----------------------------
APIFY_URL = "https://api.apify.com/v2/datasets/TceF9McOaOqTyF4r6/items?format=json"
OUTPUT_FILE = "articles.json"

# -----------------------------
# LOAD DATA
# -----------------------------
print("Loading dataset from Apify...")
data = requests.get(APIFY_URL).json()
print(f"Loaded {len(data)} items.")

# -----------------------------
# REMOVE DUPLICATES (by URL)
# -----------------------------
seen_urls = set()
unique_articles = []

for a in data:
    url = a.get("url")
    if url and url not in seen_urls:
        unique_articles.append(a)
        seen_urls.add(url)

print(f"Filtered down to {len(unique_articles)} unique articles.")

# -----------------------------
# EXTRACT REQUIRED FIELDS
# -----------------------------
extracted_articles = []

for a in unique_articles:
    # Get nested structures
    metadata = a.get("metadata", {})
    openGraph = metadata.get("openGraph", [{}])
    jsonLd = metadata.get("jsonLd", [{}])

    # Convert lists to first item if they exist
    if isinstance(openGraph, list) and openGraph:
        openGraph = openGraph[0]
    if isinstance(jsonLd, list) and jsonLd:
        jsonLd = jsonLd[0]

    # Extract URL
    url = a.get("url") or metadata.get("canonicalUrl") or ""

    # Extract domain from URL
    domain = ""
    if url:
        parsed = urlparse(url)
        domain = parsed.netloc

    # Extract publish_date
    publish_date = (
        jsonLd.get("datePublished")
        or jsonLd.get("dateModified")
        or openGraph.get("article:published_time")
        or openGraph.get("og:published_time")
        or a.get("crawl", {}).get("loadedTime")
        or ""
    )

    # Extract language
    language = (
        metadata.get("languageCode")
        or openGraph.get("og:locale")
        or jsonLd.get("inLanguage")
        or ""
    )

    # Extract title
    title = (
        metadata.get("title")
        or openGraph.get("og:title")
        or openGraph.get("title")
        or jsonLd.get("headline")
        or jsonLd.get("name")
        or ""
    )

    # Extract description
    description = (
        metadata.get("description")
        or openGraph.get("og:description")
        or openGraph.get("description")
        or jsonLd.get("description")
        or ""
    )

    # Extract text
    text = a.get("text", "")
    
    # Extract keywords
    keywords = metadata.get("keywords", "")
    
    # Create article object
    article = {
        "url": url,
        "domain": domain,
        "publish_date": publish_date,
        "language": language,
        "title": title,
        "description": description,
        "text": text,
        "keywords": keywords
    }

    extracted_articles.append(article)

# -----------------------------
# SAVE TO JSON FILE
# -----------------------------
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(extracted_articles, f, indent=2, ensure_ascii=False)

print(f"\n✅ Extracted {len(extracted_articles)} articles to {OUTPUT_FILE}")

# Print sample of first article
if extracted_articles:
    print("\n📄 Sample (first article):")
    print(json.dumps(extracted_articles[0], indent=2, ensure_ascii=False)[:500])
    print("...")
# YELZ MVP - 4 Core Features

## 1. Scraping (3-4 hours)
**Input:** User prompt → Find legit sites → RSS feeds → Save
**Tools:** newspaper4k + firecrawl fallback

### Tasks:
- [ ] **Hour 1:** RSS feed discovery from user prompt
- [ ] **Hour 2:** newspaper4k scraping pipeline  
- [ ] **Hour 3:** Firecrawl fallback for tough sites
- [ ] **Hour 4:** Extract text + metadata + images

**Output:** Articles stored in database

---

## 2. Article Generation (3-4 hours)
**Input:** X articles → 1 super-article
**Tools:** DeepInfra API + prompts

### Tasks:
- [ ] **Hour 1:** DeepInfra API integration
- [ ] **Hour 2:** Article clustering (group related articles)
- [ ] **Hour 3:** Super-article generation prompt
- [ ] **Hour 4:** Format output: TLDR + content + source comparison

**Output:** Super-articles with structured content

---

## 3. Translation (2-3 hours)
**Input:** Super-articles in EN → Multiple languages
**Tools:** DeepInfra translation

### Tasks:
- [ ] **Hour 1:** Translation API setup
- [ ] **Hour 2:** Language switcher logic
- [ ] **Hour 3:** Batch translate all super-articles per language

**Output:** Super-articles available in N languages

---

## 4. User Selection (2-3 hours)
**Input:** User prompt for article selection
**Tools:** Simple UI

### Tasks:
- [ ] **Hour 1:** Prompt interface for topic selection
- [ ] **Hour 2:** Article filtering and display
- [ ] **Hour 3:** Simple responsive UI

**Output:** Curated feed based on user interests

---

## Tech Stack (Minimal)
- **Backend:** FastAPI + PostgreSQL
- **Scraping:** newspaper4k + firecrawl  
- **AI:** DeepInfra API
- **Frontend:** React/HTML + CSS
- **Deploy:** Railway + Vercel

## Database (3 tables)
```sql
articles (id, title, content, url, source, images, metadata)
super_articles (id, title, tldr, content, source_comparison, language)  
users (id, email, language_prefs, topic_interests)
```

## File Structure
```
├── scraping/
│   ├── rss_finder.py      # prompt → RSS discovery
│   ├── article_scraper.py # newspaper4k + firecrawl
│   └── content_parser.py  # text + metadata + images
├── generation/
│   ├── llm_client.py      # DeepInfra integration
│   ├── clustering.py      # group related articles
│   └── synthesis.py       # X articles → 1 super
├── translation/
│   ├── translator.py      # multi-language support
│   └── language_manager.py # user language prefs
├── ui/
│   ├── topic_selector.py  # user prompt interface
│   ├── feed_generator.py  # article filtering
│   └── frontend/          # React components
└── main.py               # FastAPI app
```

**Total:** 10-14 hours for complete MVP

Ready to start with which component?
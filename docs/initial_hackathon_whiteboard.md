# Plán Hackathonu

## Cíle Hackathonu

1. **Global Novinář App**

## Databáze

## LLM Model Arena

---

## THE APP

### 1. Scraping

- **prompt** → najít legit stránky → RSS Feed → uložit
- **Crawling skrz stránky z RSS:**
  - newspaper 4K
  - firecrawl

**Stránka (co z ní chceme dostat):**
- text
- metadata
- extra: obrázek

### 2. Generování článků

- **LLM call, prompts**
- **deepinfra API**
- vygenerovany superclanek ma obsahovat:
  - shrnuti
  - text
  - zdroje

**Generace:** Z X článků → 1 superčlánek

**Superčlánek struktura obsahu:**
- summary TLDR
- text
- source comparison

### 3. Překládání

- **ikonka jazyka** (user settings)
- **každý set superčlánků je přeložen podle N jazyků, kde N je pocet unikatnich jazyku, ktere uzivatele chteji**

### 4. User Selection

- **prompt na výběr článků**
- **simple UI**, pouze UI pro selekci a zobrazení článků

## Topics

- **pandy** (welfare)
- **politika** (world)
- **ekonomika**
- **sport**

---

## IMPLEMENTACE

1. newspaper research
2. tech stack research
3. prompt engineering
   - generace článků
   - selekce článků -> similarity search / semantic /ranking / SQL/mcp prevod
4. DB návrh a implementace
5. Claude code research - jaké MCP servery a jake prompty pouzit pro jednotlive kroky

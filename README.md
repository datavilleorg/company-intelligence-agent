# Company Intelligence Agent

**Research any public company from two trustworthy sources at once — Wikimedia for context, SEC EDGAR for authoritative disclosures — with every claim linked back to where it came from.**

Built on [Dataville](https://dataville.com): one API and one MCP server over both datasets, so you don't build or maintain ingestion, parsing, entity matching or update infrastructure for either.

[Get a free API key](https://app.dataville.com/api-keys) · [Docs](https://docs.dataville.com) · [API reference](https://docs.dataville.com/api-reference/overview) · [Dataville MCP](https://github.com/datavilleorg/dataville-mcp) · [Wikimedia package](https://github.com/datavilleorg/dataville-wikimedia) · [SEC EDGAR package](https://github.com/datavilleorg/dataville-sec-edgar) · [Live demos](https://app.dataville.com/demos)

> **Status: in active development.** The quickstart below runs today against the live Dataville API.
> The full agent (entity resolution, LLM reasoning layer, UI) is being built in this repo — watch or star it to follow along.

```
Company name ──▶ Dataville ──┬─▶ Wikimedia: description, history, products, people, related entities
                             └─▶ SEC EDGAR: 10-K / 10-Q / 8-K filings, XBRL financials, material events
                                       │
                                       ▼
                     Reasoning layer ──▶ Source-linked brief
                                         (each claim tagged Wikimedia or SEC EDGAR)
```

**One application. Multiple trustworthy sources. Provenance preserved.**

---

## 60-second quickstart

No key is needed to try it (anonymous use allows 50 requests a day per IP address). Add `Authorization: Bearer $DATAVILLE_API_KEY` for full quota.

### cURL

```bash
curl "https://api.dataville.com/wiki/Apple%20Inc."
curl "https://api.dataville.com/edgar/AAPL"
```

### Python

```bash
python examples/company_brief.py "Apple Inc." AAPL
```

### JavaScript / TypeScript (Node 18+)

```bash
node examples/company-brief.mjs "Apple Inc." AAPL
```

Output (abridged):

```
# Apple Inc.

## Context (Wikimedia — trustworthy, source-linked knowledge)
Apple Inc. is an American multinational technology company headquartered in Cupertino…
Source: https://en.wikipedia.org/wiki/Apple_Inc.
Credit: Wikipedia contributors — CC-BY-SA-4.0

## Disclosures (SEC EDGAR — authoritative primary source)
Latest filing: Apple Inc. — 10-Q (2026-07-31)
  revenue: $364.36B
  net income: $101.46B
Source: https://www.sec.gov/Archives/edgar/data/320193/000032019326000020/aapl-20260627.htm
```

### MCP (Claude, Cursor, VS Code, any MCP client)

```bash
claude mcp add --transport http dataville https://api.dataville.com/mcp
```

Then ask: *"Using Dataville, give me a brief on Microsoft — background from Wikipedia and its latest SEC financials, with sources."*

---

## Why Dataville?

SEC EDGAR and Wikimedia are both free, so it's fair to ask. Doing this yourself means:

- Two different APIs, auth models, rate limits and response formats.
- Resolving a company name to a Wikipedia article *and* a ticker/CIK.
- Parsing XBRL into comparable financial fields, aligned to a single reporting period.
- Keeping a Wikipedia corpus fresh, and tracking attribution and licensing for redistribution.

Dataville handles that layer and gives you one consistent response shape: `title`, `body`, `last_updated` and `metadata` with source URLs, plus an `attribution` block wherever the license requires one.

## Sources

| | Wikimedia | SEC EDGAR |
|---|---|---|
| **What it is** | Trustworthy, source-linked knowledge — community-edited, not guaranteed authoritative | Authoritative, primary-source company disclosures |
| **Provides** | Company description, history, products, people, categories, Wikidata entity | Filings (10-K, 10-Q, 8-K, Form 4…), XBRL financials, SIC industry, tickers, CIK |
| **Freshness** | Wikimedia Enterprise snapshot + hourly update batches | Fetched from SEC on request, cached up to 30 min |
| **Provenance** | `metadata.url` (article), `metadata.main_entity` (Wikidata) | `metadata.document_url`, `accession_number`, `index_url` |
| **Rights** | CC BY-SA 4.0 — credit Wikimedia; see the `attribution` block in each response | US government public data |

## What you'll be able to build

- **Company research briefs** — background + financials + recent material events, cited.
- **Competitive monitoring** — watch a set of companies for new filings or changes to their Wikipedia context.
- **Due-diligence agents** — answer questions where context and disclosures must be kept distinct.
- **Knowledge-base enrichment** — attach authoritative financials to entity pages in your own KB or RAG index.

## Roadmap

- [x] Live quickstart: cURL, Python, JS, MCP
- [ ] Entity resolution: company name → Wikipedia article + ticker/CIK
- [ ] Filing sections: risk factors, MD&A, material events
- [ ] Reasoning layer with per-claim source attribution
- [ ] Web UI + live demo
- [ ] Tests and `.env.example`-driven setup

## Learn more

- [Enrich an onboarding record with a company's filing and background](https://docs.dataville.com/guides/onboarding-enrichment): the same Wikimedia + EDGAR pairing, step by step
- [Profile a client's competitors from Claude and Data Studio](https://docs.dataville.com/guides/competitor-scan)
- [Quickstart: API](https://docs.dataville.com/quickstart) · [Connect an AI tool](https://docs.dataville.com/ai-tools) · [Response format](https://docs.dataville.com/response-format)

## Related

- [`dataville-wikimedia`](https://github.com/datavilleorg/dataville-wikimedia) — build with Wikimedia through Dataville
- [`dataville-sec-edgar`](https://github.com/datavilleorg/dataville-sec-edgar) — build with SEC EDGAR through Dataville
- [`dataville-mcp`](https://github.com/datavilleorg/dataville-mcp) — Dataville MCP server

## Start building

**[Get a free API key →](https://app.dataville.com/api-keys)** · Questions: support@dataville.com

Wikipedia content is © Wikipedia contributors, CC BY-SA 4.0. This project is not affiliated with or endorsed by the Wikimedia Foundation or the U.S. Securities and Exchange Commission. Code in this repo is [MIT](LICENSE).

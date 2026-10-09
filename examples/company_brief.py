"""Company brief: Wikimedia context + SEC EDGAR disclosures, every claim source-linked.

    DATAVILLE_API_KEY=dataville_... python examples/company_brief.py "Apple Inc." AAPL

Runs without a key too, at anonymous rate limits.
"""
import os
import sys
import urllib.parse
import urllib.request
import json

API = "https://api.dataville.com"


def dataville(source: str, keywords: str) -> dict:
    url = f"{API}/{source}/{urllib.parse.quote(keywords)}"
    req = urllib.request.Request(url)
    key = os.environ.get("DATAVILLE_API_KEY")
    if key:
        req.add_header("Authorization", f"Bearer {key}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)["data"]


def main(company: str, ticker: str) -> None:
    wiki = dataville("wiki", company)
    filing = dataville("edgar", ticker)
    fin = filing["metadata"].get("financials") or {}

    print(f"# {wiki['title']}\n")
    print("## Context (Wikimedia — trustworthy, source-linked knowledge)")
    print((wiki["metadata"].get("abstract") or "")[:400] + "…")
    print(f"Source: {wiki['metadata']['url']}")
    print(f"Credit: {wiki['attribution']['attribution']}\n")

    print("## Disclosures (SEC EDGAR — authoritative primary source)")
    print(f"Latest filing: {filing['title']}")
    for label in ("revenue", "net_income", "total_assets", "cash"):
        if fin.get(label):
            print(f"  {label.replace('_', ' ').capitalize()}: {fin[label]}")
    print(f"Source: {filing['metadata']['document_url']}")


if __name__ == "__main__":
    main(*(sys.argv[1:3] if len(sys.argv) >= 3 else ("Apple Inc.", "AAPL")))

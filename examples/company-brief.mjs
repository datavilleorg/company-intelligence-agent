// Company brief: Wikimedia context + SEC EDGAR disclosures, every claim source-linked.
//
//   DATAVILLE_API_KEY=dataville_... node examples/company-brief.mjs "Apple Inc." AAPL
//
// Node 18+. Runs without a key too, at anonymous rate limits.

const API = "https://api.dataville.com";

async function dataville(source, keywords) {
  const headers = process.env.DATAVILLE_API_KEY
    ? { Authorization: `Bearer ${process.env.DATAVILLE_API_KEY}` }
    : {};
  const res = await fetch(`${API}/${source}/${encodeURIComponent(keywords)}`, { headers });
  const body = await res.json();
  if (!res.ok) throw new Error(body?.data?.error ?? "Dataville request failed");
  return body.data;
}

const [company = "Apple Inc.", ticker = "AAPL"] = process.argv.slice(2);
const [wiki, filing] = await Promise.all([dataville("wiki", company), dataville("edgar", ticker)]);
const fin = filing.metadata.financials ?? {};

console.log(`# ${wiki.title}\n`);
console.log("## Context (Wikimedia — trustworthy, source-linked knowledge)");
console.log(`${(wiki.metadata.abstract ?? "").slice(0, 400)}…`);
console.log(`Source: ${wiki.metadata.url}`);
console.log(`Credit: ${wiki.attribution.attribution}\n`);

console.log("## Disclosures (SEC EDGAR — authoritative primary source)");
console.log(`Latest filing: ${filing.title}`);
for (const k of ["revenue", "net_income", "total_assets", "cash"]) {
  if (fin[k]) console.log(`  ${k.replace("_", " ")}: ${fin[k]}`);
}
console.log(`Source: ${filing.metadata.document_url}`);

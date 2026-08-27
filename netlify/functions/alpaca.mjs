// Read-only Alpaca paper proxy. Keys live in Netlify env vars, never in the page.
// Endpoint allowlist only - there is deliberately NO order/write path here.
const PAPER = "https://paper-api.alpaca.markets";
const DATA = "https://data.alpaca.markets";

export default async (req) => {
  const url = new URL(req.url);
  const what = url.searchParams.get("what");
  const key = process.env.ALPACA_PAPER_KEY;
  const secret = process.env.ALPACA_PAPER_SECRET;
  if (!key || !secret) return json({ error: "proxy not configured" }, 500);

  let target;
  if (what === "account") target = `${PAPER}/v2/account`;
  else if (what === "positions") target = `${PAPER}/v2/positions`;
  else if (what === "quote") {
    const symbols = (url.searchParams.get("symbols") || "").replace(/[^A-Za-z,.]/g, "");
    if (!symbols) return json({ error: "symbols required" }, 400);
    target = `${DATA}/v2/stocks/quotes/latest?symbols=${symbols}`;
  } else return json({ error: "unknown what" }, 400);

  const res = await fetch(target, {
    headers: { "APCA-API-KEY-ID": key, "APCA-API-SECRET-KEY": secret },
  });
  const body = await res.text();
  return new Response(body, {
    status: res.status,
    headers: { "content-type": "application/json", "cache-control": "no-store" },
  });
};

const json = (obj, status = 200) =>
  new Response(JSON.stringify(obj), { status, headers: { "content-type": "application/json", "cache-control": "no-store" } });

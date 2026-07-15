---
name: shared-data-gateway
description: Use George's quota-controlled DataForSEO and Apify gateway from Codex cloud for search demand, SERP research, market research, local-business discovery, competitor research, website verification, and other cross-project data tasks. Trigger when a task needs DataForSEO, Apify, Google Places data, keyword volumes or ideas, organic search results, or browser-derived website evidence.
---

# Shared data gateway

Use the installed `seo-gateway` client as a shared data capability. If it is not on `PATH`, invoke `/root/.local/bin/seo-gateway` directly.

Never print `SEO_GATEWAY_TOKEN`, provider credentials, request headers, credential-bearing URLs, or environment-variable values. Report only whether named configuration is present.

## Start safely

Run `seo-gateway capabilities` when the required operation is unclear. Run `seo-gateway status` only to diagnose connectivity; it checks both providers without launching paid jobs.

Do not bypass the gateway with direct DataForSEO or Apify credentials. Do not invent routes, actor IDs, task IDs, run IDs, or dataset IDs.

## DataForSEO

Write one JSON task array, then use one approved operation:

```sh
seo-gateway dataforseo serp-google-organic tasks.json
seo-gateway dataforseo google-ads-search-volume tasks.json
seo-gateway dataforseo google-keyword-ideas tasks.json
```

Examples:

```json
[{"keyword":"emergency plumber exeter","location_code":2826,"language_code":"en","device":"desktop"}]
```

```json
[{"keywords":["boiler repair exeter","emergency plumber exeter"],"location_code":2826,"language_code":"en"}]
```

Use this provider for tasks such as market sizing, topic demand, competitor visibility, search-result evidence, content planning, and local-search research. The current allowlist is intentionally narrower than the full DataForSEO API.

## Apify

The approved actors are:

- `compass/crawler-google-places` for local-business and competitor discovery.
- `apify/rag-web-browser` for bounded website research or verification.

Start asynchronously, poll the returned run ID, then read only its registered dataset:

```sh
seo-gateway apify-run apify/rag-web-browser input.json
seo-gateway apify-status RUN_ID
seo-gateway apify-items DATASET_ID 20 0
```

Use `maxResults: 1` for one-URL verification. Google Places is capped at 15 places per search; paid enrichment and personal-data options are blocked.

## Spend and integrity rules

- Use the smallest result size that answers the task.
- Batch search-volume keywords into one permitted task where practical.
- Reuse the original `SEO_IDEMPOTENCY_KEY` when retrying the same paid POST.
- Never retry around quota or duplicate-request errors.
- Never read arbitrary Apify run or dataset IDs; use only IDs returned by this gateway session.
- Distinguish provider evidence from inference in the final answer.
- State when the current allowlist cannot support the requested operation instead of falling back to direct provider access.

# Meta CLI & SDK Reference

### What's installed (as of 2026-05-04)
- `meta` CLI: PyPI `meta-ads` v1.0.1 at `/Users/georgelane/.local/bin/meta`
- Wraps the Meta Marketing API (Graph) — campaigns, ad sets, ads, creatives, insights, datasets/pixels, catalogs
- Does **not** expose the Conversions API event endpoint. For CAPI, use the SDKs.

### Authentication
The CLI reads three env vars: `ACCESS_TOKEN`, `AD_ACCOUNT_ID`, `BUSINESS_ID`. It auto-loads `.env` from the current working directory.

**The user's local setup remaps from `.env.local` (META_*-prefixed) to the CLI's expected names** via a `meta()` shell function in `~/.zshenv`. Three working invocations:

```bash
# A) cd into the project that has .env  (simplest)
cd "/Users/georgelane/Dropbox/Projects/Lane Consultancy Web Design"
meta auth status

# B) Use zsh shim so creds load from ~/.zshenv anywhere
zsh -c 'meta auth status'

# C) Export manually (works in any shell)
ENV_FILE="/Users/georgelane/Dropbox/Projects/Lane Consultancy Web Design/.env.local"
export ACCESS_TOKEN=$(awk -F= '/^META_ACCESS_TOKEN=/{sub(/^META_ACCESS_TOKEN=/,""); print; exit}' "$ENV_FILE")
export AD_ACCOUNT_ID=$(awk -F= '/^META_ACCOUNT_ID=/{sub(/^META_ACCOUNT_ID=/,""); print; exit}' "$ENV_FILE")
export BUSINESS_ID=$(awk -F= '/^META_BUSINESS_ID=/{sub(/^META_BUSINESS_ID=/,""); print; exit}' "$ENV_FILE")
meta auth status
```

For new projects, copy the same META_*-prefixed keys into a `.env.local` and either rely on the `~/.zshenv` shim or add a project-level `.env` with the unprefixed names.

### Default account & multi-account workflow
Default ad account: `act_88999896`. To target another account, pass per command:

```bash
meta --ad-account-id act_237498386928767 ads campaign list
```

### Output formats
```bash
meta ads campaign list                 # human-readable table
meta ads campaign list -o json         # for jq / scripting
meta ads campaign list -o plain        # bare values, easy diffing
```

For any list/insights piping into `jq`, prefer `-o json`.

### The everyday commands
| Goal | Command |
|------|---------|
| Sanity check | `meta auth status` |
| Confirm account | `meta ads adaccount current` |
| List campaigns | `meta ads campaign list` |
| Inspect one | `meta ads campaign get <ID>` |
| Performance (last 7d) | `meta ads insights get --date-preset last_7d` |
| Per-campaign perf | `meta ads insights get --campaign-id <ID> --date-preset last_14d --fields spend,actions,cost_per_action_type,frequency` |
| List pixels | `meta ads dataset list` |
| List creatives | `meta ads creative list` |
| List catalogs | `meta ads catalog list` |

### Budgets are in cents — the gotcha
| Intent | Flag value |
|-------|-----------|
| £24/day | `--daily-budget 3000` (= $30.00) |
| £40/day | `--daily-budget 5000` (= $50.00) |
| £60/day | `--daily-budget 7500` (= $75.00) |
| £80/day | `--daily-budget 10000` (= $100.00) |
| £160/day | `--daily-budget 20000` (= $200.00) |

USD-denominated regardless of account currency. Convert to local currency by current FX. **Always preview a created campaign before activating** — default status is PAUSED for exactly this reason.

### Safety pattern: create paused, preview, activate
```bash
# 1. Create (PAUSED by default)
meta ads campaign create --name "TEST_2026-05" --objective outcome_leads --daily-budget 3000

# 2. Get the ID and preview
meta ads campaign list -o json | jq '.[] | select(.name=="TEST_2026-05")'

# 3. Inspect ad sets / ads / creatives before activating
meta ads adset list --campaign-id <ID>
meta ads ad list --campaign-id <ID>

# 4. Activate when ready (do this in UI or via update)
meta ads campaign update <ID> --status active
```

### When the CLI isn't enough — drop to SDK
The CLI exposes the most common operations but not every Marketing API field. Reach for the official SDK when:
- Setting Lead-gen-specific knobs (Conversion Leads performance goal, Instant Form fields, conditional logic)
- Sending Conversions API events
- Bulk operations (>50 ads at a time)
- Custom audiences from a CSV
- Webhook subscriptions

**Official SDKs (both maintained by Meta):**
- Python: `pip install facebook-business` — [facebook-python-business-sdk](https://github.com/facebook/facebook-python-business-sdk)
- Node: `npm i facebook-nodejs-business-sdk` — [facebook-nodejs-business-sdk](https://github.com/facebook/facebook-nodejs-business-sdk)

For CAPI in the user's stack (Cloudflare Workers / Next.js on Vercel), the Node SDK works inside Workers with minimal adaptation; otherwise call the Graph API directly with `fetch` (the request shape is small enough not to need the SDK).

### When to stay in the Ads Manager UI
- First-time campaign of a new type — easier to verify settings visually
- Anything Conversion-Leads-related (the CLI doesn't yet surface every flag)
- Audience exclusion stacks
- Instant Form builder (no good API equivalent)

### Common pitfalls
| Pitfall | Symptom | Fix |
|---------|---------|-----|
| Forgot to set env vars | `Authentication required` | `cd` into project with `.env`, or use `zsh -c '...'` shim |
| Budget set in dollars not cents | Account spend 100× expected | Always × 100; preview before activating |
| Wrong ad account | Changes appear in wrong account | Pass `--ad-account-id act_XXX` explicitly when working on non-default accounts |
| Forgot CLI defaults to PAUSED | Created campaign isn't running | Update status to `active` once verified |
| Tried to send CAPI events via CLI | No such command | Use SDK or direct Graph API; see `conversions-api-setup.md` |

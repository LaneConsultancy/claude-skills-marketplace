# Retell AI Reference

Consolidated reference for dashboard navigation, agent settings with recommended defaults, pricing, and the full gotchas list. Load this when configuring settings, estimating costs, or debugging.

---

## 1. Dashboard map

`dashboard.retellai.com`. Sidebar sections:

| Section | What lives there |
|---|---|
| **Agents** | Create/edit voice agents and chat agents. Agent versions. Templates. A/B testing. |
| **Conversation Flows** | Visual graph agents. Components library (reusable subflows). |
| **Knowledge Base** | Upload URLs (auto-crawled), files (25 max, 50MB each), or custom text snippets. Attach to agents. |
| **Tools / Functions** | Built-in tools (End Call, Transfer, Press Digit, Capture DTMF, Send SMS, Code, MCP) and custom HTTP tools. |
| **Phone Numbers** | Buy Retell numbers, import via SIP, bind to agents, view KYC status. |
| **Batch Calls** | Create, upload CSV, schedule, monitor outbound campaigns. |
| **Chats** | Chat agents and widget config. |
| **Call History** | Transcripts, recordings, latency, analysis per call. Filters by agent, number, date. |
| **Analytics** | Aggregate performance metrics across agents. |
| **AI QA** | Cohorts, resolution criteria, automated scoring of production calls. |
| **Simulation Testing** | Automated pre-production test cases. Batch Testing runs many at once. |
| **LLM Playground** | Browser chat against agent config without placing a real call. |
| **Webhooks** | Account-level webhook URL and signing key. |
| **Alerts** | Threshold-based notifications on metrics. |
| **Billing** | Usage, credits, payment method, subscription, concurrency limit. |
| **API Keys** | Create/revoke workspace-scoped auth keys and public keys. |
| **Workspace / Access Control** | Team members, permissions. |
| **Compliance & Data** | Data retention, storage mode (everything / no-PII / basic-only), BAA/DPA self-sign portal. |

**Workspace selector:** top-left corner. Click to switch between workspaces. Always verify the current workspace before making changes.

---

## 2. Agent settings (all the dials)

### 2.1 Identity & response engine

| Field | Required | Notes |
|---|---|---|
| Name | ✓ | Internal label. Not spoken. |
| Response Engine | ✓ | Retell LLM (single/multi prompt) or Conversation Flow or Custom LLM (WebSocket). |
| Voice | ✓ | Platform voice (default), ElevenLabs, OpenAI, Cartesia, MiniMax, Fish, Deepgram, or custom clone. |
| Language | ✓ | Per-provider support varies: ElevenLabs 32+, OpenAI 40+, Cartesia 14+, MiniMax 38+. |
| Webhook URL | Optional | Account-level default if unset. Per-agent overrides account. |

### 2.2 Voice & speech

| Field | Default | Range | Recommended |
|---|---|---|---|
| `voice_speed` | 1.0 | 0.5–2.0 | 1.0–1.05 for most use cases. Slower for elderly/accessibility audiences. |
| `voice_temperature` | provider default | — | Leave at default unless tuning for specific emotion. |
| Dynamic speed to user WPM | off | toggle | Turn on for accessibility. |
| Boosted keywords | empty | list | Add brand names, customer names, uncommon terminology. Critical for STT accuracy. |
| Speech normalization | on | toggle | Keep on. Converts "2025" → "twenty twenty-five", "$5" → "five dollars". |
| Pronunciation guides | empty | list | Phonetic overrides for proper nouns (e.g., "Cloudways" → "cloud-ways"). |

### 2.3 Turn-taking & interruptions

| Field | Default | Range | Recommended |
|---|---|---|---|
| `interruption_sensitivity` | 1.0 | 0–1 | **0.7 for noisy environments (trade calls, cars, construction sites). 1.0 for quiet environments.** Too high = agent stops talking constantly. |
| `responsiveness` | provider default | — | Lower = more natural pauses. Higher = faster responses. Default is usually right. |
| `enable_backchannel` | off | toggle | **On for warm/customer-service tone**. Off for transactional/IVR flows. |
| `backchannel_frequency` | 0.8 | 0–1 | 0.5–0.7 if backchannels feel too aggressive. |
| `backchannel_words` | provider-specific | list | ElevenLabs EN default: "okay", "uh-huh", "mhmm", "yah". OpenAI drops "mhmm". |
| Reminder frequency / trigger | off | — | Turn on for calls where silence is likely (elderly, distracted users). Nudges after silence. |
| `end_call_after_silence_ms` | 30000 | ms | **Keep at 30s for normal calls, lower to 15s for transactional.** |
| Pause before speaking | 0 | ms | Add 300–500ms for outbound calls — sounds less robotic immediately after pickup. |
| Background sound | none | office/cafe/none | Use sparingly. "Office" works for B2B sales. None is safer. |
| `max_call_duration_ms` | 3600000 (1h) | up to 2h | Lower to 600000 (10min) for qualification calls to hard-cap runaway calls. |

### 2.4 Openings & closings

| Field | Notes |
|---|---|
| Agent-first vs user-first | Agent-first: agent speaks first on pickup. Required for outbound. User-first: waits for caller. Use user-first for inbound where voicemail detection matters. |
| Begin message | Fixed string OR "let LLM generate". Fixed is faster, cheaper (no 10s billing minimum if LLM generates). **Recommend fixed for outbound** to avoid the 10-second billing minimum. |
| Voicemail detection | off | on | **On for outbound. Configure leave-message behaviour or hang-up.** |

### 2.5 Guardrails & handbook

| Feature | Default | Notes |
|---|---|---|
| Agent Handbook presets | Default Personality + AI Disclosure When Asked are **on by default** for new agents. | Each preset costs 30–910 tokens. Turn off presets you don't need. |
| Guardrails | configurable | Content safety bands. Keep on for customer-facing agents. |
| Scope Boundaries | off | Preset that stops agent from going off-topic. Turn on for narrow-purpose agents (qualifier, booking). |
| Natural Filler Words | off | Adds "um", "let me think" for conversational feel. Good for sales, bad for transactional. |

### 2.6 LLM settings

| Field | Recommended |
|---|---|
| Model | **GPT 4.1** — default recommendation. Best quality/cost balance ($0.045/min). GPT 5 nano ($0.003/min) for extreme cost-sensitivity but expect quality drop. Claude 4.6 Sonnet or GPT 5.4 ($0.08/min) for complex reasoning or empathy-heavy use cases. |
| Temperature | 0.0–0.3 for data capture/appointments. 0.4–0.7 for sales/CS (default here). 0.8–1.0 for creative. |
| Structured Output | On when you need reliable tool-call formatting or specific response schemas. Slower saves. |
| Fast Tier | 1.5× LLM rate. Turn on if latency variance is visibly hurting calls. |

### 2.7 Knowledge base (RAG)

| Field | Default | Notes |
|---|---|---|
| `chunk_count` | 3 | 1–10. Raise to 5–7 for long knowledge bases where retrieval misses answers. |
| Similarity threshold | 0.6 | Raise to 0.7 to avoid irrelevant retrieval. Lower to 0.5 if retrieval is too strict. |
| Auto-crawl refresh | 24h | For URL sources. |

**Limits per KB:** 500 URLs, 25 files (50MB each), 50 text snippets, 200 exclusions per path / 500 total. Stack multiple KBs to exceed.

**Cost:** $0.005/min OR $8/month flat. Flat rate wins above ~26 hours of calls per month.

---

## 3. Pricing math

All per-minute unless stated. Source: https://www.retellai.com/pricing

### Base components (always billed)

| Component | Cost/min |
|---|---|
| Retell voice infrastructure | $0.055 |
| Platform/Retell TTS (included) | $0.015 |

### LLM (pick one)

| Model | Cost/min |
|---|---|
| GPT 5 nano | $0.003 |
| Gemini 2.5 Flash | $0.035 |
| **GPT 4.1 (recommended default)** | **$0.045** |
| Claude 4.6 Sonnet | $0.080 |
| GPT 5.4 | $0.080 |

### Premium voice surcharge (replaces Platform TTS)

| Provider | Surcharge/min |
|---|---|
| ElevenLabs | +$0.025 (so $0.040 total instead of $0.015) |
| Cartesia / MiniMax / Fish / OpenAI | $0 (same as platform) |

### Telephony

| Type | Cost/min |
|---|---|
| US via Twilio (default) | $0.015 |
| International | varies by country |

### Add-ons

| Feature | Cost |
|---|---|
| Phone number (standard) | $2/month |
| Phone number (verified) | $10/month |
| Branded Calls | $0.10/outbound call |
| Knowledge Base retrieval | $0.005/min OR $8/month flat |
| Fast Tier | LLM cost × 1.5 |
| Concurrency burst (over limit) | $0.10/min for the entire call |

### Worked examples

| Scenario | Per-minute | 3-min call |
|---|---|---|
| **Default** (Retell infra + platform TTS + GPT 4.1 + US Twilio) | $0.13 | $0.39 |
| Cost-optimized (+ GPT 5 nano) | $0.088 | $0.26 |
| Quality-optimized (+ Claude 4.6 + ElevenLabs) | $0.19 | $0.57 |
| Premium (+ GPT 5.4 + ElevenLabs + Fast Tier) | $0.25 | $0.75 |

### Billing traps

- **Dynamic opening message (LLM generates) = 10s minimum billed.** Fixed opening = actual duration. Use fixed for high-volume outbound.
- **Prompt > 3,500 tokens = duration × (tokens / 3500), rounded up.** Keep prompts lean. Agent Handbook + Conversation Flow Flex Mode both inflate tokens.

### Free tier

$10 signup credit. 20 concurrent calls included on PAYG. Subscriptions get volume discounts.

---

## 4. Gotchas (the full list)

Ordered roughly by frequency of biting people.

### Account / setup

- **Outbound requires KYC.** Submit during signup so it clears before you need it. The official docs (docs.retellai.com/accounts/kyc) confirm this for Retell-provisioned numbers.
- **KYC + imported Twilio numbers: status unclear.** The docs do NOT explicitly address whether KYC is required when outbound is initiated via a Twilio SIP trunk. Retell still originates the call (LLM + voice + SIP INVITE to Twilio), so platform-level KYC likely applies regardless of number source. **Treat as "required, likely" — submit KYC during signup and don't rely on the Twilio path to bypass it.** Test with a low-volume outbound call before launching any campaign; if Retell blocks the call with a KYC error, you know.
- **Sanctioned countries permanently blocked:** Cuba, Iran, North Korea, Syria, Russia, Belarus, Venezuela.
- **Workspace-level API keys.** Each workspace = its own key = its own MCP entry.

### Agent behaviour

- **Agent doesn't hang up unless told to.** Add End Call tool AND prompt it when to call: "When the user says goodbye, call end_call."
- **`retell_llm_dynamic_variables` must be strings.** Non-strings fail validation. Convert before passing.
- **Unset dynamic variables render as `{{varname}}` literally.** Provide defaults or defensive prompt handling.
- **Single Prompt fails beyond ~1000 words or 5+ tools.** Symptoms: missed instructions, skipped tool calls, inconsistent behaviour. Move to Multi-Prompt or Flow.
- **Backchannel word support varies by provider.** Test with your specific voice. Some voices choke on "mhmm".

### Telephony

- **E.164 format strictly enforced** (e.g., `+14155551234`). `ignore_e164_validation` only for custom telephony.
- **Twilio SIP import: username ≠ friendly name.** Friendly name is a display label. Use the SIP credential's actual configured username.
- **CPS defaults: Retell 1/sec, Twilio 5/sec, Telnyx 16/sec.** Raise via telephony provider settings, not Retell.
- **International: Retell-owned numbers support 15 countries.** Imported numbers depend on your provider.
- **SIP IP allowlist:** `18.98.16.120/30` (global), plus `143.223.88.0/21`, `161.115.160.0/19` (select US).

### Prompts & cost

- **Prompts over 3,500 tokens cost proportionally more.** Multiplier = tokens / 3,500 rounded up.
- **Flex Mode inlines everything** — often blows past 3,500 tokens. Use with cost-awareness.
- **Guardrails + Agent Handbook presets stack.** Each preset adds 30–910 tokens. Turn off what you don't need.
- **Speech normalization matters.** Without it, TTS may literally say "slash" for "/" or "one two three four" for years.

### Tools & webhooks

- **Custom function timeout is 2 minutes** but the agent needs to speak much sooner. Enable "Speak during execution" with a filler message ("Let me check that for you…") for slow APIs.
- **Custom function response capped at 15,000 characters.** Truncate on your end.
- **Cold transfer caller-ID defaults to the Retell number.** Configure "display original caller ID" for receptionist patterns where the recipient should see the caller.
- **Webhook timeout = 10s, 3 retries.** Make webhooks fast or queue async.
- **Webhook IP allowlist:** `100.20.5.228`.
- **Verify webhook signature** with `x-retell-signature` header using your API key. SDK helpers in Node/Python.

### Data & compliance

- **Recording URLs expire in 10 minutes when PII-restricted storage is on.** Download immediately or switch storage mode for that agent.
- **Data storage modes (per-agent):** `everything` (default), `everything_except_pii` (scrubs PII), `basic_attributes_only` (metadata only).
- **Data retention is configurable 1–730 days.** Unset = retain forever.
- **Two-party-consent recording states (US): CA, FL, IL, MD, MA, and others.** Disclose at call start. Agent Handbook "AI Disclosure When Asked" is insufficient for two-party consent — use an explicit opening disclosure.
- **No native do-not-call list integration.** Filter your CSV or API queue before initiating outbound.

### Events & lifecycle

- **Calls that never connect skip `call_started` but still fire `call_ended` and `call_analyzed`.** Don't rely on `call_started` as a universal "call created" signal.
- **Post-call analysis doesn't populate for calls with no conversation.** Won't show custom fields if the caller hung up immediately.

### Max limits

- **Call duration:** 1h default, 2h max.
- **Prompt length:** 32,768 characters.
- **Concurrent calls:** 20 on PAYG default (burst pricing above).
- **Custom function response:** 15,000 characters.

---

## 5. Testing progression

Always climb this ladder — don't skip steps.

| Step | Tool | What it catches |
|---|---|---|
| 1. **LLM Playground** | Browser text chat | Logic bugs, tool-call behaviour, dynamic variable rendering. No audio. |
| 2. **Simulation Testing** | Automated personas | Regressions, flow coverage, success-criteria violations. Run batch tests after any prompt change. |
| 3. **Web Test Call** | "Test" button on agent page | Full audio stack, real WebRTC call, interruption behaviour, voice quality. |
| 4. **Phone Test Call** | Bound phone number | Telephony layer, SIP behaviour, real-world audio, DTMF. |
| 5. **Production with AI QA** | AI QA dashboard | Aggregate performance, cohort-level issues, drift. |

Don't ship to a client without running all 5. Simulation Testing is the one most people skip — that's where regressions hide.

---

## 6. Key doc URLs

Use when Claude needs to fetch current documentation during a workflow:

- `https://docs.retellai.com/llms.txt` — full doc index
- `https://docs.retellai.com/general/introduction` — platform overview
- `https://docs.retellai.com/get-started/quick-start` — 5-minute onboarding
- `https://docs.retellai.com/get-started/mcp-server` — MCP server setup
- `https://docs.retellai.com/build/prompt-engineering-guide` — Retell's prompt guidance
- `https://docs.retellai.com/build/agent-handbook` — personality/accuracy presets
- `https://docs.retellai.com/build/knowledge-base` — RAG setup
- `https://docs.retellai.com/build/conversation-flow/overview` — graph agents
- `https://docs.retellai.com/build/single-multi-prompt/transfer-call` — transfer patterns
- `https://docs.retellai.com/build/book-calendar` — Cal.com booking
- `https://docs.retellai.com/build/handle-voicemail` — voicemail detection
- `https://docs.retellai.com/deploy/custom-telephony` — SIP trunking, Twilio import
- `https://docs.retellai.com/deploy/outbound-call` — outbound API
- `https://docs.retellai.com/deploy/inbound-call` — inbound routing, inbound webhook
- `https://docs.retellai.com/deploy/make-batch-call` — batch campaigns
- `https://docs.retellai.com/features/post-call-analysis` — custom analysis fields
- `https://docs.retellai.com/features/webhook` — event types, signing
- `https://docs.retellai.com/accounts/kyc-verification` — KYC requirements
- `https://docs.retellai.com/accounts/privacy-disable` — data storage modes
- `https://www.retellai.com/pricing` — live rate card

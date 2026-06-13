# Retell AI Workflows

Step-by-step browser-driven workflows for common operations. Load a specific workflow when executing it — don't preload the whole file.

All workflows assume claude-in-chrome is available. Every step ends with a screenshot-verify pattern: take screenshot, confirm expected state, report discrepancies.

---

## §1. First-time onboarding (account → first agent → MCP setup)

Use when: User has never used Retell AI before.

### Pre-flight
- Ask which workspace this is for (user's own business name, or "scratch" for learning). This becomes the Retell workspace name.
- Ask which email to register under. **For client work later, each client gets its own workspace — this email choice matters for organization.**

### Steps

1. **Navigate to signup.** Open `https://dashboard.retellai.com` in a new tab. If redirected to login, click "Sign up".
2. **Create account.** Use email + password or Google SSO. Screenshot the confirmation.
3. **Name the workspace.** Use the name from pre-flight (e.g., "Lane Consultancy", "Thames Boilers"). This appears top-left in the dashboard.
4. **Submit KYC immediately.** Navigate to Billing → KYC Verification. Fill out the form. This unblocks outbound calling later; without it, outbound is blocked. Screenshot the submission confirmation.
5. **Navigate to Agents.** Click "Create an agent". Pick "Single Prompt" (simplest for first-time).
6. **Name the agent.** "Test agent - [date]".
7. **Pick a voice.** Platform voices → pick a warm female or male voice (e.g., "Maya" or "Adrian") — these are telecom-optimized.
8. **Paste a minimal prompt** (just for testing the setup works):
   ```
   ## Identity
   You are a friendly test assistant.

   ## Task
   Greet the caller, ask how they are, and wish them a good day. When they say goodbye, call end_call.
   ```
9. **Attach End Call tool.** Tools → Add → End Call.
10. **Save.** Screenshot the saved state.
11. **Click "Test" (Web Test Call).** Verify audio works, the agent speaks, interruptions work. Screenshot the test confirmation.
12. **Generate an API key.** Navigate to API Keys → "Create Key". Name it `skill-mcp-<workspace>`. Copy the key.
13. **Install MCP for this workspace.** Run in terminal:
    ```bash
    claude mcp add --transport http retell-<workspace-slug> https://retell.stlmcp.com \
      --header "Authorization: Bearer <API_KEY>"
    ```
    Replace `<workspace-slug>` with a short slug (e.g., `lane`, `thames`). Replace `<API_KEY>` with the key from step 12.
14. **Verify MCP.** In Claude Code, run `/mcp` and confirm `retell-<workspace-slug>` appears in the list.
15. **Done.** User is ready to build real agents.

### Troubleshooting

- **Signup hangs on email verification.** Retell sends a verification email — check spam. If no email after 2 min, resend.
- **KYC form fields missing.** Sometimes the form requires scrolling — check the full page before assuming something's broken.
- **Web Test Call fails with "No audio".** Check browser mic permissions. Also check `read_console_messages` for WebRTC errors.
- **MCP install succeeds but `/mcp` doesn't list it.** Restart Claude Code. MCP configs are loaded at session start.

---

## §2. Build a new agent (Single Prompt)

Use when: User knows what they want the agent to do and it's simple enough for Single Prompt.

### Pre-flight
- Confirm the workspace in the dashboard top-left before starting.
- Confirm which template applies (`templates/inbound-lead-qualifier.md`, `templates/outbound-offer-followup.md`, etc.) or that this is a one-off.

### Steps

1. **Navigate to Agents → Create an agent → Single Prompt.**
2. **Name the agent.** Use a clear name: `<purpose>-<inbound|outbound>-v1` (e.g., `lead-qualifier-inbound-v1`).
3. **Paste the prompt** from the template, replacing all `{{placeholders}}` with real values. Verify no `{{}}` remain unresolved.
4. **Configure voice & speech.**
   - Voice: Platform voice (default). Only switch to ElevenLabs if quality is specifically required (and accept the +$0.025/min cost).
   - `voice_speed`: 1.0 (adjust ±0.05 for slightly faster/slower).
   - Boosted keywords: add the business name, owner's name, any technical terms (e.g., "boiler", "Worcester").
   - Pronunciation guides: add any brand/proper noun that TTS mispronounces in testing.
5. **Configure interaction.**
   - `interruption_sensitivity`: 0.7 for noisy environments, 1.0 for quiet office calls.
   - `enable_backchannel`: on for warm/CS agents, off for transactional.
   - `end_call_after_silence_ms`: 30000 (default).
   - `max_call_duration_ms`: 600000 (10 min) for qualification agents, 1800000 (30 min) for intake, 3600000 (1h default) for general.
6. **Configure opening.**
   - Agent-first with **fixed** begin message (not LLM-generated) for outbound — avoids 10s billing minimum.
   - For inbound, user-first if voicemail detection matters; otherwise agent-first.
7. **Add tools.**
   - **Always add End Call.** Without it, the agent can't hang up.
   - Add any transfer, booking, or custom tools the template specifies.
8. **Configure LLM.** GPT 4.1, temperature per template (0.2 for data capture, 0.5 for sales, 0.3 for receptionist).
9. **Configure Agent Handbook presets.** Turn OFF presets not needed for this agent type — they each cost tokens. Keep on: "AI Disclosure When Asked" (always), "Scope Boundaries" (for narrow agents).
10. **Configure post-call analysis.** Add the custom fields specified in the template (e.g., `qualified`, `business_type`, `callback_requested`).
11. **Save.** Screenshot.
12. **Test in LLM Playground** — catch logic bugs before audio testing.
13. **Test via Web Test Call** — check audio, interruptions, voice quality.
14. **If prompt edits needed, iterate steps 3–13.**

---

## §3. Buy and bind a phone number (Retell-managed)

Use when: User wants a phone number purchased through Retell (fastest path to a working number).

### Pre-flight
- Confirm the workspace.
- **Verify at least one agent exists** in the workspace. The "bind to agent" step needs an agent to select — if there's none, you'll hit an empty dropdown and get stuck. Build the agent first (§2), then come back to this workflow.
- Confirm KYC is approved (required for outbound; inbound-only works without — skip the KYC wait if you're only doing inbound for now).
- Ask: what area code should the number have? (Local area code for the business's service area.)
- Ask: inbound, outbound, or both?
- **If the user has an existing number with a mismatched area code** (e.g., a California-area number for a Texas business): flag that this affects caller trust. Options: (a) buy a new local number and set call forwarding from the old one, (b) port the old number to Retell/Twilio and display a local number via CNAM, (c) accept the mismatch if the business is regional/national. Don't ignore this — it matters for inbound conversion.

### Steps

1. **Navigate to Phone Numbers → Buy New Number.**
2. **Enter area code filter.** e.g., "415" for San Francisco, "020" for London (note: Retell UK availability varies — check before promising).
3. **Pick an available number.** Review the number. Confirm with the user before purchasing.
4. **Purchase.** $2/month charged. Screenshot the success page.
5. **Bind to agent(s).**
   - Inbound agent: select from dropdown.
   - Outbound agent: select from dropdown (may be the same agent).
6. **Save binding.** Screenshot.
7. **If inbound:** call the number from a real phone to verify the agent picks up. Check Call History for the test call.
8. **If outbound:** from Call History or Make Call UI, initiate an outbound call to the user's phone. Verify the agent speaks.

---

## §4. Import a Twilio number (SIP trunk)

Use when: User already has a Twilio number they want to reuse, or needs features not available on Retell-native numbers.

### Pre-flight
- User needs Twilio credentials (account SID, auth token).
- User needs to decide IP allowlist (`18.98.16.120/30`) or username/password auth for the SIP trunk.
- **KYC caveat for outbound via imported numbers:** The Retell docs do NOT explicitly state whether KYC is required when outbound is initiated via an imported Twilio trunk. Retell still originates the call through its platform, so assume KYC applies. Submit KYC during signup regardless of whether you're using Retell-native or imported numbers. Test with a single low-volume outbound before any campaign; if Retell returns a KYC error, the signal is clear.

### Steps

**Part A: Twilio side**

1. **Log into Twilio Console** (`console.twilio.com`). Screenshot.
2. **Navigate to Elastic SIP Trunking → Trunks → Create new Trunk.**
3. **Friendly name:** something descriptive (e.g., `retell-<workspace>`). This is a display label only — **do not use it as the username later.**
4. **Termination → Termination URI:** This is a subdomain Twilio auto-generates for your trunk. Pick a unique prefix (e.g., `retell-<workspace>.pstn.twilio.com`). Twilio will confirm it's available and save. Write down the full URI — Retell needs it.
5. **Origination → Origination URI:** Add a new Origination URI with value `sip:sip.retellai.com`. Priority/weight can stay default. Save.
6. **Authentication (pick ONE method):**
   - **Option A — IP ACL (simplest):** Authentication → IP Access Control Lists → Create new → add `18.98.16.120/30`. Attach to the trunk. Done.
   - **Option B — Credential List (needed for non-IP-allowlist scenarios):**
     - 6a. In Twilio: Elastic SIP Trunking → Authentication → **Credential Lists** → Create new List. Name it (e.g., `retell-creds`).
     - 6b. Add a credential: pick a **username** (NOT the trunk's friendly name — make it something like `retell_<workspace>`) and a strong password. Save both in a password manager.
     - 6c. Back on the trunk: Termination → Authentication → attach the Credential List you just created.
     - 6d. Write down the username AND password — Retell needs both.
7. **Save the trunk.** Screenshot.
8. **Move numbers to the trunk.** Phone Numbers → Active Numbers → select number → Voice → set "A call comes in" to "SIP Trunk" → pick the trunk. Save.

**Part B: Retell side**

9. **Dashboard → Phone Numbers → Import Number.**
10. **Enter Termination SIP URI** (from step 4).
11. **Enter credentials** (username/password from step 6, if used).
12. **Save.** Screenshot.
13. **Bind to agent.** Same as §3 step 5.
14. **Test inbound and outbound.** Same as §3 steps 7–8.

### Troubleshooting
- **"Authentication failed" on Retell import.** The username is NOT the friendly name. It's the username from the Credential List.
- **Calls connect but no audio.** Codec mismatch. Retell supports PCMU, PCMA, G.722. Check Twilio trunk settings.
- **Outbound works but inbound doesn't.** Twilio Origination URI points back to Retell (`sip:sip.retellai.com`) — verify this.

---

## §5. Set up webhooks & post-call analysis

Use when: User needs to receive call events on their server (CRM integration, lead routing, automation).

### Pre-flight
- User needs a publicly reachable HTTPS endpoint.
- User needs to handle `x-retell-signature` verification.
- Decide: account-level webhook (fires for all agents) or agent-level (overrides for one agent).

### Steps

1. **Decide scope.** Account-level: Dashboard → Webhooks. Agent-level: Agent → Settings → Webhook URL.
2. **Paste the endpoint URL.** Must be HTTPS. Screenshot.
3. **Save the signing secret.** Retell shows the API key used for signature verification — use this in your webhook handler.
4. **Allowlist Retell's IP** (`100.20.5.228`) on your server/firewall.
5. **Pick event types to listen for.** Default events:
   - `call_started` — call picked up (missing for never-connected calls).
   - `call_ended` — call hung up. **Always fires.**
   - `call_analyzed` — post-call analysis complete (fires a few seconds after `call_ended`). **Always fires.**
   - `transcript_updated` — during-call, high-volume; use sparingly.
   - `transfer_started/bridged/cancelled/ended` — transfer lifecycle.
6. **Configure post-call analysis custom fields.** Agent → Post-Call Analysis → Add Field.
   - Boolean (e.g., `qualified`, `callback_requested`)
   - Text (e.g., `detailed_summary`, `next_action`)
   - Number (e.g., `quoted_price`)
   - Selector/Enum (e.g., `call_outcome` = `booked` | `not_qualified` | `callback` | `no_answer`)
   - Each field needs a description and format example.
7. **Test end-to-end.** Place a test call, verify your endpoint received `call_ended` and `call_analyzed` with the expected fields.
8. **Verify signature.** Confirm your webhook handler validates `x-retell-signature` — skipping this lets anyone forge events to your endpoint.

### Troubleshooting
- **Events not arriving.** Check firewall allows `100.20.5.228`. Check HTTPS cert is valid. Check webhook timeout (your endpoint must respond 2xx within 10s).
- **Signature validation fails.** Check you're using the correct API key (account-level vs agent-level). The signing secret differs if you set an agent-level webhook URL.
- **Custom fields empty.** Calls that never connect or have no conversation don't populate custom fields.

---

## §6. Set up batch calling (outbound campaign)

Use when: User wants to call a list of contacts (e.g., reactivation campaign, bulk outreach).

### Pre-flight
- KYC must be approved.
- Outbound agent must be built and tested.
- Phone number bound to the agent.
- CSV prepared with at minimum a `phone number` column (E.164 format) and any per-contact dynamic variables (e.g., `first_name`, `business_name`).
- **Confirm opt-out list has been applied to the CSV before upload.** Retell has no native DNC integration.

### Steps

1. **Navigate to Batch Calls → Create Batch Call.**
2. **Name the batch.** Descriptive: `<campaign>-<date>` (e.g., `reactivation-2026-04-22`).
3. **Pick From Number.** Must be bound to an agent.
4. **Upload CSV.** Verify Retell recognises the `phone number` column and any dynamic variable columns. Screenshot the preview.
5. **Verify dynamic variables resolve in the agent prompt.** If the prompt says `{{first_name}}`, the CSV must have a `first_name` column.
6. **Choose send time.** Send Now or Schedule. **Respect local call windows** — don't call before 8am or after 9pm in the recipient's timezone.
7. **Submit batch.** Status: Draft → Planned → Ongoing.
8. **Monitor progress.** Metrics: Sent / Picked Up / Successful. Drill into individual calls for transcripts.
9. **Post-batch review.** Export results. Review post-call analysis fields to feed back into CRM.

### Troubleshooting
- **"Dynamic variable not resolved" errors.** CSV column name must exactly match the `{{variable}}` name in the prompt.
- **Calls queued but not sent.** Check CPS limit (default 1/sec). Raise via telephony provider (Twilio up to 5, Telnyx up to 16).
- **High no-answer rate.** Review time of day vs. recipient timezone. Review caller-ID — is it showing the expected number?
- **Calls cut off immediately.** Voicemail detection might be misfiring. Check agent voicemail settings.

---

## §7. Debug a failing or underperforming agent

Use when: User says "the agent isn't working right" — ambiguous complaints, regression after a change, or latency issues.

### Triage questions (ask user first)

- What's wrong specifically? (Hangs up early / won't hang up / wrong answers / sounds robotic / slow responses / other)
- When did it start? (After a prompt change / always / intermittent)
- Which agent and workspace?

### Diagnostic steps

1. **Reproduce in LLM Playground first.** Cheapest signal. If it fails here, it's a prompt/logic bug, not audio.
2. **Check Call History for the recent failing calls.**
   - Open the transcript. Read the full exchange.
   - Check tool calls — was End Call triggered? Was the right tool invoked?
   - Check latency breakdown (ASR / LLM / TTS). If LLM latency > 3s, Fast Tier might be warranted.
   - Listen to the recording if audio-related (10-min URL expiry — download if needed).
3. **Check console in browser** with `read_console_messages` during a test call.
4. **Common fixes:**
   - Agent doesn't hang up → End Call tool missing or no explicit trigger in prompt.
   - Agent skips questions → Prompt too long or too many instructions per step. Break into numbered steps or move to Multi-Prompt.
   - Agent interrupted constantly → Lower `interruption_sensitivity` to 0.7.
   - Sounds robotic → Enable backchannel, add natural filler words preset (costs tokens), reduce overly formal Style Guardrails.
   - High latency → Try Fast Tier (1.5× LLM cost). Check for slow custom function tools.
   - Mispronounces brand → Add to boosted keywords AND pronunciation guides.
   - Says "slash" for "/" or reads dates robotically → Speech normalization is off.
5. **Iterate: change one thing at a time, re-run LLM Playground + Web Test Call.**
6. **After fix: run Simulation Testing** with 3–5 personas to catch regressions before deploying to production traffic.

---

## §8. MCP setup (deferred from onboarding)

Use when: User didn't set up MCP during onboarding and wants to now, or is configuring MCP for an additional workspace.

### Steps

1. **Get API key.** Dashboard → API Keys → "Create Key" (if none exists). Copy the key.
2. **Pick a name for this MCP entry.** Convention: `retell-<workspace-slug>` (e.g., `retell-lane`, `retell-thames`, `retell-client-acme`). This lets you distinguish multiple workspaces.
3. **Install via Claude Code CLI:**
   ```bash
   claude mcp add --transport http retell-<workspace-slug> https://retell.stlmcp.com \
     --header "Authorization: Bearer <API_KEY>"
   ```
4. **Verify.** Run `/mcp` in Claude Code. Confirm the entry appears.
5. **If Claude Desktop instead**, edit the config file directly:
   ```json
   {
     "mcpServers": {
       "retell-<workspace-slug>": {
         "url": "https://retell.stlmcp.com",
         "headers": {
           "Authorization": "Bearer <API_KEY>"
         }
       }
     }
   }
   ```
6. **Test the MCP.** Ask Claude to list agents or phone numbers via the MCP — confirms the key and connection work.

### When to use MCP vs. browser

| Task | Use |
|---|---|
| Create/edit agent (first time, or heavy prompt work) | Browser (visual editor, live testing) |
| Create 10 similar agents for 10 clients | MCP (scripted, repeatable) |
| LLM Playground / Web Test Call | Browser (MCP doesn't support these) |
| Conversation Flow graph editing | Browser (visual editor only) |
| List / filter / export call history | Either (MCP is faster for bulk) |
| Listen to a recording | Browser |
| Update webhook URL for 5 agents | MCP (scripted) |
| Debug a single call | Browser (transcript + audio + latency) |

**Rule:** Browser for visual, exploratory, or single-item work. MCP for bulk, programmatic, or repeatable operations.

---

## §9. Create a new workspace (for client isolation)

Use when: User is onboarding a new client and wants workspace-level isolation.

### Steps

1. **Open Retell dashboard.** Click the workspace selector (top-left).
2. **Click "Create Workspace"** or equivalent. (Retell's UI may label this "Create Organization" — verify in the dashboard.)
3. **Name it for the client.** e.g., `acme-plumbing`. Include a client code if you manage many.
4. **Configure billing.** Each workspace has its own billing. Decide: bill to you (you pass through) or bill client directly. Set up accordingly.
5. **Generate an API key for this workspace.** API Keys → Create. Copy.
6. **Install MCP for this workspace.** Follow §8 steps 2–4 with a new workspace-slug.
7. **Document the setup.** Note the workspace name, API key location (password manager), and MCP entry in your client tracker.
8. **Build first agent** using §2 workflow, referencing appropriate template.

### Client handover

If the client eventually takes ownership of the workspace:
- Transfer ownership via Workspace Settings → Transfer Ownership (or similar).
- Client gets their own access. You can be removed or stay as collaborator.
- Your MCP config still works until they rotate the API key.

---

## §10. Cal.com integration (booking tool setup)

Use when: Any agent needs to book or check calendar availability in-call. Required before using templates like `inbound-lead-qualifier` (booking path) or `appointment-booker`.

### Pre-flight
- User needs a Cal.com account (free tier works for basic bookings).
- User needs to know what kind of appointment to offer (duration, hosts, location/video).
- Retell agent must exist in the workspace.

### Part A: Cal.com side

1. **Log into Cal.com** at `app.cal.com`. Sign up if needed (free tier is fine for <100 bookings/month).
2. **Create an event type.** Event Types → New Event Type.
   - **Title:** e.g., "PipePro Consultation" — this is what the booking page shows.
   - **URL:** `cal.com/<username>/<slug>` — pick a clean slug.
   - **Duration:** 15 / 30 / 60 min depending on the use case.
   - **Location:** Phone call (Cal.com asks for the invitee's number) OR Google Meet / Zoom if video.
   - Set buffer times, max bookings per day, minimum notice if needed.
   - Save.
3. **Grab the Event Type ID.**
   - Option A (easiest): In the Event Type settings URL, look at the URL path. It'll be like `app.cal.com/event-types/2345678` — the number `2345678` is the ID.
   - Option B (via API): `curl -H "Authorization: Bearer $CAL_API_KEY" https://api.cal.com/v2/event-types` — find the event type in the response.
   - Write it down. Retell needs this number.
4. **Generate a Cal.com API key.**
   - Cal.com Settings → Developer → API Keys → Create New.
   - Name it (e.g., "retell-pipepro-production").
   - Set expiration (or "never" for convenience — but rotate annually).
   - Copy the key. Cal.com won't show it again.
5. **Set your availability.** Availability → Create/edit schedule. Ensure there are bookable slots in the windows you promise in the agent prompt. Agent with "I can book you in the next 3 business days" needs actual slots in those days.

### Part B: Retell side

6. **Navigate to the agent** that needs booking (or the Tools section for a reusable tool).
7. **Add the Book on Calendar tool.**
   - Agent → Tools → Add Tool → "Book on Calendar (Cal.com)".
   - **Name:** `book_appointment` (lowercase snake_case — must match what the prompt references).
   - **Description:** "Books a 15-minute consultation on the owner's Cal.com calendar. Call this once the caller confirms a time slot."
   - **Cal.com API Key:** paste from step 4.
   - **Event Type ID:** paste from step 3.
   - Save.
8. **Add the Check Availability tool.**
   - Agent → Tools → Add Tool → "Check Calendar Availability".
   - **Name:** `check_availability`.
   - **Description:** "Checks open slots on the owner's Cal.com calendar over the next few days. Call this before offering specific times to the caller."
   - Same API key + Event Type ID as step 7.
   - Save.
9. **Verify the tool is attached.** Agent → Tools list should show both `book_appointment` and `check_availability`.
10. **Update the prompt to reference these tools by name.** In the Task section:
    - "Use `check_availability` to find open slots."
    - "Use `book_appointment` to confirm the booking."
    - **Exact casing matters.**

### Part C: Testing

11. **Test in LLM Playground.** Walk through a booking conversation. In the Playground, tool calls are visible — confirm `check_availability` fires at the right moment and returns slots.
12. **Test via Web Test Call.** Actually book a test slot.
13. **Verify in Cal.com.** Open Cal.com → Bookings → confirm the test booking appears with the right name, time, and contact info.
14. **Verify confirmation email/text.** Cal.com sends these by default — check your inbox/phone.
15. **Delete test bookings** once verified so they don't block real slots.

### Troubleshooting

- **"401 Unauthorized" when agent calls tool:** API key wrong or revoked. Regenerate in Cal.com, update in Retell agent tool config.
- **Tool fires but no availability returned:** Your Cal.com availability schedule might not cover the dates being queried. Check Availability → schedule covers the window.
- **Event Type ID doesn't work:** Check you copied the numeric ID, not the event-type slug. ID is a number like `2345678`, not a string like `pipepro-consult`.
- **Booking succeeds but wrong timezone:** Cal.com booking timezone defaults to the event owner's timezone. If callers are in different timezones, make sure Cal.com's timezone detection is enabled, or pass timezone as a parameter.
- **Agent says "booked" but nothing in Cal.com:** Check the tool's Spoke-After setting — the agent may have spoken the confirmation before the tool actually completed. Also check that the booking payload includes required fields (name, email, start time).
- **Double-booking / overlap:** Cal.com has "prevent overlapping bookings" on by default. If callers report double-booking, verify this is on.

### Cal.com + Retell: cost & scale notes

- Cal.com free tier: unlimited meetings, some features gated (team scheduling, multiple event types need paid).
- API rate limits: Cal.com's API is generous for <10 calls/minute. If you're batch-calling 100 contacts and each may check availability + book, watch for rate limit errors at scale.
- **For pre-scheduled batch calls:** consider querying availability ONCE before the batch starts and passing slot options as dynamic variables. Reduces API load and avoids mid-call latency.

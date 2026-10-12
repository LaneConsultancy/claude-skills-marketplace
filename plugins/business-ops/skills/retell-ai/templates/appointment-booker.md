# Template: Appointment Booker (Conversation Flow)

**Use case:** Inbound or outbound agent whose primary job is booking time on a calendar. Handles availability lookup, slot offering, confirmation, and fallback when no slots work. Uses Cal.com as the booking backend.

**Agent type:** Conversation Flow (graph-based — the booking logic branches based on availability lookup results).

**Why Conversation Flow?** Appointment booking has inherent branching: availability query → offer slots → user picks or declines → re-query with different parameters → confirm → book. A Single Prompt can *try* to do this, but it drifts with 3+ slot offers. A Flow with explicit nodes is more reliable.

**Typical duration:** 2–4 minutes. Cost at default config: ~$0.26–$0.52 per call. **Watch Flex Mode token inflation** — if you turn Flex on, prompts can exceed 3,500 tokens.

---

## How to customize

| Placeholder | What to fill in |
|---|---|
| `{{agent_name}}` | Persona name |
| `{{business_name}}` | Business name |
| `{{service_being_booked}}` | What kind of appointment (e.g., "consultation", "estimate", "callback") |
| `{{duration_minutes}}` | Appointment duration (e.g., 15, 30, 60) |
| `{{cal_api_key}}` | Cal.com API key (store as secret in Retell) |
| `{{cal_event_type_id}}` | Numeric event type ID from Cal.com event URL |
| `{{business_hours_window}}` | e.g., "weekdays 9am to 5pm local" |
| `{{earliest_booking}}` | e.g., "next business day" or "same day if before 2pm" |
| `{{latest_booking}}` | e.g., "2 weeks out" |
| `{{confirmation_channel}}` | "text and email" (Cal.com sends these automatically) |

---

## Flow structure

Six core nodes:

1. **Greeting** (Conversation) — "Hi, ready to book your {{service_being_booked}}?"
2. **Collect caller details** (Conversation) — name, email, phone, postcode if needed.
3. **Check availability** (Function) — calls Cal.com Check Availability.
4. **Offer slots** (Subagent) — presents 2–3 options, handles decline/pick.
5. **Book** (Function) — calls Cal.com Book.
6. **Confirm & Close** (Conversation) — confirms booking, handles questions, calls End.

Plus branches:
- **No availability in window** — ask for new timeframe, loop back to Check.
- **Caller undecided** — offer to send booking link, capture details for callback.
- **Booking failure** — graceful fallback: capture preference manually, promise owner follow-up.

---

## Global settings (graph level)

```
## Identity
You are {{agent_name}}, the booking assistant for {{business_name}}. Your job is to book a {{service_being_booked}}.

## Style
- Warm, efficient. You're here to book them, not chat.
- Keep each turn tight. 1 question at a time.
- Read dates and times as spoken: "Tuesday the fifteenth at two PM" not "Tuesday, 15th at 2:00".

## Response Guidelines
- If caller unsure about timing: offer 2–3 concrete options from availability.
- If no options work: ask "What kind of timeframe works for you?" and re-query.
- If caller gets confused: slow down, re-confirm the target date/time.

## Global Guardrails
- Never promise a time not confirmed by the Cal.com availability tool.
- Never quote pricing or service details beyond basic facts — those are for the actual appointment.
- Always paraphrase spelling for name and email before booking.
```

---

## Node 1 — Greeting

**Type:** Conversation node

**Prompt:**
```
Say: "Hi, this is {{agent_name}} from {{business_name}}. I'm here to help you book a {{service_being_booked}}. Is that what you were after?"

Listen for:
- Yes → transition to `collect_details`
- Wants info/not yet → transition to `deflect` (offer to send info instead)
- Wrong number / confused → apologise, call end_call
```

**Edges:**
- → `collect_details` if confirmed
- → `deflect` if user wants info first
- → `end` if wrong number

---

## Node 2 — Collect Caller Details

**Type:** Conversation node

**Prompt:**
```
Capture in natural conversation:
1. "Who am I booking this for? Can I grab your full name?" — store as `customer_name`
2. "And what's the best email for the confirmation?" — store as `customer_email`. Paraphrase back letter-by-letter.
3. "Best phone number?" — store as `customer_phone`. Paraphrase back.
4. "And roughly, where are you based — just a postcode or town is fine." — store as `customer_location` (only if {{service_being_booked}} requires location).

Do NOT ask all four in one turn. One at a time.

When all required fields collected → transition to `check_availability`.
```

**Edges:**
- → `check_availability` when all required fields set

---

## Node 3 — Check Availability

**Type:** Function node (deterministic, not a conversation)

**Tool:** `check_availability` (Cal.com)

**Parameters:**
- `api_key`: `{{cal_api_key}}`
- `event_type_id`: `{{cal_event_type_id}}`
- `start_date`: `{{current_date}}` + 1 day (or immediate if same-day allowed)
- `end_date`: `{{current_date}}` + 14 days
- Optional: `timezone` from caller's location

**Speak-during-execution:** "Let me check what's available..."

**Result handling:**
- Store result in `available_slots` dynamic variable.
- Transition to `offer_slots`.
- If tool errors → transition to `booking_fallback`.

---

## Node 4 — Offer Slots

**Type:** Subagent node (conversation with tool)

**Prompt:**
```
Review the slots in {{available_slots}}. Pick 2–3 options that span different days and times (e.g., tomorrow morning, Wednesday afternoon, Friday morning — not three slots on the same day).

Say: "Great — I've got a few options. How about {{option_1}}, {{option_2}}, or {{option_3}} — any of those work?"

Listen for:
- Picks a specific option → store as `selected_slot`, transition to `book`.
- "Do you have anything else?" / "Those don't work" → ask for preferred timeframe, set `requery_window`, transition back to `check_availability` with new window.
- "Let me think" / "I'll call back" → offer to send booking link: "Want me to text you the booking link so you can pick a time?" Transition to `deflect` if yes.
- Says they need to check with someone → "No problem. Want me to send the booking link so you can book when you're ready?"

Do NOT offer more than 3 slots at a time — overwhelms the caller.
```

**Edges:**
- → `book` if slot selected
- → `check_availability` with new window if declined
- → `deflect` if caller wants to think
- → `end` if caller gives up

---

## Node 5 — Book

**Type:** Function node

**Tool:** `book_appointment` (Cal.com)

**Parameters:**
- `api_key`: `{{cal_api_key}}`
- `event_type_id`: `{{cal_event_type_id}}`
- `start`: `{{selected_slot}}`
- `name`: `{{customer_name}}`
- `email`: `{{customer_email}}`
- `phone`: `{{customer_phone}}`
- `notes`: auto-generated summary of call

**Speak-during-execution:** "Great, booking that now..."

**Result handling:**
- Success → store `booking_confirmation_id`, transition to `confirm_close`.
- Failure → transition to `booking_fallback`.

---

## Node 6 — Confirm & Close

**Type:** Conversation node

**Prompt:**
```
Say: "You're booked for {{selected_slot_readable}}. You'll get a confirmation by {{confirmation_channel}} with all the details."

Ask: "Anything else you want to mention before I let you go?"

Listen:
- No → say "Thanks, have a great day." Call end_call.
- Question you can answer from basic facts → answer briefly, then re-prompt "Anything else?".
- Question outside scope → "Good question — {{owner_name}} will cover that on the call. Thanks for booking."
- Wants to reschedule/cancel → "You can reschedule from the confirmation email — there's a link in there. Anything else?"

Call end_call when done.
```

**Edges:** Terminal.

---

## Deflect / Fallback Nodes

**`deflect` (Conversation):**
```
"No worries — what's the best way to send you the booking link, email or text?"
Capture preference, send link via Custom Function (hook to your email/SMS provider).
Say: "Sent. Call back any time if you need help. Have a good one."
Call end_call.
```

**`booking_fallback` (Conversation):**
```
Say: "Hmm — looks like my booking system is having a moment. Let me take your preference manually and {{owner_name}} will confirm by {{confirmation_channel}} within the hour."

Capture:
- Preferred day/time (free text)
- Backup option

Say: "Got it. {{owner_name}} will confirm shortly. Thanks."
Call end_call.
```

---

## Retell dashboard settings

| Setting | Value |
|---|---|
| Response Engine | Conversation Flow |
| Flex Mode | **OFF** (keeps token count low; only enable if flow gets too rigid) |
| LLM | GPT 4.1 |
| Temperature | 0.2 (booking needs determinism) |
| Voice | Platform voice |
| `voice_speed` | 1.0 |
| `interruption_sensitivity` | 0.7 |
| `enable_backchannel` | on |
| `end_call_after_silence_ms` | 30000 |
| `max_call_duration_ms` | 600000 (10 min) |
| Agent-first | Yes, fixed opening (from Greeting node) |
| Voicemail detection | on if outbound, off if inbound-only |
| Speech normalization | on (critical for reading times/dates) |
| Boosted keywords | business_name, service name, owner name, day names, time references |

---

## Tools to attach

| Tool | Node used in |
|---|---|
| End Call | Confirm & Close, Deflect, Fallback, errant branches |
| Check Calendar Availability (Cal.com) | Check Availability node |
| Book on Calendar (Cal.com) | Book node |
| Send SMS (or Custom HTTP to your SMS provider) | Deflect node |
| Custom HTTP (log_interaction) | Optional — log every outcome to your CRM |

---

## Post-call analysis fields

| Field | Type | Description |
|---|---|---|
| `outcome` | Selector | `booked` \| `deflected_to_link` \| `declined` \| `booking_failed` \| `no_availability_match` \| `voicemail` |
| `booking_id` | Text | Cal.com booking ID if booked. |
| `booked_time` | Text | ISO format. |
| `customer_name` | Text | |
| `customer_email` | Text | |
| `customer_phone` | Text | |
| `slots_offered` | Number | How many slot options were offered before success/failure. |
| `failure_reason` | Text | If not booked, why. |
| `summary` | Text | 1–2 sentence summary. |

---

## Testing checklist

- [ ] LLM Playground: walk through happy path (greet → details → availability → pick first slot → book).
- [ ] LLM Playground: walk through reject-all-slots → re-query path.
- [ ] LLM Playground: walk through "send me the link instead" path.
- [ ] Simulation Testing: 5+ personas including busy/indecisive/decisive/confused.
- [ ] Cal.com integration: confirm bookings actually appear in Cal.com after test calls.
- [ ] Web Test Call: full happy path.
- [ ] Check token count per call — should be well under 3,500 with Flex off.
- [ ] Verify booking_fallback actually works (temporarily revoke Cal.com API key to simulate failure).

---

## Conversation Flow-specific notes

- **Node naming matters.** Use descriptive IDs (`offer_slots`, `check_availability`) — easier to follow when debugging.
- **Function nodes are deterministic** — they don't use an LLM turn, just call the API and transition. Fast, cheap, reliable.
- **Subagent nodes DO use an LLM turn** — with the prompt you set. Use them for conversation + tool-call decisions.
- **Conversation nodes just speak.** They can ask for input but can't call tools. For "ask then act" patterns, chain Conversation → Subagent or Conversation → Function.
- **Edges with conditions** can reference dynamic variables set by upstream nodes.
- **Re-entering a node is allowed** (e.g., re-querying availability with a new window). Use this for loops.
- **Visual editing in the dashboard** — the Conversation Flow graph editor is the only way to build/edit these. MCP does not support visual flow editing. Use claude-in-chrome.

---

## When to switch to Multi-Prompt or Single Prompt instead

- Booking is simple (always "this week, any slot works") → Single Prompt is fine. Conversation Flow is overkill.
- Booking has clear linear phases but no branching → Multi-Prompt.
- **Use Conversation Flow when you have true branching logic** (availability-dependent, user-choice-dependent).

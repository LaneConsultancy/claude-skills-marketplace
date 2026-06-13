# Template: Outbound Offer Follow-up

**Use case:** Someone filled in a lead form, started checkout, or expressed interest but didn't convert. Agent calls them back within a pre-agreed window to answer questions and push toward the next step (booking a call, completing payment, restarting a trial, etc.).

**Agent type:** Single Prompt.

**Typical duration:** 1.5–3 minutes. Cost at default config: ~$0.20–$0.40 per call.

**⚠️ Regulatory reminders:**
- **KYC must be approved** on the workspace before outbound.
- **Scrub the call list against your opt-out list** before batch upload — Retell has no native DNC integration.
- **Call windows:** Don't call before 8am or after 9pm in the recipient's timezone (US TCPA). Many US states also restrict Sunday calling.
- **Two-party consent states:** CA, FL, IL, MD, MA, and others. Add an explicit consent line to the opening if recording and in a two-party state.

---

## How to customize

| Placeholder | What to fill in |
|---|---|
| `{{agent_name}}` | Agent's persona name (match voice gender) |
| `{{business_name}}` | Business calling from |
| `{{offer_name}}` | The offer they showed interest in |
| `{{offer_brief}}` | 1 sentence on what the offer is |
| `{{form_or_action}}` | What they did that triggered this call (filled form, abandoned checkout, etc.) |
| `{{callback_owner_name}}` | Who they'd be booked with if they want a call |
| `{{booking_mechanism}}` | "Cal.com tool" or "capture time for manual booking" |
| `{{dynamic_first_name}}` | `{{first_name}}` — pulled from the batch CSV or API call |
| `{{dynamic_context}}` | `{{context}}` or similar — whatever specific thing they submitted (e.g., their business name, the service they asked about) |
| `{{common_questions}}` | Top 3 questions people typically ask about the offer, with brief answers |
| `{{common_objections}}` | Top 3 objections people typically raise |

---

## Agent prompt (paste into Retell)

```
## Identity
You are {{agent_name}} from {{business_name}}. You're calling someone who {{form_or_action}} about our {{offer_name}} and you want to check in and answer any questions.

## Style Guardrails
- Keep responses to 1–2 sentences unless they ask for detail.
- Warm and respectful. You're calling them — they didn't call you. Be considerate of their time.
- Use contractions. No corporate-speak.
- Ask ONE question at a time.
- If you sense hesitation, don't push — offer to follow up another time.
- Never use high-pressure language ("limited time", "don't miss out", "act now").

## Response Guidelines
- If they say "who's this?" or seem confused: remind them they {{form_or_action}}. Don't assume they remember.
- Numbers and dates as spoken: "four nine seven dollars" not "$497".
- If you don't understand: "Sorry, could you repeat that?"
- Never make up information. If you don't know, offer to have {{callback_owner_name}} follow up.

## Task
Your job:
1. Greet, confirm it's them, confirm this is a good moment.
2. Remind them what they did and why you're calling.
3. Answer any questions they have.
4. Move toward the next step (booking a call with {{callback_owner_name}} or rescheduling).
5. If they're not interested, respect that and end the call.

### Steps

**Step 1 — Open.**
Say: "Hi, is this {{dynamic_first_name}}? This is {{agent_name}} from {{business_name}}. Is this a good moment to talk for a minute?"

If they say NO / bad time:
- "No problem. When would be a better time? I can call back then."
- Capture their preferred time, say "Got it, I'll call back {{preferred_time}}", then end call.

If they say YES:
- Proceed to Step 2.

**Step 2 — Remind them.**
Say: "I'm calling because you {{form_or_action}} about our {{offer_name}}. I wanted to check in — see if you had any questions, or if there's anything I can help with."

Pause. Let them respond.

**Step 3 — Answer questions / handle objections.**
If they have questions, answer from this list:

{{common_questions}}

If they raise objections, handle from this list:

{{common_objections}}

For anything outside these lists: "Good question. I'd rather have {{callback_owner_name}} answer that properly — can I book you a 15-minute call with them?"

**Step 4 — Push toward next step.**
After questions are addressed:
- "Is there anything holding you back from {{next_action}}?"

If they say "I need to think about it":
- "Totally fine. Want me to send you a reminder in a few days, or is there a time that'd work for a quick call with {{callback_owner_name}}?"

If they say "Yes, let's do it":
- If {{booking_mechanism}} is "Cal.com tool" → proceed to booking.
- Otherwise → "Great. What's the best time for {{callback_owner_name}} to reach you?" Capture and end call.

If they say "Not interested":
- "No problem — thanks for your time. Can I take you off the list so you don't hear from us again?" Capture confirmation, end call.

**Step 5 — Booking flow (if using Cal.com):**
- Use `check_availability` to find open slots over the next 2 business days.
- Offer 2 options: "I've got tomorrow at two PM or Thursday at ten AM — which works?"
- Use `book_appointment`.
- Confirm: "You're booked for {{time}}. You'll get a text confirmation."

## End Call Triggers
Call `end_call` when:
- You've handled the outcome (booked / callback scheduled / opted out).
- Caller says bye.
- Caller asks you to stop calling.

Always sign off politely: "Thanks for your time, {{dynamic_first_name}}. Have a good one."

## Voicemail Handling
If voicemail is detected:
- Leave this message exactly, then call end_call:
- "Hi {{dynamic_first_name}}, this is {{agent_name}} from {{business_name}}, following up on your interest in our {{offer_name}}. Give us a call back when you have a moment. Have a good day."
- Do NOT try to have a conversation with voicemail.

## AI Disclosure
If asked "are you a robot":
- "I'm an AI assistant for {{business_name}}. I can answer basic questions, and I can book you in with {{callback_owner_name}} if you want to chat to a human."

## Do-Not-Call Handling
If the caller says ANY of these (or similar):
- "Don't call me again"
- "Take me off your list"
- "Stop calling me"
- "Do not call"
Say: "I understand — I'll make sure you're not called again. Thanks." Then call end_call.
Set post-call analysis field `opt_out_requested` to `true`.

## Two-Party Consent Opening (if applicable)
Prepend to Step 1 if the caller is in a two-party consent state:
- "Hi, this is {{agent_name}} from {{business_name}}. This call may be recorded for quality. Is now a good moment?"
- If they decline recording: end call and log.
```

---

## Retell dashboard settings

| Setting | Value |
|---|---|
| Response Engine | Retell LLM — Single Prompt |
| LLM | GPT 4.1 |
| Temperature | 0.4 |
| Voice | Platform voice |
| `voice_speed` | 1.0 |
| `interruption_sensitivity` | 0.8 (outbound usually quieter environments) |
| `enable_backchannel` | on |
| `backchannel_frequency` | 0.5 |
| `end_call_after_silence_ms` | 20000 (outbound — shorter) |
| `max_call_duration_ms` | 480000 (8 min) |
| Agent-first/User-first | **Agent-first**, FIXED begin message (avoid 10s LLM minimum) |
| Begin message (fixed) | "Hi, is this {{first_name}}?" |
| Voicemail detection | **on** |
| Voicemail action | Leave message (from prompt) |
| Pause before speaking | 400ms |
| Speech normalization | on |

---

## Tools to attach

| Tool | Required | Notes |
|---|---|---|
| End Call | **Yes** | |
| Book on Calendar (Cal.com) | If booking in-call | |
| Check Calendar Availability | If booking in-call | |
| Custom HTTP (log_opt_out) | Recommended | Immediately push opt-out to your DNC list, not just post-call. Agent may continue to next entry before webhook fires. |

---

## Batch call CSV schema

```csv
phone number,first_name,context,email
+14155551234,Jane,requested website info on April 10,jane@example.com
+14155555678,Mike,abandoned $497 checkout on April 12,mike@example.com
```

Required: `phone number` (E.164).
Dynamic vars referenced in prompt: `first_name`, `context`.
Other columns: available as `{{column_name}}` if you reference them in prompt.

---

## Post-call analysis fields

| Field | Type | Description |
|---|---|---|
| `outcome` | Selector | `booked` \| `callback_scheduled` \| `not_interested` \| `opted_out` \| `voicemail` \| `no_answer` \| `unreachable` |
| `booked_time` | Text | ISO time if booked. |
| `callback_time` | Text | Preferred callback time if scheduled. |
| `opt_out_requested` | Boolean | Critical. Used to update DNC list. |
| `questions_asked` | Text | Free-text summary of caller questions. |
| `main_objection` | Text | Primary objection raised, if any. |
| `summary` | Text | 1–2 sentences. |

---

## Testing checklist

- [ ] LLM Playground: Run 5 personas (interested, not interested, wrong number, hostile, wants to opt out). Verify outcomes.
- [ ] Simulation Testing: Automated run with 10+ personas including voicemail scenarios.
- [ ] Web Test Call: Audio, interruptions, voicemail message delivery.
- [ ] Phone Test Call: Call your own phone. Let it ring out to voicemail — verify voicemail message is left correctly.
- [ ] Batch call test: Upload 5 rows (mix of real test numbers + voicemails). Verify dynamic variables resolve, opt-outs logged.
- [ ] Verify opt-out webhook fires immediately and updates DNC list.
- [ ] Verify call times are within legal windows for recipient timezones.

# Template: Voicemail Handler (shared pattern)

**Use case:** This is not a standalone agent — it's a **pattern to layer into any outbound agent**. Retell's voicemail detection fires when the callee's answering machine picks up. Without handling, agents try to "converse" with a voicemail and leave unusable messages.

**Applies to:** Any outbound agent (`outbound-offer-followup`, outbound reminders, outbound surveys, etc.). Not needed for inbound.

---

## How voicemail detection works in Retell

- Enable voicemail detection on the agent (Settings → Voicemail Detection → On).
- When a call connects, Retell's detection model runs in parallel with your agent.
- If voicemail is detected, Retell pauses your agent and triggers whichever voicemail behaviour you configured:
  - **Leave message:** agent reads a pre-defined message and hangs up.
  - **Hang up:** agent ends the call immediately.
- Detection is not perfect. It can misfire on slow human answers or long greetings (bilingual households, accents, etc.). Prompt defensively.

---

## How to customize

| Placeholder | What to fill in |
|---|---|
| `{{agent_name}}` | Agent's name (first name, spoken) |
| `{{business_name}}` | Calling from |
| `{{reason_for_call_brief}}` | 1 short phrase (e.g., "following up on the boiler quote", "your website enquiry") |
| `{{callback_number}}` | Number to ask callback on. E.164, but speak it in natural chunks |
| `{{callback_number_spoken}}` | Natural-speech form of callback number. e.g., "four one five, five five five, one two three four" |
| `{{callback_url_short}}` | Optional short URL to send via SMS after voicemail (e.g., "laneco.com/book") |

---

## Voicemail message (paste into Voicemail Detection → Leave Message field)

Keep it under 20 seconds. Longer messages get cut off or ignored.

```
Hi, this is {{agent_name}} from {{business_name}}, {{reason_for_call_brief}}. 
Give us a call back at {{callback_number_spoken}} when you have a moment, or I'll try again another day. 
Thanks, have a good one.
```

**Why it works:**
- Opens with business name + agent name (caller can decide relevance in 2 seconds)
- States reason upfront (don't bury the lede)
- Gives number explicitly, in spoken form (TTS reads this naturally)
- Offers a second contact path ("I'll try again") — reduces pressure
- Warm sign-off, not salesy

---

## Agent prompt additions

Add this section to any outbound agent's prompt, AFTER the main Task section and BEFORE End Call Triggers:

```
## Voicemail Handling

Retell will detect voicemail automatically. If voicemail is detected, Retell will leave the pre-configured message and end the call — you don't need to do anything.

However, sometimes voicemail detection fails and a real human picks up after a long silence, OR a human picks up but their greeting is long/quiet/in another language, making you think it's voicemail.

Defensive behaviour:
- If you hear a tone/beep followed by silence, assume voicemail-not-detected and leave the message manually:
  - Say: "Hi, this is {{agent_name}} from {{business_name}}, {{reason_for_call_brief}}. Give us a call back at {{callback_number_spoken}}. Thanks."
  - Call end_call.
- If you hear "hello" after an unusually long pause (3+ seconds): greet normally and proceed — it's probably a person.
- If the first response is a voice saying something like "please leave a message after the beep" or "this mailbox is not set up": it's voicemail that Retell missed. Leave the message manually, then call end_call.
- If you're genuinely unsure: ask once "Hello, is this a good time to talk?" then wait. If no response for 5 seconds → treat as voicemail, leave message, end call.
```

---

## Retell settings to enable voicemail handling

| Setting | Value |
|---|---|
| Voicemail detection | **ON** |
| Voicemail action | "Leave message" |
| Voicemail message | See template above |
| `interruption_sensitivity` | 0.8 on outbound (slightly higher helps the agent hold the floor while leaving the voicemail) |
| Pause before speaking | 400ms (gives the answering machine a moment to finish its greeting before you start talking) |

---

## Optional: SMS follow-up after voicemail

Voicemail hit rates for callbacks are low (5–15%). To recover, send an SMS right after the voicemail with a booking link or info.

**Implementation:** 
- On webhook `call_ended` with `disconnection_reason = voicemail_reached`, trigger SMS via your SMS provider.
- OR attach a Custom HTTP tool `send_voicemail_followup_sms` and call it from within the agent just before `end_call` when voicemail detected.

**SMS template:**
```
Hi from {{business_name}} — just left you a voicemail about {{reason_for_call_brief}}. Call us back at {{callback_number_spoken}} or book a time directly: {{callback_url_short}}. No rush.
```

---

## Testing voicemail handling

**This is the hardest part of any outbound agent to test properly.**

1. **LLM Playground** won't simulate voicemail (no audio layer). You can test the agent's fallback prompt logic by typing "please leave a message after the beep" or a tone description.
2. **Web Test Call** won't trigger voicemail detection (it's a browser WebRTC session).
3. **Phone Test Call** is the only real test:
   - Have Retell call your actual phone.
   - Let it ring through to voicemail.
   - Retrieve your voicemail later and verify the message came through correctly.
   - Expected: clear message, number pronounced correctly, under 20 seconds.
4. **Retry with human answer:** pick up on the 4th ring (after a delay — simulate slow pickup) and say "Hello" after a 3-second pause. Verify the agent recognises this as a human and proceeds normally.
5. **Retry with ambiguous greeting:** pick up and say "Hi this is Jane" very quietly. Verify the agent still recognises and proceeds.

**Common issues:**
- **Message cut off mid-sentence:** Voicemail message too long. Trim to <20 seconds.
- **Agent speaks over the callee's greeting:** `pause_before_speaking` is too short. Raise to 500–800ms.
- **Number mispronounced:** Use the `_spoken` form with commas and spaces, e.g., "four one five, five five five, one two three four". Add the number to Speech Normalization pronunciations if persistently wrong.
- **Voicemail detection misfires on slow humans:** Lower sensitivity in voicemail detection settings, or rely on the defensive prompt section above.
- **Agent leaves message but doesn't hang up:** Missing End Call tool, or missing explicit end-call trigger in prompt after voicemail.

---

## Post-call analysis fields for voicemail

Add to any outbound agent:

| Field | Type | Description |
|---|---|---|
| `voicemail_detected` | Boolean | True if voicemail was detected (by Retell or by the defensive prompt). |
| `voicemail_message_left` | Boolean | True if a message was actually delivered. |
| `voicemail_followup_sms_sent` | Boolean | True if SMS fired post-voicemail. |

---

## When NOT to leave a voicemail

- When calling lists where the caller hasn't opted in (high risk of TCPA complaint in the US).
- When calling someone for a second or third attempt in a short window — let them come to you.
- When local law restricts voicemail (some jurisdictions treat voicemail as a "call" for DNC purposes).

If in doubt: hang up on voicemail, log the attempt, try again in 2–3 days at a different time of day.

---

## Handling voicemail across a campaign

For a 500-contact batch:
- Expect 40–60% voicemail rate on cold outbound.
- Don't retry the same contact more than 3 times total.
- Space retries: Day 1 morning → Day 2 afternoon → Day 4 evening.
- After 3 voicemails: drop the contact or hand off to a human.
- Track voicemail-to-callback conversion separately — if it's under 5%, consider whether voicemails are worth leaving at all.

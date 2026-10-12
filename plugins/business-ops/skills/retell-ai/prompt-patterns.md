# Retell AI Prompt Patterns

How to structure voice-agent prompts using Retell's own framework + patterns for common behaviours. Load this when writing or reviewing an agent prompt.

**Reference:** `https://docs.retellai.com/build/prompt-engineering-guide`

---

## The Retell prompt structure

Retell recommends five sections, in this order:

### 1. Identity
Who is the agent? What business? What role?

```
## Identity
You are Sarah, a friendly appointment coordinator for {{business_name}}, a {{business_type}} serving {{service_area}}. You handle inbound calls from potential customers and help them book consultations.
```

Keep to 2–3 sentences. Don't over-specify personality — let the voice + style guardrails do that work.

### 2. Style Guardrails
How to speak. The voice and mannerisms.

```
## Style Guardrails
- Keep responses to 1–2 sentences unless the customer asks for detail.
- Use contractions ("I'll", "we're") — never formal English.
- Warm and direct. No filler phrases like "absolutely" or "great question".
- Never say you're an AI unless asked directly, then disclose honestly.
- Ask one question at a time. Let the customer answer before moving on.
- Paraphrase what the customer says back to confirm you heard correctly.
```

### 3. Response Guidelines
How to handle common speech patterns and edge cases.

```
## Response Guidelines
- Numbers and dates: speak them naturally. "Monday the fifteenth", not "Monday, January 15th". "Two hundred dollars", not "$200".
- Spellings: if the customer spells something, read it back letter by letter to confirm.
- If you don't understand: "Sorry, could you repeat that?" — not "I didn't catch that."
- If there's background noise: "I'm having trouble hearing you — are you somewhere quieter?"
- Never make up information you don't have. If you don't know, say so and offer to follow up.
```

### 4. Task Instructions
The actual job. Step-by-step what to do.

```
## Task
Your job is to qualify whether the caller is a fit for our {{offer}}, then book a 15-minute consultation if they are.

Steps:
1. Greet: "Hi, this is Sarah from {{business_name}}. Thanks for calling — how can I help?"
2. Find out what they're looking for. Listen for: {{qualification_signal_1}}, {{qualification_signal_2}}.
3. If they mention one of those signals, ask: "{{qualification_followup_question}}"
4. If qualified, say: "It sounds like we could help. Would you like to book a free 15-minute consultation with {{owner_name}} this week?"
5. If yes, use the `check_availability` tool to find open slots, then use `book_appointment` to confirm.
6. If they're not a fit, politely close: "Thanks for calling. Based on what you've described, we're probably not the right fit — but {{alternative_referral}} might be able to help."
7. When the conversation is complete, call `end_call` with a friendly sign-off.
```

**Critical:** List exact trigger phrases for tools. The LLM decides when to call a tool based on your prompt — vague guidance = missed or over-triggered tools.

### 5. Objection Handling
Common objections and how to respond.

```
## Objection Handling
- "I'm just browsing": "Totally fine — can I send you some info by text to look at later?"
- "How much does it cost?": "The consultation is free. Pricing depends on the scope — {{owner_name}} covers that in the call."
- "I need to think about it": "Of course. Would it help if I send you our details so you can call back when you're ready?"
- "Send me an email instead": "Happy to. What's the best email to use?" — then use `send_email` tool if available, or capture in post-call analysis.
- "Can you call me back later?": "Sure. What time works best?" — then capture callback time in post-call analysis.
```

---

## Core patterns

### Pattern: Agent hangs up reliably

**Problem:** Agents don't end calls by themselves. Calls run to max duration.

**Fix:**
1. Attach the End Call tool to the agent.
2. In the prompt, write explicit end-call triggers:

```
## End Call Triggers
Call `end_call` when:
- The customer says goodbye ("bye", "see you", "thanks, bye", "have a good one").
- You've completed the task (booking confirmed, information captured) AND the customer has no more questions.
- The customer is abusive or the call is clearly wasted time.

Always give a brief sign-off before calling end_call: "Thanks for your time, have a great day."
```

### Pattern: Voicemail handling (outbound)

**Problem:** Outbound calls that hit voicemail either hang up awkwardly or leave a weird message.

**Fix:**
1. Enable voicemail detection on the agent.
2. In the prompt, add:

```
## Voicemail Handling
If voicemail is detected:
- Leave this message, then call `end_call`:
- "Hi, this is {{agent_name}} calling from {{business_name}} about {{reason_for_call}}. Call us back at {{callback_number}} when you have a moment. Thanks."
- Do NOT try to have a conversation with voicemail.
```

### Pattern: Transfer to a human

**Problem:** Agent needs to transfer but doesn't know when.

**Fix:**
1. Attach the Transfer Call tool with the destination number (E.164).
2. In the prompt:

```
## Transfer Triggers
Call `transfer_call` when:
- The customer explicitly asks to speak to a human ("can I talk to a person", "real human please", "manager please").
- The customer has a complaint or complex issue you can't handle.
- The customer is visibly frustrated after 2+ failed attempts.

Before transferring:
- "Let me put you through to {{human_name}} — one moment."
- Then call transfer_call.
```

### Pattern: Data capture without losing flow

**Problem:** Collecting lots of data (name, email, address, phone) in one rigid sequence feels robotic.

**Fix:**
- Collect naturally through the conversation, not all-at-once.
- Paraphrase each one back before moving on.

```
## Data Capture
Collect these details during natural conversation, not in a rigid list:
- Full name (ask early: "Who am I speaking with?")
- Phone number (ask if they called from a different number, or if the number might be unreliable)
- Email (ask only if we need to send follow-up info)
- Postcode / zip (ask if we need to check service area)

Always paraphrase back to confirm spelling: "So that's J-O-H-N S-M-I-T-H, correct?"
```

### Pattern: Handling "Are you a robot?"

**Problem:** Customer asks if they're talking to an AI. Deny = damages trust. Over-disclose = kills the flow.

**Fix:**
```
## AI Disclosure
If the customer directly asks "are you a robot" or "am I talking to a real person":
- Disclose honestly: "I'm an AI assistant for {{business_name}} — but I can take care of most things, and I'll connect you with {{human_name}} if you need them."
- Do NOT volunteer this information unprompted. Only disclose when asked.
- After disclosure, continue naturally — don't over-explain.
```

### Pattern: Handling background noise or poor reception

**Problem:** Caller is in a noisy environment. Agent can't understand them. Loops into frustration.

**Fix:**
- Lower `interruption_sensitivity` to 0.7.
- In the prompt:

```
## Audio Quality
If you can't understand the customer clearly:
- First attempt: "Sorry, could you say that again?"
- Second attempt: "I'm having trouble hearing you — could you move somewhere quieter?"
- Third attempt: "The line isn't great. Let me take your number and call you back. What's the best number?" — then capture and end call gracefully.
```

### Pattern: Keeping prompts lean

Retell bills proportionally once your prompt exceeds 3,500 tokens. Watch out for:

- **Overly detailed Response Guidelines** — pick the 5–7 most important rules, drop the rest.
- **Long lists of example phrases** — the LLM generalises from 2–3 examples; more is waste.
- **Redundant repetition across sections** — if you've said "be warm" in Identity, you don't need it in Style Guardrails.
- **Agent Handbook presets** — each preset adds 30–910 tokens. Turn off what you don't need.

**Rule of thumb:** Aim for 800–1,500 words. Past 2,000 words, start cutting.

---

## Dynamic variables

Use `{{variable_name}}` syntax. Variables come from:

- **Per-call dynamic variables** — passed via API when registering a call or in the inbound call webhook response.
- **System variables** — `{{current_time}}`, `{{current_date}}`, `{{caller_number}}`, `{{callee_number}}`, etc.
- **Tool results** — any value extracted from a tool response.

**Critical:** All dynamic variables must be strings. Non-strings fail validation. Convert numbers/booleans before passing.

**Unset variables render literally as `{{variable_name}}`.** Always provide defaults or handle absence in the prompt:

```
Your name, if known, is {{customer_name}}. If the value looks like "{{customer_name}}" (unresolved), just ask for their name.
```

---

## Testing a prompt before shipping

The ladder:

1. **LLM Playground** — text chat. Catches logic bugs, tool-call triggering, dynamic variable rendering.
2. **Simulation Testing** — automated persona runs. Catches regressions after prompt edits. Define 3–5 personas (ideal fit, not-quite fit, hostile, confused, hurried) and run them after every prompt change.
3. **Web Test Call** — real audio. Catches interruption sensitivity, voice quality, speech normalization issues.
4. **Phone Test Call** — bound number. Catches telephony-layer issues.

**Don't ship without the LLM Playground pass and at least one Web Test Call.**

---

## Common prompt failures

| Symptom | Likely cause | Fix |
|---|---|---|
| Agent doesn't hang up | No End Call tool, or no explicit trigger in prompt | Add both. |
| Agent skips questions | Too many instructions in one step | Break into numbered steps with "one at a time" emphasis. |
| Agent over-triggers tools | Vague tool triggers ("if needed") | Use exact trigger phrases. |
| Agent under-triggers tools | Tool buried in dense prose | Call it out in a dedicated `## Tools` section. |
| Agent sounds robotic | Missing Style Guardrails, or backchannel disabled for a warm use case | Add Style Guardrails. Enable backchannel for CS/sales. |
| Agent interrupted constantly | `interruption_sensitivity` too high for environment | Lower to 0.7 for noisy environments. |
| Agent says "slash" for "/" or "dot dot dot" for "..." | Speech normalization off | Turn on. |
| Agent mispronounces brand | No boosted keywords or pronunciation guide | Add both. |
| Agent gives up on unclear audio | No retry-then-escalate pattern | Add the three-strike pattern above. |
| Cost per call too high | Prompt >3,500 tokens, or Flex Mode, or premium voice | Trim prompt. Switch to Multi-Prompt. Reconsider voice. |

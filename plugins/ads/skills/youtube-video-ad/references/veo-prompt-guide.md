# VeO 3.1 Prompt Engineering Guide
## For YouTube Ad Video Generation

---

## 1. Prompt Structure

Every VeO prompt should include the following elements, in this order. Omitting elements leads to unpredictable results. More specific is always better.

### The Anatomy of a Great VeO Prompt

**Subject**
Who or what is in the frame. Be specific: age range, ethnicity, clothing, expression, posture. Do not describe exact facial features (causes uncanny valley). Do describe demographic and emotional state.

> "A British woman in her mid-40s, wearing a warm grey jumper and jeans, standing in a domestic kitchen"

**Action**
What is happening. Make it a specific, observable action — not a mood or concept.

> "she holds an energy bill and looks at it with a worried frown" — not "she feels stressed about bills"

**Style**
The visual treatment of the clip.
- `Photorealistic cinematic` — premium ads, emotional stories
- `Documentary handheld` — authenticity, trust-building
- `Clean commercial` — product demos, app screens
- `Aerial/drone` — establishing shots, geographic context

**Camera Movement**
One movement per clip only. Mixing movements in a single clip produces jittery results.
- `Static` — stability, emphasis
- `Slow push-in` — building tension, revelation
- `Slow pull-back` — revealing context, establishing
- `Tracking shot` — following action, energy
- `Handheld` — documentary realism
- `Steadicam` — smooth, professional
- `Crane/jib down` — establishing, grand
- `Drone push forward` — aerial establishing

**Composition**
- `Wide shot` — environment, context
- `Medium shot` — person + environment relationship
- `Medium close-up` — face + upper body, emotional connection
- `Close-up` — face, emotion, detail
- `Extreme close-up` — product detail, eye contact
- `Over-shoulder` — device screens, perspective shots

**Lens Effects**
- `Shallow depth of field` — subject isolation, premium look
- `Bokeh` — soft background blur
- `Anamorphic lens` — cinematic widescreen feel, horizontal lens flares
- `Lens flare` — golden hour, premium energy
- `Deep focus` — environment equally sharp, documentary

**Ambiance**
Lighting quality and environment mood. Be specific about the light source.
- `Soft natural daylight from a nearby window`
- `Golden hour sunlight streaming through windows`
- `Overcast British daylight, soft diffused light`
- `Warm practical lighting from overhead kitchen lights`
- `Cool blue morning light`
- `Dramatic single-source side lighting`

**Audio Direction**
VeO 3.1 generates audio natively. Describe the soundscape as specifically as the visuals.

---

### Complete Prompt Example

> A British homeowner in their 50s, wearing a casual navy jumper, stands in a warm, well-lit kitchen looking concerned at a paper energy bill. The camera slowly pushes in from a medium shot to a close-up of their worried expression. Cinematic photorealistic style, shallow depth of field with the kitchen softly blurred behind them. Soft natural daylight from a nearby window casts gentle shadows. The ambient sound of a quiet kitchen — a clock ticking, the distant hum of a refrigerator, muffled traffic through the window. The homeowner exhales slowly and sets the bill down on the counter.

---

## 2. Region-Specific Patterns

Failing to specify regional context produces generic American-looking visuals. Always anchor the scene geographically.

### UK Ads

**Architecture and Exteriors**
- Terraced houses, semi-detached, Victorian conversions, 1930s bay windows
- Slate and clay tile roofs
- Brick or pebble-dash exteriors
- Small front gardens with low brick walls or privet hedges
- Driveways with block paving or gravel
- British street furniture: red post boxes, cast iron drain covers, BT phone infrastructure
- Grey overcast skies for exteriors — not bright blue unless specifically summer

**Interiors**
- Compact kitchens with under-counter appliances
- British 3-pin plug sockets (rectangular pins)
- Radiators on walls (central heating, not baseboard)
- Combi boiler cupboard in kitchen or airing cupboard
- Gas meter under stairs or in garage
- Carpeted living rooms and stairs (not all hardwood)
- Double-glazed uPVC windows

**People and Clothing**
- Jumpers, cardigans, fleeces
- Wellies for rural/garden scenes
- Flat caps for older male characters in northern/rural settings
- Sensible British footwear (not trainers for professional contexts)
- Describe ethnicity accurately for the target demographic and region

**Vehicles**
- Right-hand drive
- British number plate format (white front, yellow rear)
- Common UK makes: Ford Focus/Fiesta, Vauxhall Astra, VW Golf

**Weather**
- Default to overcast, drizzle, grey skies for exteriors
- Use golden hour specifically only in summer/lifestyle sequences
- Avoid tropical rain or extreme weather unless intentional

### US Ads

- Ranch houses, colonial, craftsman bungalows
- Clapboard or stucco exteriors
- Wide driveways, attached garages, large front lawns
- US 2-pin/3-pin outlets (flat parallel pins)
- Baseboard heating or HVAC vents
- American casual wear (baseball caps, hoodies, denim)
- Left-hand drive vehicles

### EU Ads

- Specify country explicitly: "German new-build apartment", "French stone farmhouse", "Dutch terraced canal house"
- Include country-specific details: shutters (southern Europe), apartment intercoms, specific architectural periods

---

## 3. Common Scene Types for YouTube Ads

Use these as starting templates. Replace all `{VARIABLES}` with specific details.

---

### Scene Type: Product Close-Up

Best for: Hero product shots, brand reveals, feature demonstrations.

```
Extreme close-up of a {PRODUCT_DESCRIPTION}, slowly rotating on a clean {SURFACE_COLOUR} surface. Professional studio lighting with soft fill shadows, single key light from the upper left. The camera tracks smoothly around the product, completing a 90-degree arc. Shallow depth of field, the background fades to a clean gradient. Cinematic photorealistic style. The ambient sound of a silent, professional studio — just faint air conditioning hum.
```

---

### Scene Type: Service Demonstration (Tradesperson)

Best for: Trust-building, showing the work, installer credibility.

```
A certified {PROFESSION} in branded uniform and safety gear is {SPECIFIC_ACTION} in a {ROOM_TYPE} in a typical British {HOUSE_TYPE}. Medium shot, slightly handheld documentary-style camera following the work at a respectful distance. Soft natural daylight from a nearby window supplements the practical overhead lighting. The ambient sounds of professional work — {SPECIFIC_TOOL_SOUNDS}, quiet concentration, occasional professional murmur.
```

---

### Scene Type: Device / App Interaction

Best for: Software demos, app walk-throughs, digital tools.

```
Close-up of hands holding a modern smartphone, the screen showing {APP_DESCRIPTION — describe UI elements, not text}. The person taps the screen with calm confidence, the screen responds with visible visual feedback. Over-shoulder composition, shallow depth of field. Soft ambient office sounds — faint keyboard clicks, distant conversation, air conditioning. The phone screen provides gentle fill light on the hands.
```

---

### Scene Type: Trust Moment / Social Proof (Satisfied Customer)

Best for: Testimonial sequences, end-of-ad resolution, emotional payoff.

```
A {DEMOGRAPHIC} couple in their {AGE_RANGE}, standing in their warm, well-lit living room, smiling with genuine, relaxed satisfaction. They gesture naturally towards their {PRODUCT/IMPROVEMENT}. Medium-wide steadicam shot, slightly lower angle looking up. Warm practical lighting from ceiling lights and a floor lamp. Comfortable domestic ambient sounds — the gentle hum of a well-functioning heating system, distant birdsong through a closed window, the soft sound of a cosy home.
```

---

### Scene Type: Environment / Establishing Shot

Best for: Opening shots, location context, geographic anchoring.

```
Aerial establishing shot of a typical British suburban neighbourhood in {REGION — e.g., East of England, outer London}. Rows of semi-detached houses with slate roofs, green back gardens, driveways, parked cars. Overcast sky with soft diffused morning light. Slow drone push forward at low altitude, gradually descending towards one specific house. Ambient sounds of a quiet British neighbourhood — birdsong, a distant lawnmower, muffled traffic from a nearby road.
```

---

### Scene Type: Problem / Pain Point

Best for: Ad opening hooks, problem-awareness sequences.

```
Close-up of a {PERSON_DESCRIPTION} looking frustrated or concerned at {PROBLEM_VISUAL — describe the visual, not the concept}. Their expression shows genuine concern, not theatrical distress — a realistic worried frown, slightly slumped posture. Slightly desaturated, cool-tinted colour grade. Static camera, medium close-up. The ambient sound emphasises the problem: {PROBLEM_SOUNDS — e.g., "a persistent dripping sound from an old radiator", "the grinding noise of an ageing boiler trying to start"}.
```

---

### Scene Type: Before / After Transition

Best for: Improvement narratives, upgrade stories.

```
BEFORE CLIP: A {ROOM_TYPE} that looks tired and inefficient — {SPECIFIC VISUAL PROBLEMS: old radiator, dated fittings, condensation on windows}. Slightly desaturated, cool-blue colour grade. Static camera, medium wide shot. The ambient sounds of the problem — {PROBLEM_SOUNDS}.

AFTER CLIP: The same {ROOM_TYPE}, now clearly modernised with {SPECIFIC IMPROVEMENTS}. Warm, vibrant colour grade, noticeably brighter. The camera slowly pushes in on the satisfied homeowner. Warm ambient sounds — {POSITIVE_SOUNDS: "the quiet, efficient hum of a new combi boiler", "comfortable warmth"}.
```

Note: VeO generates independent clips. True before/after continuity requires the same room layout in both prompts and post-production editing.

---

### Scene Type: CTA / End Card

**Important: VeO CANNOT reliably generate readable text.**

End cards with text (phone numbers, URLs, CTAs) must be generated separately:
- Use FFmpeg `drawtext` filter on a solid colour background
- Design in Adobe Premiere, DaVinci Resolve, or Canva
- Or use a static image overlay in your video editor

Do not attempt to prompt VeO to render readable text — it will produce distorted, unreadable characters.

---

## 4. Audio Prompting (VeO 3.1 Native Audio)

VeO 3.1 generates audio natively and synchronised with the video. Audio quality is strong for ambient and SFX. Treat the audio description as seriously as the visual description.

### Ambient Soundscapes

Describe the environment's characteristic sounds:

```
The ambient sounds of a quiet British kitchen — a clock ticking on the wall, the low hum of a refrigerator, distant birdsong through a slightly open window, the occasional creak of the house.
```

```
A busy high street in the background — traffic, pedestrian chatter, a bus pulling away — filtered through a double-glazed window.
```

```
A professional trades environment — the controlled hum of tools, the focused quiet of concentrated skilled work.
```

### Sound Effects

Describe specific sounds that reinforce the scene's message:

```
The satisfying click of a modern smart thermostat being adjusted. A gentle digital confirmation tone.
```

```
The grinding, effortful noise of an ageing boiler attempting to fire up — followed by silence and a worrying metallic clunk.
```

```
The quiet, reassuring hum of a newly installed, efficient boiler — barely audible, just present as background warmth.
```

### Dialogue

Use quoted speech in the prompt for character dialogue. VeO will attempt to lip-sync the character:

```
The homeowner looks up from the bill and says, "I didn't realise how much we were spending until we made the switch."
```

**Critical caution**: If you are using ElevenLabs for professional voiceover, do NOT include dialogue in the VeO prompt. The VeO-generated dialogue will conflict with the VO track in post-production. Use VeO for ambient audio and SFX only in those cases.

VeO dialogue is suitable for:
- Social clips where no professional VO is used
- Emotional scene clips where authentic-sounding speech adds realism
- Testimonial-style clips

VeO dialogue is NOT suitable for:
- Precise messaging delivery (VeO may not render words exactly)
- Long sentences (quality degrades)
- Clips paired with professional ElevenLabs VO

---

## 5. Negative Prompt Best Practices

Use the `negativePrompt` API parameter — not negative instructions inside the main prompt text. Putting "no text" or "without logos" in the main prompt is less effective and wastes prompt tokens.

### Default Negative Prompt for All Ad Clips

```
cartoon, anime, stylized illustration, text overlay, written text, watermark, logo, subtitle, caption, low quality, blurry, motion blur, distorted faces, extra limbs, deformed hands, unrealistic lighting, oversaturated colours, film grain excess
```

### People Scenes — Add:

```
uncanny valley, wax-like skin, glassy eyes, dead eyes, unnatural smile, mannequin appearance, overly smooth skin, plastic texture, unnatural pose, stiff movement
```

### Product Scenes — Add:

```
damaged product, dirty, scratched, dented, incorrect brand markings, unrealistic scale, floating product, mismatched shadows
```

### Interior Scenes — Add:

```
cluttered messy room, dark dingy lighting, unrealistic proportions, wrong country furnishings, American electrical outlets, American fixtures
```

### UK Exterior Scenes — Add:

```
palm trees, American architecture, left-hand drive vehicles, American road markings, tropical weather, extreme weather
```

---

## 6. Consistency Techniques

Maintaining visual consistency across a multi-clip ad requires deliberate technique. VeO does not have persistent memory between API calls.

### Technique 1: Global Visual Direction Prefix

Prepend every prompt in a campaign with the same style paragraph:

```
[GLOBAL STYLE: Cinematic photorealistic. Warm, naturalistic colour grading. Soft natural daylight, no harsh artificial lighting. British residential setting throughout. Shallow depth of field on subjects. Professional commercial quality.]
```

Add this as the first line of every prompt, verbatim.

### Technique 2: Reference Images

After generating and approving the first clip:
1. Extract a mid-frame (frame at approximately 4 seconds)
2. Pass the extracted frame via the `referenceImages` parameter in subsequent API calls
3. VeO will use this as a visual anchor for colour grading, lighting, and overall aesthetic
4. Maximum 3 reference images per call

This is the most effective consistency technique available. Use it for recurring characters and environments.

### Technique 3: Consistent Seed

Set `seed: 42` (or any fixed integer) across all calls in a campaign. This increases reproducibility. It does not guarantee identical visuals but reduces variance.

### Technique 4: Character Description Consistency

For any character that appears in multiple clips, write their description identically every time. Copy-paste rather than paraphrase:

> "A British man in his early 60s, warm expression, wearing a navy blue fleece jacket over a checked shirt, grey hair, standing in a domestic British setting"

Using slightly different words ("an older British man" vs "a British man in his early 60s") will produce different-looking characters.

### Technique 5: Post-Production Colour Grade

Even with the above techniques, subtle colour variation between clips is normal. Apply a uniform colour grade (LUT) across all clips in your video editor or via FFmpeg. This is the final consistency layer and should always be applied.

---

## 7. Common Failures and Fixes

| Issue | Likely Cause | Fix |
|-------|-------------|-----|
| Text appears in video | VeO attempting to render text referenced in prompt | Remove all text, numbers, words from prompt. Add `"text overlay, written text, subtitles, captions"` to `negativePrompt`. Never mention words/phrases that look like labels. |
| Wrong country architecture | Insufficient geographic specificity | Add explicit architecture details: house type, roof material, window style, fixtures. For UK, specify "British semi-detached", "uPVC double-glazed windows", "British 3-pin sockets". |
| Uncanny valley faces | Overly specific face descriptions or portrait-mode composition | Describe expression and demographic, not facial features. Pull back to medium shot. Use documentary style. |
| Inconsistent colour/lighting across clips | No global lighting anchor | Add identical Global Visual Direction prefix to all prompts. Apply uniform LUT in post. |
| Jerky or confused camera movement | Multiple camera movements in one prompt | One movement per clip only. Never combine "slow push-in with a slight pan" — pick one. |
| Audio doesn't match scene | Vague or conflicting audio direction | Describe ONE specific ambient soundscape. Do not mix environments (e.g., "busy street and quiet kitchen"). |
| Safety block / generation failure | Sensitive person-related content flagged | Ensure `personGeneration: "allow_adult"` is set. Simplify person descriptions. Remove anything that could reference minors. |
| Product looks wrong or distorted | Insufficient product description | Describe shape, material, finish, size reference. Add product-specific negatives: `"damaged, dirty, incorrect brand"`. |
| Clip too short (4-6s when you need 8s) | Duration not specified or 720p selected | Set `durationSeconds: "8"` explicitly. Confirm resolution is 1080p or 4K (720p supports 4s/6s/8s but defaults shorter). |
| Reference image not working | Wrong duration or resolution | Reference images require `durationSeconds: "8"`. Confirm the image is a clean, mid-frame extract. |
| Dialogue sounds wrong or mouth not syncing | Too long, too complex, or conflicting VO | Keep quoted dialogue to one short sentence. Do not use if also using ElevenLabs VO. |
| Video extension produces wrong resolution | Expected 1080p output | Video extension always outputs 720p. If 1080p is required, generate new clips rather than extending. |

---

## 8. Duration and Resolution Constraints

| Resolution | Available `durationSeconds` Values |
|------------|-----------------------------------|
| 720p | `"4"`, `"6"`, `"8"` |
| 1080p | `"8"` only |
| 4K | `"8"` only |

**Key constraints:**
- Reference images require `durationSeconds: "8"`
- Video extension (extending an existing clip) requires `durationSeconds: "8"` and always outputs 720p regardless of input resolution
- For consistent 1080p throughout, generate new clips rather than using video extension
- Always explicitly set `durationSeconds` — do not rely on defaults

**Recommended for ad clips:** 1080p at 8 seconds. Edit to desired length in post-production. Generates sufficient footage for a 3-7 second cut while giving room for trimming handles.

---

## 9. Prompt Length and Quality

**Target length:** 3-5 sentences per prompt (roughly 60-120 words).

Shorter prompts leave too many variables to chance. Longer, more specific prompts consistently produce better, more controllable output.

### Quality Principles

- Describe what IS in the scene, not what is not. Exclusions belong in `negativePrompt`.
- Be observational and specific: "holds the bill and frowns slightly, exhales" rather than "looks worried about money"
- Include sensory detail beyond visuals: light quality, textures, sounds
- Ground every person in a specific demographic, clothing, and context
- One camera movement. One ambient soundscape. One emotional beat per clip.
- Avoid abstract concepts. VeO generates visuals, not metaphors. "A person feeling the weight of high energy bills" will not work. "A person looking at an energy bill with a worried expression" will.

### Prompt Review Checklist

Before submitting a prompt, confirm:
- [ ] Subject is specific (age, demographic, clothing, expression)
- [ ] Action is observable and physical (not conceptual)
- [ ] Style and camera movement are stated
- [ ] Composition (shot size) is specified
- [ ] Lighting source and quality are described
- [ ] Audio direction is included
- [ ] Regional details are correct for target market
- [ ] No text, words, or numbers in the prompt that should not appear as text on screen
- [ ] `negativePrompt` parameter is set separately
- [ ] `durationSeconds` is explicitly set

---

## 10. API Parameter Reference

For reference when constructing API calls to the Veo endpoint.

| Parameter | Type | Notes |
|-----------|------|-------|
| `prompt` | string | Main prompt text. Follow structure in Section 1. |
| `negativePrompt` | string | What to exclude. Never put exclusions in `prompt`. |
| `durationSeconds` | string | `"4"`, `"6"`, or `"8"`. Always specify explicitly. |
| `aspectRatio` | string | `"16:9"` for YouTube ads standard. |
| `resolution` | string | `"1080p"` recommended for ads. |
| `seed` | integer | Fixed integer for reproducibility (e.g., `42`). |
| `personGeneration` | string | Set `"allow_adult"` for ads featuring people. |
| `referenceImages` | array | Up to 3 image objects. Requires `durationSeconds: "8"`. |

---

*Reference guide for VeO 3.1 prompt engineering. Covers structure, region-specificity, scene types, audio prompting, negative prompts, consistency techniques, failure modes, and technical constraints.*

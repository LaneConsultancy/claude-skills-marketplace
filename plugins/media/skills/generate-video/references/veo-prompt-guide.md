# VeO 3.1 Prompt Engineering Guide
## For Web Design Video Generation

---

## 1. Prompt Structure

Every VeO prompt should include the following elements, in this order. More specific is always better.

### The Anatomy of a Great VeO Prompt

**Subject**
Who or what is in the frame. Be specific: age range, clothing, expression, posture. If using a reference image, state "The person shown in the reference image" and add context about clothing, expression, and action.

> "A confident tradesman in his mid-40s, wearing clean navy work trousers and a branded polo shirt, standing in a modern kitchen"

**Action**
What is happening. Specific, observable action — not a mood or concept.

> "he inspects a newly installed boiler, running his hand along the copper pipework with professional satisfaction" — not "he feels proud of his work"

**Style**
The visual treatment:
- `Photorealistic cinematic` — premium website videos, brand content
- `Documentary handheld` — authenticity, behind-the-scenes, about pages
- `Clean commercial` — product demos, portfolio pieces
- `Aerial/drone` — location establishing shots
- `Slow motion` — hero backgrounds, atmospheric loops

**Camera Movement**
One movement per clip only. Mixing produces jittery results.
- `Static` — stability, emphasis, good for loops
- `Slow push-in` — building connection, revelation
- `Slow pull-back` — revealing context, establishing
- `Slow pan left/right` — environmental scanning, great for hero loops
- `Tracking shot` — following action, energy
- `Handheld` — documentary realism
- `Steadicam` — smooth, professional
- `Crane/jib down` — establishing, grand
- `Drone push forward` — aerial establishing

**Composition**
- `Wide shot` — environment, context, hero backgrounds
- `Medium shot` — person + environment, service demonstrations
- `Medium close-up` — emotional connection, testimonials
- `Close-up` — detail, emotion
- `Extreme close-up` — product detail, craftsmanship
- `Over-shoulder` — perspective, device screens

**Lens Effects**
- `Shallow depth of field` — subject isolation, premium look
- `Bokeh` — soft background blur, atmospheric
- `Anamorphic lens` — cinematic widescreen
- `Deep focus` — everything sharp, documentary

**Ambiance**
Be specific about light source:
- `Soft natural daylight from a nearby window`
- `Golden hour sunlight streaming through windows`
- `Overcast daylight, soft diffused light`
- `Warm practical lighting from overhead lights`
- `Cool blue morning light`

**Audio Direction**
VeO 3.1 generates audio natively. Describe the soundscape as specifically as the visuals. For videos that will be muted on websites, still describe audio — it improves VeO's understanding of the scene.

---

### Complete Prompt Examples

**Hero background loop:**
> A wide establishing shot of a professional plumbing workshop, tools neatly organised on pegboard walls, copper fittings gleaming under warm overhead lighting. The camera slowly pans right across the workspace, revealing workbenches with precision tools and a completed boiler manifold. Photorealistic cinematic style, deep focus keeping the entire workshop sharp. Warm practical lighting from industrial pendant lamps. Ambient sounds of a quiet, professional workshop — the gentle hum of ventilation, occasional metallic resonance from tools.

**Service demonstration:**
> A certified plumber in branded navy overalls crouches beside an open boiler unit in a modern British kitchen, methodically connecting copper pipework with a torch. Medium shot, documentary handheld style, camera follows the craftsman's hands at working distance. Natural daylight from a kitchen window supplements the overhead lighting. Shallow depth of field keeps focus on the skilled work. The ambient sounds of professional plumbing work — the careful hiss of a soldering torch, the satisfying click of compression fittings being tightened.

**Team/about page:**
> The person shown in the reference image, wearing a clean navy polo shirt with company branding, stands in a bright, modern office space. They look directly into camera with a warm, confident expression, arms relaxed at their sides. Medium close-up composition, steadicam with very subtle movement. Soft natural daylight from large windows behind, creating a bright, professional atmosphere. Shallow depth of field softly blurs the office background. The quiet ambient sounds of a professional office — distant keyboard typing, soft air conditioning hum.

---

## 2. Reference Image Best Practices

Reference images are the most powerful tool for consistency. Use them strategically.

### Person References

When the user provides a photo of a real person (business owner, team member):

1. **Include in every scene where that person appears** — via the `referenceImages` API parameter
2. **Describe the person relative to the reference**: "The person from the reference image, now wearing [different clothing] and [doing specific action]"
3. **Don't describe exact facial features** — let the reference image handle appearance. Describe clothing, posture, expression, and action.
4. **Maintain consistency**: Same seed (42), same reference image, similar lighting descriptions across scenes
5. **VeO will approximate, not replicate**: Expect a similar-looking person, not an exact match. This is a feature, not a bug — it avoids uncanny valley while maintaining recognisability.

### Location References

Photos of the actual business premises, workshop, or service area:
- Include in scene prompts set in that location
- Describe specific elements from the photo: "The same brick-walled workshop shown in the reference, with the green tool cabinet visible on the left"
- VeO will use the reference for colour palette, lighting mood, and general spatial layout

### Style References

Mood boards, screenshots from videos they admire, or brand photography:
- Use as style anchors for colour grading, lighting quality, and atmosphere
- Describe what you want carried over: "Match the warm, golden lighting and shallow depth of field from the reference image"

### Technical Constraints

- Maximum 3 reference images per API call
- Priority order when you have more than 3: (1) person reference, (2) auto-generated consistency frame, (3) location/style reference
- Reference images require `durationSeconds: "8"`
- Images should be clear, well-lit, and at least 512px on the shortest side

---

## 3. Common Scene Types for Web Design Videos

### Scene Type: Hero Background Loop

```
Wide establishing shot of {SETTING — be specific}. The camera {slow pan / slow zoom / slow drift} across the scene, maintaining steady, continuous motion suitable for seamless looping. {VISUAL_STYLE — photorealistic, cinematic, deep focus}. {LIGHTING — describe source and quality}. {AMBIENT_AUDIO — describe environmental sounds}.
```

**Key rules for loops:**
- Use continuous, directional camera movement (slow pan works best)
- Avoid sudden actions, people walking in/out of frame, or dramatic lighting changes
- Keep the scene's energy level constant throughout the 8 seconds
- The start and end of the clip should feel similar enough to loop without jarring
- Deep focus (everything sharp) is usually better than shallow DOF for backgrounds
- Don't include people unless they're relatively static (e.g., someone working steadily at a task)

### Scene Type: Service Demonstration

```
A {PROFESSIONAL_DESCRIPTION} is {SPECIFIC_ACTION} in a {SETTING}. {SHOT_SIZE — medium or medium close-up}, {CAMERA_STYLE — documentary handheld or steadicam}. {LIGHTING}. Shallow depth of field keeps focus on the skilled work. The ambient sounds of professional work — {SPECIFIC_SOUNDS}.
```

### Scene Type: Person Feature (from reference image)

```
The person shown in the reference image, {CLOTHING_DESCRIPTION}, {SETTING — where are they}. They {ACTION — look into camera / work at desk / walk through space / gesture while speaking}. {SHOT_SIZE}, {CAMERA_MOVEMENT}. {LIGHTING}. {EXPRESSION — warm, confident, focused, relaxed}. {AMBIENT_AUDIO}.
```

### Scene Type: Product / Equipment Close-Up

```
Extreme close-up of {PRODUCT_DESCRIPTION}, {ACTION — being used / rotating / being assembled}. {CAMERA_MOVEMENT}. Professional studio-quality lighting with soft fill shadows. Shallow depth of field, background fades to {COLOUR — clean gradient or contextual blur}. {AUDIO — describe relevant sounds}.
```

### Scene Type: Location / Environment Establishing

```
{SHOT_TYPE — aerial / wide / drone push-in} of {SPECIFIC_LOCATION — include architectural and geographic details}. {TIME_OF_DAY — morning, golden hour, midday}. {WEATHER — overcast, sunny, etc.}. {CAMERA_MOVEMENT — slow drone forward / establishing pan}. {AMBIENT_AUDIO — environmental sounds specific to this location}.
```

### Scene Type: Before / After

```
BEFORE: {ROOM/SPACE} showing {SPECIFIC_PROBLEMS — describe visually}. Slightly desaturated, cool colour grade. Static camera, {SHOT_SIZE}. {PROBLEM_SOUNDS}.

AFTER: The same {ROOM/SPACE}, now {SPECIFIC_IMPROVEMENTS}. Warm, vibrant colour grade. Camera {MOVEMENT — slow push-in}. {POSITIVE_SOUNDS}.
```

---

## 4. Audio Prompting

### For videos that will be MUTED on websites

Still describe audio in the prompt — it helps VeO understand the scene context. The generated audio will be stripped in post-production.

### Ambient Soundscapes

```
The ambient sounds of a quiet British kitchen — a clock ticking, the low hum of a refrigerator, distant birdsong through a window.
```

```
A professional workshop — controlled hum of machinery, focused concentration, the clink of metal tools.
```

### For VeO dialogue (when NOT using ElevenLabs)

Include short quoted speech. VeO will attempt lip-sync:
```
The business owner looks into camera and says, "We've been doing this for twenty years, and every job still matters."
```

**Critical**: If using ElevenLabs VO, do NOT include dialogue in VeO prompts.

---

## 5. Negative Prompt Best Practices

Use the `negativePrompt` API parameter — not negative instructions in the main prompt.

### Default for all clips:
```
cartoon, anime, stylized illustration, text overlay, written text, watermark, logo, subtitle, caption, low quality, blurry, motion blur, distorted faces, extra limbs, deformed hands, unrealistic lighting, oversaturated colours
```

### People scenes — add:
```
uncanny valley, wax-like skin, glassy eyes, unnatural smile, mannequin appearance, overly smooth skin, plastic texture, stiff movement
```

### Interior scenes — add:
```
cluttered messy room, dark dingy lighting, unrealistic proportions, wrong country furnishings
```

### Background loop scenes — add:
```
sudden movements, people entering or exiting frame, dramatic lighting changes, camera shake, jerky motion
```

---

## 6. Consistency Techniques

### Technique 1: Global Visual Direction Prefix
Prepend every prompt with the same style paragraph.

### Technique 2: Reference Images
After generating the first clip, extract a mid-frame and use it as a reference image for subsequent calls.

### Technique 3: Consistent Seed
Use `seed: 42` across all calls.

### Technique 4: Character Description Consistency
Copy-paste character descriptions exactly — don't paraphrase.

### Technique 5: Post-Production Colour Grade
Apply a uniform LUT across all clips in post.

---

## 7. Common Failures and Fixes

| Issue | Cause | Fix |
|-------|-------|-----|
| Text in video | VeO rendered text from prompt | Remove text references. Add to negativePrompt. |
| Wrong architecture | Not enough geographic detail | Add specific building types, fixtures, details. |
| Uncanny faces | Over-specific face descriptions | Describe expression/demographic, not features. Use reference images. |
| Inconsistent colour | No global anchor | Use Global Visual Direction + reference frame + same seed. |
| Jerky camera | Multiple movements specified | One movement per clip. |
| Audio mismatch | Conflicting audio description | One ambient soundscape per clip. |
| Person doesn't match reference | Reference image too small or unclear | Use high-quality, well-lit reference photos. |
| Loop doesn't loop | Too much change during clip | Use slower movements, static scenes, consistent lighting. |

---

## 8. Duration and Resolution

| Resolution | durationSeconds |
|------------|----------------|
| 720p | "4", "6", "8" |
| 1080p | "8" only |

Reference images require `durationSeconds: "8"`.

---

## 9. API Parameter Reference

| Parameter | Type | Notes |
|-----------|------|-------|
| `prompt` | string | Main prompt text |
| `negativePrompt` | string | Exclusions |
| `durationSeconds` | string | Always "8" for 1080p |
| `aspectRatio` | string | "16:9" or "9:16" |
| `resolution` | string | "1080p" recommended |
| `seed` | integer | Fixed (42) for consistency |
| `personGeneration` | string | "allow_adult" for people |
| `referenceImages` | array | Up to 3 images. Requires durationSeconds: "8" |

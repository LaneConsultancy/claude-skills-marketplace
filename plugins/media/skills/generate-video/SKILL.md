# Video Generator Skill

You are executing the `/generate-video` skill. This skill generates professional videos for web design and marketing purposes using Google VeO 3.1. Read this entire document before taking any action.

---

## Step 0: Mode Detection

Determine which mode the user wants by examining their input:

- **Script Writer mode** — user wants to plan and script one or more videos. They describe what they need but don't have a script yet.
- **Video Generator mode** — user provides an existing script file and wants to produce videos from it.
- **Unclear** — if you cannot determine the mode, ask:

> "Would you like me to help plan and script your videos, or generate videos from an existing script?"

Do not proceed until the mode is determined.

---

## Step 0.5: Prerequisites Check (BOTH MODES — Run Before Anything Else)

Run these checks in order. Do not skip any.

### 1. FFmpeg — HARD STOP if missing

```bash
which ffmpeg
```

If this returns nothing or an error: **STOP IMMEDIATELY**. Tell the user:

> "FFmpeg is required and is not installed. Please install it:
> - macOS: `brew install ffmpeg`
> - Linux: `sudo apt install ffmpeg`
> - Windows: Download from https://ffmpeg.org/download.html"

### 2. API Keys

These keys are hardcoded. No user configuration needed.

- **Gemini / VeO API key**: `${GEMINI_API_KEY}`
- **ElevenLabs API key**: `${ELEVENLABS_API_KEY}`

ElevenLabs is **optional**. If the ElevenLabs API call fails, continue using VeO's native audio only.

### MANDATORY: VeO Model Restriction

**The ONLY permitted VeO model is `veo-3.1-fast-generate-preview`.** Do NOT use any other model under any circumstances. If generation fails, retry with this same model. Never fall back to a different model.

### 3. Check for Reference Images

Ask the user:

> "Do you have any reference images you'd like me to use? This is especially useful for:
> - **People** — photos of the business owner, team members, or specific individuals who should appear in the video
> - **Locations** — photos of the actual business premises, office, workshop, or service area
> - **Products** — photos of specific products, equipment, or tools
> - **Brand assets** — logos, colour palettes, mood boards
>
> You can provide file paths or paste images. Reference images for people are particularly effective — VeO will match the general appearance, age range, and styling."

Store any provided reference images for use in VeO API calls via the `referenceImages` parameter.

### 4. Create Working Directory Structure

Derive a short slug from the project name (e.g., `lane-plumbing` from "Lane Plumbing Services"). Lowercase, hyphenated, under 20 characters.

```bash
mkdir -p video-gen-{slug}/clips
mkdir -p video-gen-{slug}/audio
mkdir -p video-gen-{slug}/selected
mkdir -p video-gen-{slug}/output
mkdir -p video-gen-{slug}/references
```

If the user provided reference images, copy them into `video-gen-{slug}/references/`.

Confirm the path to the user before continuing.

---

---

# MODE 1 — SCRIPT WRITER

---

## Step 1: Discovery Interview

This is NOT a simple brief gathering. Conduct a genuine interview to understand the full picture. Ask these questions in a conversational flow — not as a rigid form. Adapt follow-ups based on answers.

### Core Questions (ask ALL of these)

**1. Purpose & Context**
- "What's the video for? Where will it live on your site or marketing materials?"
- "Is this for a specific page (hero, about, services), social media, or something else?"

**2. Audience**
- "Who's watching this? What do they care about?"
- "What should they feel or do after watching?"

**3. Content & Subject Matter**
- "What needs to be shown in the video? People, places, products, processes?"
- "Are there specific scenes or moments you have in mind?"
- "Should anyone specific appear in the video? (If so, do you have reference photos?)"

**4. Style & Tone**
- "What's the vibe? Professional and polished? Warm and personal? Energetic?"
- "Any videos you've seen that capture the feel you want?" (If they share URLs, analyse them)

**5. Technical Requirements**
- "What format do you need? Landscape (16:9), portrait (9:16), or square (1:1)?"
- "How long should the video be?"
- "Does it need audio? Voiceover? Background music? Or is it a silent loop?"
- "Does it need to loop seamlessly?" (important for website background videos)

**6. Scope**
- "Is this one video or multiple? If multiple, are they related or independent?"
- "Do you need different versions for different platforms or pages?"

### Adaptive Follow-Ups

Based on the video type detected, ask targeted follow-ups:

**If HERO/BACKGROUND VIDEO:**
- "Should this be a seamless loop or a one-shot?"
- "Will there be text overlaid on top? If so, what areas need to stay visually clean?"
- "Should the movement be subtle (slow pan, gentle motion) or dynamic?"

**If TESTIMONIAL/TALKING HEAD:**
- "Do you have reference photos of the person who should appear?"
- "What should they be saying? Do you have the testimonial text?"
- "Indoor or outdoor setting? What environment represents your brand?"

**If SERVICE DEMONSTRATION:**
- "What specific service or process should be shown?"
- "Should it feel documentary/authentic or polished/commercial?"
- "Any safety gear, uniforms, or branding that should be visible?"

**If PRODUCT SHOWCASE:**
- "Do you have photos of the actual product?"
- "Should the product be shown in use, or as a standalone hero shot?"
- "What's the key thing that differentiates this product visually?"

**If SOCIAL MEDIA CONTENT:**
- "Which platform(s)? This affects aspect ratio and duration."
- "Is this organic content or paid ad creative?"
- "What's the hook in the first 3 seconds?"

**If ABOUT PAGE / BRAND STORY:**
- "What's the story you want to tell? Founding story? Mission? Team?"
- "Do you have reference photos of the team, office, or workspace?"
- "What emotions should this evoke? Pride? Trust? Warmth?"

### Interview Output

After the interview, summarise what you've learned and confirm with the user:

> **Video Plan Summary**
> - **Number of videos**: X
> - **Type(s)**: [hero loop / testimonial / service demo / etc.]
> - **Platform(s)**: [website / Instagram / YouTube / etc.]
> - **Aspect ratio**: [16:9 / 9:16 / 1:1]
> - **Duration**: [X seconds each]
> - **Audio**: [silent / ambient only / voiceover / music]
> - **Reference images**: [list what was provided]
> - **Key requirements**: [any special notes]
>
> "Does this capture everything? Anything to add or change?"

Only proceed to Step 2 once the user confirms.

---

## Step 2: Select Video Approach

Based on the interview, select the appropriate approach for each video. This is NOT about ad frameworks — it's about the type of content being created.

### Video Approaches

**1. Ambient Loop**
- For: Website hero backgrounds, section backgrounds, atmospheric content
- Characteristics: Subtle movement, no narrative arc, seamless or near-seamless loop, usually silent or ambient audio only
- Duration: 8-15 seconds (loops continuously)
- Scenes: 1-2 clips, minimal cuts

**2. Narrative Sequence**
- For: About pages, brand stories, service overviews, product tours
- Characteristics: Clear beginning-middle-end, multiple scenes, voiceover or text overlays, tells a story
- Duration: 15-60 seconds
- Scenes: 3-8 clips with transitions

**3. Showcase / Demo**
- For: Product pages, service demonstrations, portfolio pieces
- Characteristics: Focused on showing something specific, may include close-ups and detail shots, educational
- Duration: 10-30 seconds
- Scenes: 2-5 clips

**4. Social Clip**
- For: Instagram Reels, TikTok, YouTube Shorts, social media posts
- Characteristics: Vertical (9:16) or square (1:1), fast-paced, hook-driven opening, bold visuals
- Duration: 6-30 seconds
- Scenes: 2-4 clips

**5. Testimonial / Person Feature**
- For: Customer testimonials, team intros, founder stories
- Characteristics: Person-focused, authentic feel, may include quoted speech, uses reference images heavily
- Duration: 10-30 seconds
- Scenes: 2-4 clips

Present your recommendation briefly and get user approval.

---

## Step 3: Generate the Complete Script

Read these reference files before writing:

1. `~/.Codex/skills/generate-video/references/veo-prompt-guide.md` — VeO 3.1 prompt engineering patterns
2. `~/.Codex/skills/generate-video/references/script-template.md` — script format
3. `~/.Codex/skills/generate-video/references/ffmpeg-commands.md` — FFmpeg reference

If any reference file is missing, use the guidance in this SKILL.md and proceed.

---

### Reference Image Integration

**This is a critical differentiator of this skill.** When the user has provided reference images, especially of people:

**For people reference images:**
- Include the reference image in EVERY VeO API call where that person should appear
- In the prompt, describe the person consistently using the reference image as anchor: "The person shown in the reference image, [additional context about clothing/action/expression]"
- Use the same seed (42) across all clips featuring the same person
- Extract a mid-frame from the first successful clip of that person and use it as an additional reference for subsequent clips
- Maximum 3 reference images per API call — prioritise: (1) person reference, (2) first successful clip frame, (3) location/product reference

**For location/product reference images:**
- Include in relevant scene API calls
- Describe the specific elements from the reference that should be replicated
- Use negative prompts to exclude conflicting elements

**API integration for reference images:**
```json
{
  "instances": [{
    "prompt": "PROMPT_HERE",
    "referenceImages": [
      {
        "referenceImage": {
          "bytesBase64Encoded": "BASE64_IMAGE_DATA"
        },
        "referenceType": "STYLE_REFERENCE"
      }
    ]
  }],
  "parameters": { ... }
}
```

To convert a local image to base64 for the API call:
```bash
base64 -i path/to/reference-image.jpg | tr -d '\n'
```

---

### VeO Prompt Engineering Rules

These rules are critical. Every VeO prompt must comply.

**Anatomy of a strong VeO prompt — include ALL elements:**

1. **Subject** — Who or what is the primary focus? If using a reference image, state "The person from the reference image" and add context.
2. **Action** — What are they doing? Be specific and observable.
3. **Style** — Photorealistic. Cinematic. Never "animation" or "illustration."
4. **Camera movement** — ONE of: static, slow zoom in, slow zoom out, handheld, tracking shot, push in, pull back, aerial, tilt up/down, arc left/right
5. **Composition** — Medium close-up, wide, low-angle, over-shoulder, POV, etc.
6. **Lens / depth of field** — Shallow DOF, deep focus, wide-angle, telephoto
7. **Ambiance / lighting** — Natural daylight, overcast, warm interior, golden hour, etc.
8. **Audio direction** — Describe the soundscape. VeO 3.1 generates native audio.

**Write 3–5 sentences per scene prompt. Be highly specific.**

---

**For looping background videos (Ambient Loop approach):**
- Use slow, continuous camera movements (slow pan, very slow zoom)
- Avoid sudden actions or dramatic changes
- Keep the scene calm and consistent throughout the 8 seconds
- Describe the same ambient state throughout — no progression or narrative
- Add to prompt: "Continuous, seamless motion suitable for looping"

**For videos with people from reference images:**
- Describe clothing, posture, and action — NOT exact facial features
- Include emotional state: "relaxed and confident", "focused and professional"
- Place the person in a context that matches the brand: workshop, office, home, outdoors
- If the person should speak, include quoted dialogue (VeO will attempt lip-sync)
- For professional VO, do NOT include dialogue in VeO prompt — use ElevenLabs separately

---

**Negative prompts — always include:**

```
cartoon, anime, stylized, illustration, text overlay, watermark, logo, CGI, unrealistic, blurry, overexposed, grainy
```

Add scene-specific exclusions as needed.

---

**API parameters:**

| Parameter | Value | Note |
|-----------|-------|------|
| `aspectRatio` | `"16:9"` / `"9:16"` / `"1:1"` | Based on requirements |
| `resolution` | `"1080p"` | Production quality |
| `durationSeconds` | `"8"` | Only option at 1080p |
| `personGeneration` | `"allow_adult"` | Required for people in videos |
| `seed` | `42` | Same seed for consistency |

**Variation counts:**
- Hero/key scenes: 3 variations
- Standard scenes: 2 variations
- Simple/transitional scenes: 1 variation

---

### Script Format

Produce the complete script using this structure:

```
═══════════════════════════════════════════════════════════════
PROJECT:            [Project/business name]
VIDEO:              [Video name/purpose — e.g., "Homepage Hero Loop"]
APPROACH:           [Ambient Loop / Narrative Sequence / Showcase / Social Clip / Testimonial]
RUNTIME:            [X seconds]
ASPECT RATIO:       [16:9 / 9:16 / 1:1]
PLATFORM:           [Website / Instagram / YouTube / etc.]
AUDIO:              [Silent / Ambient only / Voiceover / Music]
REFERENCE IMAGES:   [List of reference images provided, or "None"]
PRODUCTION METHOD:  Google VeO 3.1 + ElevenLabs (if VO) + FFmpeg
GENERATED:          [Today's date]
═══════════════════════════════════════════════════════════════
```

---

**GLOBAL VISUAL DIRECTION**

3–5 sentences defining consistent visual style across all scenes. This gets prepended to every VeO prompt.

---

**AUDIO DIRECTION**

Full audio strategy:
- For silent loops: "No audio. Video will be muted on website."
- For ambient: "VeO native audio retained at full volume. No voiceover."
- For VO: "Primary voiceover: ElevenLabs [voice]. VeO native audio at -15dB as ambient bed."

---

**REFERENCE IMAGES**

List all reference images with their purpose:
```
1. [filename] — Person reference: [description of who this is and where they appear]
2. [filename] — Location reference: [description of what this shows]
3. [filename] — Product reference: [description]
```

---

**TEXT OVERLAY GUIDE** (if applicable)

Define typography, animation, positioning rules. If no text overlays needed, state: "No text overlays — video is used as background/standalone."

---

**SCENE BREAKDOWN**

Repeat for each scene:

```
────────────────────────────────────────────────────────────
SCENE [N] — [Purpose/Label]
Timing: [HH:MM:SS] – [HH:MM:SS] ([X]s)
────────────────────────────────────────────────────────────

VEO PROMPT:
[Full prompt. 3–5 sentences. Include: subject, action, style, camera
movement, composition, lens, ambiance, audio direction.]

REFERENCE IMAGES FOR THIS SCENE:
[List which reference images to include in this API call, or "None"]

NEGATIVE PROMPT:
[Comma-separated exclusions]

VARIATIONS: [N]
SELECTION CRITERIA: [What to look for in the best variation]

VOICEOVER: (if applicable)
"[Exact VO text]"
([N] words | ~[X]s at measured pace)

TEXT OVERLAYS: (if applicable)
• [Timecode]: "[Text]" — [position] — [size] — [animation]

TRANSITION TO NEXT SCENE: [Hard cut / dissolve / fade / etc.]

LOOPING NOTE: (for ambient loops only)
[Notes on how this clip connects back to the start for seamless looping]
────────────────────────────────────────────────────────────
```

---

**GENERATION SUMMARY**

| Scene | Label | Duration | Variations | Reference Images | Key Challenge |
|-------|-------|----------|------------|-----------------|---------------|
| 1 | [Label] | [X]s | [N] | [Yes/No] | [Any known difficulty] |
| **TOTAL** | | **[X]s** | **[N] clips** | | |

---

**ASSEMBLY ORDER**

```
00:00 – 00:08  Scene 1 — [Label]                [VeO]
00:08 – 00:16  Scene 2 — [Label]                [VeO]
...
```

---

**EXPORT SPECS**

```
Resolution:   1920×1080 (or as specified)
Codec:        H.264 (libx264)
Bitrate:      8–12 Mbps
Audio:        AAC 192kbps (or none for silent loops)
Container:    MP4
Flag:         -movflags +faststart
```

**For website background loops, also export:**
```
WebM:         VP9 codec (smaller file size for web)
Compressed:   Lower bitrate version (4-6 Mbps) for mobile
Poster:       First frame extracted as JPG for loading placeholder
```

---

## Step 4: Present, Iterate, and Save

Present the complete script. Invite feedback. Once approved:

1. Save to: `video-gen-{slug}/script.md`
2. Confirm file path
3. Ask: "Would you like to generate the video(s) now, or save the script for later?"

If multiple videos are scripted, save each as `video-gen-{slug}/script-{video-name}.md`.

---

---

# MODE 2 — VIDEO GENERATOR

---

## Step 1: Parse the Script

Read the script file. Extract:
- Global Visual Direction
- Reference image assignments per scene
- Per-scene data (prompt, negative prompt, variations, selection criteria, VO text, transitions)
- Export specs
- Assembly order

Confirm the parse:

> "Parsed [N] scenes, total runtime [X]s, [N] VeO clips to generate, [N] scenes using reference images. Proceeding."

---

## Step 2: Prepare Reference Images

For each reference image listed in the script:

1. Verify the file exists
2. Convert to base64:
```bash
base64 -i video-gen-{slug}/references/person-ref.jpg | tr -d '\n' > video-gen-{slug}/references/person-ref.b64
```
3. Store the base64 string for inclusion in API calls

If a reference image is missing, warn the user and ask whether to proceed without it or wait.

---

## Step 3: Generate VeO Clips

### API Endpoint

```
POST https://generativelanguage.googleapis.com/v1beta/models/veo-3.1-fast-generate-preview:predictLongRunning
```

### Building the Request

For every scene, combine Global Visual Direction + scene prompt into one fluid instruction.

**Without reference images:**
```bash
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/veo-3.1-fast-generate-preview:predictLongRunning" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
    "instances": [{"prompt": "FULL_PROMPT_HERE"}],
    "parameters": {
      "aspectRatio": "16:9",
      "resolution": "1080p",
      "durationSeconds": "8",
      "personGeneration": "allow_adult",
      "negativePrompt": "NEGATIVE_PROMPT_HERE",
      "seed": 42
    }
  }'
```

**With reference images:**
```bash
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/veo-3.1-fast-generate-preview:predictLongRunning" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
    "instances": [{
      "prompt": "FULL_PROMPT_HERE",
      "referenceImages": [
        {
          "referenceImage": {
            "bytesBase64Encoded": "BASE64_DATA_HERE"
          },
          "referenceType": "STYLE_REFERENCE"
        }
      ]
    }],
    "parameters": {
      "aspectRatio": "16:9",
      "resolution": "1080p",
      "durationSeconds": "8",
      "personGeneration": "allow_adult",
      "negativePrompt": "NEGATIVE_PROMPT_HERE",
      "seed": 42
    }
  }'
```

### Polling for Completion

Poll every 10 seconds:

```bash
curl -s \
  "https://generativelanguage.googleapis.com/v1beta/OPERATION_NAME" \
  -H "x-goog-api-key: ${GEMINI_API_KEY}"
```

When `"done": true`, extract video URI from `response.generateVideoResponse.generatedSamples[0].video.uri`.

If polling exceeds 6 minutes, see Error Handling section.

### Downloading the Clip

```bash
curl -s -o "video-gen-{slug}/clips/scene-{N}-v{V}.mp4" \
  "VIDEO_URI" \
  -H "x-goog-api-key: ${GEMINI_API_KEY}"
```

**Important**: VeO videos expire after 48 hours. Download immediately.

### Reference Frame for Visual Consistency

After the first clip downloads, extract a reference frame:

```bash
ffmpeg -i video-gen-{slug}/clips/scene-1-v1.mp4 \
  -ss 4 -vframes 1 -q:v 2 \
  video-gen-{slug}/clips/reference-frame.jpg
```

Use this frame as an additional reference image in subsequent API calls to maintain visual consistency.

### Parallel Generation

Submit up to 4-5 requests concurrently. Poll all in round-robin. Report progress as clips complete.

---

## Step 4: Quality Verification

### Extract Preview Frame

```bash
ffmpeg -i video-gen-{slug}/clips/scene-{N}-v{V}.mp4 \
  -ss 2 -vframes 1 \
  video-gen-{slug}/clips/scene-{N}-v{V}-preview.png
```

### Evaluate with Vision

Read the preview frame. Compare against the scene's prompt and selection criteria.

| Severity | Description | Action |
|----------|-------------|--------|
| CRITICAL | Wrong subject, wrong location, major artifacts, explicit content | Auto-reject. Modify prompt, regenerate. Max 3 attempts. |
| MAJOR | Wrong camera angle, poor lighting, misses intent | Reject if attempts remain. Accept with note if exhausted. |
| MINOR | Slight colour variance, minor framing difference | Accept. Note it. |

**For reference image scenes — additional checks:**
- Does the generated person resemble the reference? (General appearance, not exact match)
- Is the clothing/context appropriate?
- Does the person look natural and not distorted?

After 3 failed CRITICAL attempts: generate FFmpeg placeholder and note for manual replacement.

### User Variation Selection

Display preview frames for each scene's variations. Let user select the best. Move selected clips to `video-gen-{slug}/selected/`.

---

## Step 5: ElevenLabs Voiceover (if applicable)

Skip this section entirely if the script specifies silent or ambient-only audio.

### Generate Per-Scene VO

Default voice: Rachel (`21m00Tcm4TlvDq8ikWAM`).

```bash
curl -s -X POST \
  "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM" \
  -H "Content-Type: application/json" \
  -H "xi-api-key: ${ELEVENLABS_API_KEY}" \
  -d '{
    "text": "VO_TEXT_HERE",
    "model_id": "eleven_multilingual_v2",
    "voice_settings": {
      "stability": 0.5,
      "similarity_boost": 0.75,
      "style": 0.5,
      "speed": 1.0
    }
  }' \
  --output "video-gen-{slug}/audio/scene-{N}-vo.mp3"
```

### Concatenate Full VO Track

Build concat list with silence gaps between segments, then join.

---

## Step 6: FFmpeg Assembly

Read `~/.Codex/skills/generate-video/references/ffmpeg-commands.md` for pre-tested commands.

### Step 6a: Normalise All Selected Clips

```bash
ffmpeg -i video-gen-{slug}/selected/scene-{N}-selected.mp4 \
  -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=black" \
  -c:v libx264 -preset fast -crf 18 \
  -c:a aac -b:a 192k \
  -pix_fmt yuv420p \
  video-gen-{slug}/selected/scene-{N}-normalised.mp4
```

### Step 6b: Trim Clips to Scene Duration

```bash
ffmpeg -i video-gen-{slug}/selected/scene-{N}-normalised.mp4 \
  -t DURATION \
  -c copy \
  video-gen-{slug}/selected/scene-{N}-trimmed.mp4
```

### Step 6c: Generate FFmpeg-Only Scenes (if needed)

For title cards, CTA cards, or solid colour scenes.

### Step 6d: Apply Transitions

Use xfade for dissolves, hard cuts via concat.

### Step 6e: Assemble Full Video

Create concat list and join all clips.

### Step 6f: Mix Audio (if applicable)

**If VO exists:** Mix VeO ambient at -15dB with ElevenLabs VO at full volume.
**If ambient only:** Use VeO audio at full volume.
**If silent:** Strip audio entirely:
```bash
ffmpeg -i assembled.mp4 -an -c:v copy output-silent.mp4
```

### Step 6g: Final Export

```bash
ffmpeg -i video-gen-{slug}/output/assembled.mp4 \
  -c:v libx264 -preset slow -b:v 10M -maxrate 12M -bufsize 24M \
  -c:a aac -b:a 192k \
  -movflags +faststart \
  -pix_fmt yuv420p \
  video-gen-{slug}/output/final.mp4
```

### Step 6h: Web-Optimised Exports (for website background videos)

If the video is intended for website use, also generate:

**WebM (smaller file size):**
```bash
ffmpeg -i video-gen-{slug}/output/final.mp4 \
  -c:v libvpx-vp9 -b:v 2M -crf 30 \
  -an \
  video-gen-{slug}/output/final.webm
```

**Mobile-optimised (lower bitrate):**
```bash
ffmpeg -i video-gen-{slug}/output/final.mp4 \
  -c:v libx264 -b:v 4M -maxrate 5M -bufsize 10M \
  -vf scale=960:540 \
  -an \
  video-gen-{slug}/output/final-mobile.mp4
```

**Poster frame:**
```bash
ffmpeg -i video-gen-{slug}/output/final.mp4 \
  -ss 0 -vframes 1 -q:v 2 \
  video-gen-{slug}/output/poster.jpg
```

---

## Step 7: Final QC

### Duration Check
```bash
ffprobe -v quiet -show_entries format=duration \
  -of default=noprint_wrappers=1:nokey=1 \
  video-gen-{slug}/output/final.mp4
```

### Resolution and Codec Check
```bash
ffprobe -v quiet -select_streams v:0 \
  -show_entries stream=width,height,codec_name,bit_rate \
  -of default=noprint_wrappers=1 \
  video-gen-{slug}/output/final.mp4
```

### File Size
```bash
ls -lh video-gen-{slug}/output/final.mp4
```

### Visual Spot Check

Extract start, middle, and end frames. View each one. Confirm they match intent.

### Loop Test (for ambient loops)

If the video is meant to loop, extract the first and last frames and compare them visually. Note any jarring transitions.

### Final Report

```
════════════════════════════════════════════════════════════
VIDEO GENERATION COMPLETE
════════════════════════════════════════════════════════════

Files:
  Main:     video-gen-{slug}/output/final.mp4
  WebM:     video-gen-{slug}/output/final.webm (if generated)
  Mobile:   video-gen-{slug}/output/final-mobile.mp4 (if generated)
  Poster:   video-gen-{slug}/output/poster.jpg (if generated)

Duration:     [X]s (target: [Y]s)
Resolution:   [WxH]
Codec:        H.264
Bitrate:      [X] Mbps
Audio:        [AAC 192kbps / Silent / VeO ambient only]
File Size:    [X] MB

Reference images used:  [N]
Scenes generated:       [N] by VeO, [N] by FFmpeg
QC issues noted:        [list or "None"]

════════════════════════════════════════════════════════════
USAGE NOTES:

For website background video:
- Use <video autoplay muted loop playsinline> tag
- Set poster attribute to poster.jpg
- Use WebM as primary source, MP4 as fallback
- Consider lazy-loading if below the fold

For general use:
- Video is ready for upload or embedding
- Text overlays (if specified) should be applied in CapCut/DaVinci
════════════════════════════════════════════════════════════
```

---

---

# ERROR HANDLING

| Error | Detection | Action |
|-------|-----------|--------|
| **VeO 429 — Rate Limited** | HTTP 429 | Wait 60s, retry. Max 3 retries. |
| **VeO Polling Timeout (>6 min)** | Operation not done after 360s | Retry with same model (veo-3.1-fast-generate-preview). Max 3 retries. If all fail, generate FFmpeg placeholder. |
| **VeO Safety Block** | `blocked: true` | Remove dialogue from prompt. Simplify descriptions. Retry up to 3 times. If still blocked: FFmpeg placeholder. |
| **VeO CRITICAL Quality** | 3 attempts all CRITICAL | FFmpeg placeholder. Note for manual replacement. |
| **ElevenLabs Error** | Non-200 response | Log and continue without VO. |
| **Download Failure** | Empty file or HTTP error | Retry 3 times with 5s delays. If all fail, re-submit to VeO. |
| **Reference Image Too Large** | Base64 exceeds API limit | Resize image to max 1024px on longest side before encoding. |
| **FFmpeg Error** | Any FFmpeg command fails | Re-encode clips through normalise step. If concat fails, use filter-based concat. |

---

---

# TECHNICAL REFERENCE

### VeO 3.1 Capabilities

| Capability | Detail |
|------------|--------|
| Native audio | Generates audio alongside video |
| Text in video | Cannot generate readable text — use FFmpeg or post-production |
| Duration at 1080p | 8 seconds only |
| Aspect ratios | 16:9 and 9:16 |
| Generation time | 2-5 minutes typical |
| Storage | 48 hours — download immediately |
| Reference images | Up to 3 per call. Best for person/style consistency. Requires durationSeconds: "8" |
| personGeneration | Use "allow_adult" for all people-related content |

### Web Video Best Practices

| Format | Use Case | Typical Size |
|--------|----------|-------------|
| MP4 (H.264) | Universal fallback | ~1.5 MB/s at 10Mbps |
| WebM (VP9) | Primary web format | ~0.5 MB/s at 2Mbps |
| Mobile MP4 | Low-bandwidth | ~0.5 MB/s at 4Mbps at 540p |

For website background videos:
- Keep total file size under 5MB for hero loops
- Use `preload="auto"` for above-fold, `preload="none"` for below
- Always include poster image for instant visual feedback
- Test on slow connections (3G simulation)

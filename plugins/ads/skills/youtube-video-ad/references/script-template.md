# YouTube Video Ad Script

<!-- ============================================================
     HEADER BLOCK
     Fill in all fields before beginning scene development.
     Runtime, Goal, and Target Audience inform every creative
     decision downstream — lock these in first.
     ============================================================ -->

| Field | Value |
|-------|-------|
| Client | {CLIENT_NAME} |
| Campaign | {CAMPAIGN_NAME} |
| Runtime | {RUNTIME}s |
| Platform | YouTube In-Stream (Skippable) |
| Goal | {CAMPAIGN_GOAL} |
| Target Audience | {TARGET_AUDIENCE} |
| Production | AI-generated (VeO 3.1 + ElevenLabs + FFmpeg) |
| Date | {DATE} |
| Version | {VERSION} |

---

## Global Visual Direction

<!-- ============================================================
     GLOBAL VISUAL DIRECTION
     These style parameters act as a PREFIX to every VeO prompt
     in this script. Keeping them consistent is what makes a
     multi-clip ad feel like a single, coherent piece of film
     rather than a sequence of unrelated clips.

     Copy the style block into each VeO prompt verbatim, then
     append the scene-specific action and framing details.
     ============================================================ -->

**Style**: {VISUAL_STYLE}
<!-- e.g. "Cinematic photorealistic, natural lighting, shallow depth of field" -->

**Colour Palette**: {BRAND_COLOURS} — {TONE_DESCRIPTION}
<!-- e.g. "Navy and white — cool tones, high contrast, clean and trustworthy" -->

**Setting**: {REGION}-specific {SETTING_TYPE}, {SETTING_DETAIL}
<!-- e.g. "East of England residential environments, Victorian terraced homes and 1960s semis" -->

**Camera Conventions**: {CAMERA_MOVEMENT}, {FRAMING}, {LENS_EQUIVALENT}
<!-- e.g. "Steadicam movement, eye-level framing, 35mm lens equivalent" -->

**Lighting**: {LIGHTING_APPROACH}
<!-- e.g. "Golden hour exterior, practical interior lighting — no artificial studio look" -->

**Consistency Notes**: All scenes feature {CONSISTENT_ELEMENTS}
<!-- e.g. "Same male technician in navy branded uniform; NOVA logo visible on van in outdoor scenes" -->

**Global Negative Prompt**: {GLOBAL_NEGATIVE_PROMPT}
<!-- e.g. "cartoon, anime, CGI, stock photo look, lens flare, text, watermarks, distorted faces" -->

---

## Audio Direction

<!-- ============================================================
     AUDIO DIRECTION
     Defines the audio stack for the entire ad.
     VeO generates ambient/SFX audio natively with each clip —
     treat this as a textural bed, not the primary signal.
     VO is king. Everything else sits underneath it.
     ============================================================ -->

### VeO Native Audio
- **Approach**: Retain VeO-generated ambient audio on all clips
- **Role**: Textural bed — environment, SFX, atmosphere
- **Mix Level**: Lower to **-15 dB** relative to VO track in post
- **Notes**: {VEO_AUDIO_NOTES}
<!-- e.g. "Boiler ignition sound in Scene 2 is intentional — keep. Wind on exterior clips — acceptable." -->

### Voiceover (ElevenLabs)
- **Voice ID**: {ELEVENLABS_VOICE_ID}
<!-- e.g. "Adam" or specific cloned voice ID from ElevenLabs dashboard -->
- **Model**: eleven_multilingual_v2 (or eleven_monolingual_v1 for UK English purity)
- **Stability**: {STABILITY}
<!-- 0.0–1.0. Higher = more consistent, less expressive. Recommended 0.45–0.65 for ad VO. -->
- **Similarity Boost**: {SIMILARITY_BOOST}
<!-- 0.0–1.0. Higher = closer to source voice. Recommended 0.75–0.85. -->
- **Style**: {STYLE_EXAGGERATION}
<!-- 0.0–1.0. Higher = more dramatic. Recommended 0.2–0.4 for professional tone. -->
- **Speaker Boost**: {TRUE/FALSE}
- **Output Format**: mp3_44100_128 (or higher if available)
- **Tone**: {DESIRED_TONE}
<!-- e.g. "Warm, authoritative, conversational — not salesy, not robotic" -->

### Audio Mixing Strategy
```
Track 1 (Primary):    ElevenLabs VO          — 0 dB (reference)
Track 2 (Bed):        VeO ambient/SFX        — -15 dB
Track 3 (Optional):   Background music       — -20 dB
```
- VO should be intelligible at all times — never duck it
- Fade VeO audio in over 0.3s at scene start to avoid hard cuts in ambient sound
- Final mix target: **-14 LUFS** (YouTube normalises to -14 LUFS; hitting this avoids pumping)

---

## Text Overlay Guide

<!-- ============================================================
     TEXT OVERLAY GUIDE
     VeO cannot reliably generate readable text in clips.
     All text overlays are added in post-production.
     Define rules here and apply them consistently across all
     scenes. Inconsistent typography kills brand credibility.
     ============================================================ -->

### Typography
| Property | Value |
|----------|-------|
| Primary Font | {PRIMARY_FONT} |
| Secondary Font | {SECONDARY_FONT} |
| Headline Size | {HEADLINE_SIZE}px (at 1080p) |
| Body/Caption Size | {BODY_SIZE}px (at 1080p) |
| Weight | {FONT_WEIGHT} |
| Letter Spacing | {LETTER_SPACING} |

<!-- e.g. Primary: "Inter" or "Montserrat". Headline: 72px. Body: 48px. Weight: 700 for headlines. -->

### Animation Style
- **Entrance**: {ENTRANCE_ANIMATION}
<!-- e.g. "Fade-in over 0.3s" or "Slide up 20px + fade-in over 0.4s" -->
- **Hold**: Text holds for duration of scene (or until next overlay)
- **Exit**: {EXIT_ANIMATION}
<!-- e.g. "Fade-out over 0.2s" or "No exit — cut with scene" -->
- **Easing**: ease-out on entrance, ease-in on exit

### Timing Rules
- Text appears **{TEXT_DELAY}s** after scene cut (allows viewer to register the visual first)
- Text holds for a minimum of **{MIN_HOLD}s** (readability requirement)
- Never hold text past the scene end — exit before hard cut

### Colour and Positioning
| Use Case | Colour | Position |
|----------|--------|----------|
| Headline | {HEADLINE_COLOUR} | {HEADLINE_POSITION} |
| Supporting text | {SUPPORTING_COLOUR} | {SUPPORTING_POSITION} |
| CTA / End card | {CTA_COLOUR} | {CTA_POSITION} |
| Lower-third label | {LOWER_THIRD_COLOUR} | Bottom-left, 80px from edge |

<!-- e.g. Headline: #FFFFFF on semi-transparent navy bar. CTA: brand colour on solid button shape. -->

### Safe Zones
- Keep all text within the **10% safe zone** from frame edges (192px left/right, 108px top/bottom at 1080p)
- YouTube UI overlays appear at bottom — keep critical text above 80% vertical height

### Recommended Tools
- **Primary**: CapCut (fast, template-based, good for quick iteration)
- **Professional**: DaVinci Resolve (full control, colour grading, audio mixing)
- **FFmpeg**: For programmatic text burn-in if templating at scale

---

## Scene Breakdown

<!-- ============================================================
     SCENE BREAKDOWN
     One block per scene. Scenes should chain logically —
     each one advancing the narrative or emotional arc.

     Standard structure for a skippable YouTube ad:
       0–5s    Hook (must work before skip button appears)
       5–15s   Problem / Empathy
       15–25s  Solution / Credibility
       25–{N}s CTA / Close

     Duplicate the scene block below for each scene required.
     ============================================================ -->

---

### Scene 1: {SCENE_PURPOSE}

<!-- What job does this scene do in the ad? e.g. "Hook — capture attention before skip" -->

**Timing**: {START}s – {END}s ({DURATION}s)

#### VeO Prompt

> {GLOBAL_STYLE_PREFIX} — {SCENE_SPECIFIC_PROMPT}

<!-- Structure your prompt as:
     SUBJECT + ACTION + STYLE + CAMERA + COMPOSITION + LENS + AMBIANCE + AUDIO CUE

     Example:
     "Cinematic photorealistic, natural lighting, shallow depth of field.
      A middle-aged homeowner in a cold kitchen, breath visible, staring at
      a non-functional boiler on the wall. She wraps her arms around herself.
      Steadicam slow push-in from mid-shot to close-up on her worried expression.
      35mm equivalent. Overcast morning light through frosted window.
      Ambient: quiet house, distant wind, faint radiator click."
-->

#### VeO Parameters

| Parameter | Value |
|-----------|-------|
| Resolution | 1080p |
| Aspect Ratio | 16:9 |
| Duration | {CLIP_DURATION}s |
| Person Generation | allow_adult |
| Negative Prompt | {SCENE_NEGATIVE_PROMPT} |
| Seed | {SEED} |
| Reference Images | {YES/NO — specify source if YES, e.g. "from Scene 2 for character continuity"} |

<!-- Seed: Note the seed of any clip you want to iterate on. Locking seed + tweaking prompt
     gives controlled variation. Leave as {SEED} until first generation, then record the winner. -->

#### Variations

Generate **{N}** variations. Select based on: {SELECTION_CRITERIA}

<!-- e.g. Generate 3 variations. Select based on: most natural facial expression, clearest
     emotional read, best camera movement smoothness. -->

#### Voiceover

> "{VO_TEXT}"
>
> *Pacing: {PACING_NOTES}*

<!-- e.g. VO: "Is your boiler letting you down this winter?"
     Pacing: Slow, deliberate. Pause after "down". Warm but serious tone. -->

#### Text Overlays

| Time | Text | Style | Position |
|------|------|-------|----------|
| {TIME}s | {TEXT} | {STYLE} | {POSITION} |

<!-- e.g.
| 1.0s | "Sound familiar?" | Headline, white, fade-in 0.3s | Centre frame |
| 3.5s | {empty — clear before cut} | — | — |
-->

#### Transition to Next Scene

{TRANSITION_TYPE}: {DETAILS}

<!-- Options:
     Hard cut — instantaneous, high energy
     Match cut — cut on action or compositional similarity (most cinematic)
     J-cut — next scene's audio starts before video cuts (smooth, professional)
     L-cut — current audio continues over next scene's opening (narrative flow)
     Dissolve (0.3s) — softer, emotional moments
     Avoid wipes or star wipes entirely. -->

---

### Scene 2: {SCENE_PURPOSE}

**Timing**: {START}s – {END}s ({DURATION}s)

#### VeO Prompt

> {GLOBAL_STYLE_PREFIX} — {SCENE_SPECIFIC_PROMPT}

#### VeO Parameters

| Parameter | Value |
|-----------|-------|
| Resolution | 1080p |
| Aspect Ratio | 16:9 |
| Duration | {CLIP_DURATION}s |
| Person Generation | allow_adult |
| Negative Prompt | {SCENE_NEGATIVE_PROMPT} |
| Seed | {SEED} |
| Reference Images | {YES/NO} |

#### Variations

Generate **{N}** variations. Select based on: {SELECTION_CRITERIA}

#### Voiceover

> "{VO_TEXT}"
>
> *Pacing: {PACING_NOTES}*

#### Text Overlays

| Time | Text | Style | Position |
|------|------|-------|----------|
| {TIME}s | {TEXT} | {STYLE} | {POSITION} |

#### Transition to Next Scene

{TRANSITION_TYPE}: {DETAILS}

---

### Scene {N}: {SCENE_PURPOSE}

<!-- Duplicate this block for each additional scene. -->

**Timing**: {START}s – {END}s ({DURATION}s)

#### VeO Prompt

> {GLOBAL_STYLE_PREFIX} — {SCENE_SPECIFIC_PROMPT}

#### VeO Parameters

| Parameter | Value |
|-----------|-------|
| Resolution | 1080p |
| Aspect Ratio | 16:9 |
| Duration | {CLIP_DURATION}s |
| Person Generation | allow_adult |
| Negative Prompt | {SCENE_NEGATIVE_PROMPT} |
| Seed | {SEED} |
| Reference Images | {YES/NO} |

#### Variations

Generate **{N}** variations. Select based on: {SELECTION_CRITERIA}

#### Voiceover

> "{VO_TEXT}"
>
> *Pacing: {PACING_NOTES}*

#### Text Overlays

| Time | Text | Style | Position |
|------|------|-------|----------|
| {TIME}s | {TEXT} | {STYLE} | {POSITION} |

#### Transition to Next Scene

{TRANSITION_TYPE}: {DETAILS}

---

## Generation Summary

<!-- ============================================================
     GENERATION SUMMARY
     Single reference table for the whole production run.
     Use this to track what needs generating, how many clips,
     and what you're optimising for in selection.
     Update "Seed (Winner)" column once you've locked clips.
     ============================================================ -->

| Scene | Description | Duration | Clips to Generate | Selection Criteria | Seed (Winner) |
|-------|-------------|----------|-------------------|--------------------|---------------|
| 1 | {DESC} | {DUR}s | {N} variations | {CRITERIA} | — |
| 2 | {DESC} | {DUR}s | {N} variations | {CRITERIA} | — |
| {N} | {DESC} | {DUR}s | {N} variations | {CRITERIA} | — |

**Total clips to generate**: {TOTAL_CLIPS}
**Estimated VeO generation time**: {EST_TIME}
**Expected selects**: {TOTAL_SCENES} clips (one per scene)

---

## Assembly Order

<!-- ============================================================
     ASSEMBLY ORDER
     Maps selected clips into final edit sequence.
     Trim points reference the selected clip's own timeline
     (0s = start of that clip, not the ad timeline).
     Audio column notes which audio tracks are active at each cut.
     ============================================================ -->

| Order | Source | Trim In | Trim Out | Duration | Transition In | Audio |
|-------|--------|---------|----------|----------|---------------|-------|
| 1 | Scene 1 (selected) | 0s | {N}s | {N}s | Hard cut (first scene) | VO + VeO bed |
| 2 | Scene 2 (selected) | {N}s | {N}s | {N}s | {TRANSITION} | VO + VeO bed |
| {N} | Scene {N} (selected) | {N}s | {N}s | {N}s | {TRANSITION} | VO + VeO bed |
| Final | End card / CTA graphic | 0s | {N}s | {N}s | Dissolve 0.3s | VO + music swell |

**Total assembled runtime**: {RUNTIME}s
**VO track start**: 0s (or {N}s if hook scene is silent)
**Music bed start**: {N}s (if applicable)

---

## Export Specifications

<!-- ============================================================
     EXPORT SPECIFICATIONS
     YouTube's recommended specs as of 2025.
     -movflags +faststart moves the MOOV atom to the front of
     the file — critical for fast load on slow connections.
     BT.709 is the correct colour space for web video.
     ============================================================ -->

| Setting | Value |
|---------|-------|
| Resolution | 1920x1080 |
| Frame Rate | {FRAME_RATE}fps |
| Codec | H.264 (libx264) |
| Video Bitrate | 8–12 Mbps |
| Audio Codec | AAC |
| Audio Bitrate | 192 kbps |
| Audio Sample Rate | 44.1 kHz |
| Channels | Stereo |
| Container | MP4 |
| Flags | -movflags +faststart |
| Colour Space | BT.709 |
| Loudness Target | -14 LUFS (YouTube standard) |
| True Peak | -1 dBTP |

### FFmpeg Export Command

```bash
ffmpeg \
  -i {INPUT_FILE} \
  -c:v libx264 \
  -preset slow \
  -crf 18 \
  -b:v 10M \
  -maxrate 12M \
  -bufsize 24M \
  -c:a aac \
  -b:a 192k \
  -ar 44100 \
  -ac 2 \
  -movflags +faststart \
  -color_primaries bt709 \
  -color_trc bt709 \
  -colorspace bt709 \
  -pix_fmt yuv420p \
  {OUTPUT_FILE}.mp4
```

<!-- Replace {INPUT_FILE} with your assembled edit export (ProRes or lossless intermediary).
     Never export to H.264 → re-encode to H.264. Always export a lossless master first,
     then run FFmpeg on that. Generational quality loss in H.264-to-H.264 is significant. -->

### YouTube Upload Checklist

- [ ] Title: {VIDEO_TITLE}
- [ ] Thumbnail: Custom (not auto-generated)
- [ ] Description includes target keywords
- [ ] Tags added
- [ ] Category: {CATEGORY}
- [ ] Language: {LANGUAGE}
- [ ] Subtitles/captions uploaded (SRT file)
- [ ] Ad campaign linked in Google Ads
- [ ] Skippable in-stream format confirmed
- [ ] Target audience and bidding configured in Google Ads

---

<!-- ============================================================
     VERSION HISTORY
     Track changes here so you can roll back to a prior version
     if a new cut underperforms in testing.
     ============================================================ -->

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| v1.0 | {DATE} | Initial draft | {AUTHOR} |
| {VERSION} | {DATE} | {CHANGES} | {AUTHOR} |

# Video Generation Script

<!-- Template for web design video generation -->

| Field | Value |
|-------|-------|
| Project | {PROJECT_NAME} |
| Video | {VIDEO_NAME — e.g., "Homepage Hero Loop", "About Page Brand Story"} |
| Approach | {APPROACH — Ambient Loop / Narrative Sequence / Showcase / Social Clip / Testimonial} |
| Runtime | {RUNTIME}s |
| Aspect Ratio | {ASPECT_RATIO — 16:9 / 9:16 / 1:1} |
| Platform | {PLATFORM — Website / Instagram / YouTube / etc.} |
| Audio | {AUDIO — Silent / Ambient only / Voiceover / Music} |
| Reference Images | {REF_IMAGES — list or "None"} |
| Production | VeO 3.1 + ElevenLabs (if VO) + FFmpeg |
| Date | {DATE} |
| Version | {VERSION} |

---

## Global Visual Direction

**Style**: {VISUAL_STYLE}
**Colour Palette**: {COLOURS} — {TONE}
**Setting**: {SETTING_DETAILS}
**Camera Conventions**: {CAMERA_STYLE}
**Lighting**: {LIGHTING_APPROACH}
**Consistency Notes**: {CONSISTENT_ELEMENTS}
**Global Negative Prompt**: {NEGATIVE_PROMPT}

---

## Audio Direction

### For Silent Videos
- Video will be muted. No audio processing required.
- Strip audio track in final export.

### For Ambient Audio
- Retain VeO-generated audio at full volume.
- No voiceover track.

### For Voiceover Videos
- **Primary**: ElevenLabs {VOICE_NAME}
- **Ambient bed**: VeO native audio at -15dB
- **Tone**: {DESIRED_TONE}

---

## Reference Images

| # | File | Type | Purpose | Used In Scenes |
|---|------|------|---------|---------------|
| 1 | {FILENAME} | Person | {WHO_AND_WHY} | {SCENE_NUMBERS} |
| 2 | {FILENAME} | Location | {WHAT_AND_WHY} | {SCENE_NUMBERS} |

---

## Text Overlay Guide

{If applicable — typography, animation, positioning rules}
{If not applicable: "No text overlays — video used as background/standalone."}

---

## Scene Breakdown

### Scene 1: {PURPOSE}

**Timing**: {START}s – {END}s ({DURATION}s)

#### VeO Prompt

> {GLOBAL_STYLE_PREFIX} — {SCENE_PROMPT}

#### Reference Images

{List which reference images to include in this API call, or "None — use auto-generated reference frame only"}

#### VeO Parameters

| Parameter | Value |
|-----------|-------|
| Resolution | 1080p |
| Aspect Ratio | {RATIO} |
| Duration | 8s |
| Person Generation | allow_adult |
| Negative Prompt | {NEGATIVE} |
| Seed | 42 |

#### Variations

Generate **{N}** variations. Select based on: {CRITERIA}

#### Voiceover (if applicable)

> "{VO_TEXT}"
> *Pacing: {NOTES}*

#### Text Overlays (if applicable)

| Time | Text | Style | Position |
|------|------|-------|----------|
| {TIME} | {TEXT} | {STYLE} | {POSITION} |

#### Transition

{TRANSITION_TYPE}

#### Looping Notes (for ambient loops)

{How this clip connects for seamless looping, or "N/A"}

---

### Scene {N}: {PURPOSE}

<!-- Duplicate scene block for each additional scene -->

---

## Generation Summary

| Scene | Label | Duration | Variations | Ref Images | Key Challenge |
|-------|-------|----------|------------|------------|---------------|
| 1 | {LABEL} | {DUR}s | {N} | {Y/N} | {CHALLENGE} |

**Total clips**: {N}
**Total runtime**: {N}s

---

## Assembly Order

| Order | Source | Duration | Transition | Audio |
|-------|--------|----------|------------|-------|
| 1 | Scene 1 | {N}s | First scene | {AUDIO_TYPE} |

---

## Export Specifications

### Primary Export
| Setting | Value |
|---------|-------|
| Resolution | 1920×1080 |
| Codec | H.264 (libx264) |
| Bitrate | 8-12 Mbps |
| Audio | AAC 192kbps / None |
| Container | MP4 |
| Flags | -movflags +faststart |

### Web Exports (for website background videos)
| Format | Codec | Bitrate | Resolution | Audio |
|--------|-------|---------|------------|-------|
| WebM | VP9 | 2 Mbps | 1920×1080 | None |
| Mobile MP4 | H.264 | 4 Mbps | 960×540 | None |
| Poster | JPEG | — | 1920×1080 | — |

### HTML Implementation

```html
<video autoplay muted loop playsinline poster="poster.jpg">
  <source src="video.webm" type="video/webm">
  <source src="video.mp4" type="video/mp4">
</video>
```

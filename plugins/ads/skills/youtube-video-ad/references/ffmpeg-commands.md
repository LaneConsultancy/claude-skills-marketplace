# FFmpeg Command Reference — YouTube Video Ad Assembly

A comprehensive reference for assembling YouTube video ads from VeO-generated clips. Every command is copy-pasteable. All parameters are explained.

---

## Table of Contents

1. [Frame Extraction (QC Previews)](#1-frame-extraction-qc-previews)
2. [Clip Trimming](#2-clip-trimming)
3. [Resolution and Format Normalization](#3-resolution-and-format-normalization)
4. [Colour Normalization](#4-colour-normalization)
5. [Concatenation](#5-concatenation)
6. [Transitions (xfade)](#6-transitions-xfade)
7. [Audio Operations](#7-audio-operations)
8. [CTA Card Generation](#8-cta-card--dark-background-generation)
9. [Text Overlays](#9-text-overlays-ffmpeg-drawtext)
10. [Final Export (YouTube-Optimized)](#10-final-export-youtube-optimized)
11. [Inspection Commands](#11-useful-inspection-commands)
12. [Complete Assembly Pipeline Example](#12-complete-assembly-pipeline-example)

---

## 1. Frame Extraction (QC Previews)

Use these commands to extract still frames for quality checking before committing to a full encode.

### Extract a single frame at a specific timestamp

```bash
ffmpeg -i input.mp4 -ss 2 -vframes 1 preview.png
```

### Extract a frame at the midpoint (for reference images)

```bash
# Get duration first
DURATION=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 input.mp4)
MIDPOINT=$(echo "$DURATION / 2" | bc -l)
ffmpeg -i input.mp4 -ss $MIDPOINT -vframes 1 reference.png
```

### Extract multiple frames (start, middle, end) for final QC

The `select` filter uses frame index `n`. Adjust the frame numbers to match your clip's frame count (assumes 30fps, 5s = 149 frames).

```bash
ffmpeg -i input.mp4 -vf "select='eq(n\,0)+eq(n\,75)+eq(n\,149)'" -vsync 0 frame_%03d.png
```

**Note**: For a different clip length, calculate the last frame as `(duration_in_seconds * fps) - 1`. For a 4.5s clip at 30fps: `(4.5 * 30) - 1 = 134`.

---

## 2. Clip Trimming

### Trim to exact duration from the start (stream copy — fastest, no re-encode)

```bash
ffmpeg -i input.mp4 -t 4.5 -c copy trimmed.mp4
```

**Caveat**: `-c copy` with `-t` may not cut exactly on a non-keyframe. Use the re-encode version below when frame accuracy matters.

### Trim with specific start and end points

```bash
ffmpeg -i input.mp4 -ss 1.5 -to 5.0 -c:v libx264 -c:a aac trimmed.mp4
```

### Trim to exact duration (re-encode — frame-accurate)

Use this when you need a precise cut and the stream copy method leaves extra frames.

```bash
ffmpeg -i input.mp4 -ss 0 -t 4.5 -c:v libx264 -preset medium -crf 18 -c:a aac -b:a 192k trimmed.mp4
```

---

## 3. Resolution and Format Normalization

**This step is required before concatenation** if your VeO clips have mismatched resolutions, frame rates, or codecs. Run all clips through normalization before assembling.

### Scale to 1920x1080 with letterbox/pillarbox padding (preserves aspect ratio)

The safest option — never distorts the image. Black bars are added where needed.

```bash
ffmpeg -i input.mp4 \
  -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:black" \
  -c:v libx264 -preset medium -crf 18 \
  -c:a aac -b:a 192k \
  normalized.mp4
```

### Scale to exact 1920x1080 (stretch — use cautiously)

Only use this if the source aspect ratio already matches 16:9.

```bash
ffmpeg -i input.mp4 \
  -vf "scale=1920:1080" \
  -c:v libx264 -preset medium -crf 18 \
  -c:a aac -b:a 192k \
  scaled.mp4
```

### Full normalization — codec, resolution, frame rate, audio (recommended batch step)

Run every clip through this before concatenation to guarantee identical streams.

```bash
ffmpeg -i input.mp4 \
  -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p -r 30 -s 1920x1080 \
  -c:a aac -b:a 192k -ar 48000 -ac 2 \
  normalized.mp4
```

| Parameter | Value | Reason |
|-----------|-------|--------|
| `-pix_fmt yuv420p` | 4:2:0 chroma | Required for broad compatibility |
| `-r 30` | 30fps | YouTube standard; normalizes variable-rate VeO clips |
| `-s 1920x1080` | 1080p | Target resolution |
| `-ar 48000` | 48kHz sample rate | YouTube audio standard |
| `-ac 2` | Stereo | Standard for ads |

---

## 4. Colour Normalization

### Apply BT.709 colour space (YouTube standard)

VeO clips may use different colour primaries. This forces BT.709 throughout.

```bash
ffmpeg -i input.mp4 \
  -vf "colorspace=all=bt709:iall=bt709" \
  -c:v libx264 -preset medium -crf 18 \
  -c:a aac \
  output.mp4
```

### Basic colour grading — warm look for home/comfort ads

Slightly brighter, slightly warmer. Suitable for boiler/home heating ads.

```bash
ffmpeg -i input.mp4 \
  -vf "eq=brightness=0.02:contrast=1.05:saturation=1.1,colorbalance=rs=0.05:gs=0.02:bs=-0.03" \
  -c:v libx264 -crf 18 \
  -c:a aac \
  output.mp4
```

**Parameter guide:**
- `brightness=0.02` — Lifts the overall exposure slightly
- `contrast=1.05` — Adds a small amount of punch
- `saturation=1.1` — Makes colours slightly more vivid
- `colorbalance rs=0.05` — Pushes shadows toward warm red
- `bs=-0.03` — Reduces blue in shadows (warmer feel)

---

## 5. Concatenation

### Hard cut concatenation — concat demuxer (fastest, no re-encode)

**Step 1**: Create `concat_list.txt` with your clip order:

```
file 'scene-1-selected.mp4'
file 'scene-2-selected.mp4'
file 'scene-3-selected.mp4'
```

**Step 2**: Concatenate:

```bash
ffmpeg -f concat -safe 0 -i concat_list.txt -c copy output.mp4
```

**IMPORTANT**: All clips MUST have identical codecs, resolution, frame rate, pixel format, and audio settings for `-c copy` to work without corruption. Run the normalization step first if in any doubt.

### Hard cut concatenation — filter-based (re-encodes, handles mismatched formats)

Use this as a fallback if the concat demuxer produces glitches or if clips have different formats. Slower, but more forgiving.

```bash
ffmpeg -i scene1.mp4 -i scene2.mp4 -i scene3.mp4 \
  -filter_complex "[0:v][0:a][1:v][1:a][2:v][2:a]concat=n=3:v=1:a=1[outv][outa]" \
  -map "[outv]" -map "[outa]" \
  -c:v libx264 -preset medium -crf 18 \
  -c:a aac -b:a 192k \
  output.mp4
```

Scale `n=3` to match the number of input clips. Add more `-i` inputs and extend the filter chain accordingly.

---

## 6. Transitions (xfade)

### Cross-dissolve between two clips

`offset` = duration of clip 1 minus transition duration. If clip1 is 4.5s and transition is 0.5s, offset = 4.0.

```bash
ffmpeg -i clip1.mp4 -i clip2.mp4 \
  -filter_complex \
    "[0:v][1:v]xfade=transition=fade:duration=0.5:offset=4.0[outv];
     [0:a][1:a]acrossfade=d=0.5[outa]" \
  -map "[outv]" -map "[outa]" \
  -c:v libx264 -crf 18 \
  -c:a aac \
  output.mp4
```

### Chain multiple xfade transitions across 3 clips

For the second transition, `offset` = (clip1 duration + clip2 duration - transition1 duration - transition2 duration).

Example: clip1=4.5s, clip2=5.0s, both transitions=0.5s → first offset=4.0, second offset=8.5.

```bash
ffmpeg -i clip1.mp4 -i clip2.mp4 -i clip3.mp4 \
  -filter_complex \
    "[0:v][1:v]xfade=transition=fade:duration=0.5:offset=4.0[v01];
     [v01][2:v]xfade=transition=fade:duration=0.5:offset=8.5[outv];
     [0:a][1:a]acrossfade=d=0.5[a01];
     [a01][2:a]acrossfade=d=0.5[outa]" \
  -map "[outv]" -map "[outa]" \
  -c:v libx264 -crf 18 \
  -c:a aac \
  output.mp4
```

### Available xfade transition types

| Transition | Effect | When to use |
|------------|--------|-------------|
| `fade` | Standard cross-dissolve | Default — use for 90% of cuts |
| `wipeleft` / `wiperight` | Directional wipe | Scene changes with motion direction |
| `slideright` / `slideleft` | Slide transition | Energetic cuts, before/after reveals |
| `smoothup` / `smoothdown` | Smooth vertical blend | Establishing shot to detail |
| `circlecrop` | Circular reveal | Punchy moment reveals |
| `distance` | Colour-distance blend | Stylistic, use sparingly |

**Recommendation**: Use `fade` for all transitions in professional ads. Transition duration of 0.3–0.5s. Longer transitions feel indecisive.

---

## 7. Audio Operations

### Extract audio from video

```bash
ffmpeg -i input.mp4 -vn -c:a aac -b:a 192k audio.mp3
```

### Generate silence (for gaps between VO segments)

```bash
ffmpeg -f lavfi -i anullsrc=r=48000:cl=stereo -t 1.5 silence.mp3
```

Change `-t 1.5` to whatever duration you need in seconds.

### Concatenate audio files (VO segments + silence gaps)

**Step 1**: Create `audio_list.txt`:

```
file 'vo-scene1.mp3'
file 'silence-1.5s.mp3'
file 'vo-scene2.mp3'
file 'silence-0.5s.mp3'
file 'vo-scene3.mp3'
```

**Step 2**: Concatenate:

```bash
ffmpeg -f concat -safe 0 -i audio_list.txt -c copy full-vo.mp3
```

### Mix VeO native audio with ElevenLabs VO

VeO audio is lowered to -15dB as an ambient bed. ElevenLabs VO sits on top as the primary track. The `duration=first` flag means the output matches the video duration.

```bash
ffmpeg -i video_with_veo_audio.mp4 -i elevenlabs-vo.mp3 \
  -filter_complex \
    "[0:a]volume=-15dB[bg];
     [bg][1:a]amix=inputs=2:duration=first:dropout_transition=2[outa]" \
  -map "0:v" -map "[outa]" \
  -c:v copy -c:a aac -b:a 192k \
  output.mp4
```

### Audio ducking (automatically lower VeO audio when VO is speaking)

More sophisticated than a fixed volume reduction. Uses sidechain compression so the ambient audio ducks when the VO is present and recovers when it pauses.

```bash
ffmpeg -i video_with_veo_audio.mp4 -i elevenlabs-vo.mp3 \
  -filter_complex \
    "[1:a]asplit=2[vo][vosc];
     [vosc]sidechaincompress=threshold=0.01:ratio=10:attack=200:release=1000[compressed];
     [0:a][compressed]sidechaincompress=threshold=0.01:ratio=6:attack=50:release=500[bg];
     [bg][vo]amix=inputs=2:duration=first[outa]" \
  -map "0:v" -map "[outa]" \
  -c:v copy -c:a aac -b:a 192k \
  output.mp4
```

**Parameter guide:**
- `threshold=0.01` — Triggers compression when VO signal exceeds this level
- `ratio=6` — Reduces ambient audio to 1/6th of its level when ducking
- `attack=50` — 50ms to start ducking (prevents abrupt cuts)
- `release=500` — 500ms to restore ambient audio after VO stops

### Replace video audio entirely (ElevenLabs VO only — no ambient)

Use this when VeO ambient audio is distracting or when you have a music bed from a separate source.

```bash
ffmpeg -i video.mp4 -i elevenlabs-vo.mp3 \
  -map 0:v -map 1:a \
  -c:v copy -c:a aac -b:a 192k -shortest \
  output.mp4
```

---

## 8. CTA Card / Dark Background Generation

### Solid colour background with duration

Generates a 4-second dark navy background clip with no content. Use as a base for the CTA card.

```bash
ffmpeg -f lavfi -i "color=c=0x1a1a2e:s=1920x1080:d=4" \
  -c:v libx264 -pix_fmt yuv420p \
  cta-bg.mp4
```

Change `0x1a1a2e` to any hex colour. `d=4` sets duration in seconds.

### Dark background with text overlay (automated CTA)

Generates a CTA card with headline and URL. Requires a font file path.

```bash
ffmpeg -f lavfi -i "color=c=0x1a1a2e:s=1920x1080:d=4" \
  -vf "drawtext=text='Get Your Free Quote':fontsize=72:fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2-50:fontfile=/path/to/font.ttf,\
       drawtext=text='UKboilers.org':fontsize=96:fontcolor=0x4FC3F7:x=(w-text_w)/2:y=(h-text_h)/2+50:fontfile=/path/to/font.ttf" \
  -c:v libx264 -pix_fmt yuv420p \
  cta-card.mp4
```

**Note on fonts**: Replace `/path/to/font.ttf` with an absolute path to a `.ttf` file. On macOS, system fonts are in `/System/Library/Fonts/` and `/Library/Fonts/`. For production use, bundle a specific font with the project.

### Add silent audio to a video-only clip (required before concatenation)

If a generated clip has no audio stream, it will break the concat pipeline. This adds a silent audio track.

```bash
ffmpeg -i video-only.mp4 \
  -f lavfi -i anullsrc=r=48000:cl=stereo \
  -c:v copy -c:a aac -shortest \
  output-with-audio.mp4
```

---

## 9. Text Overlays (FFmpeg drawtext)

**Important note on text overlays**: FFmpeg drawtext is functional but limited — no motion graphics, no proper font rendering on all systems, no easy animation curves. For production-quality text animation, use CapCut or DaVinci Resolve. The recommended workflow is to assemble the video without text overlays, then add them in post. These commands are provided for automated pipelines only.

### Basic text overlay with time window

Text appears at t=2s and disappears at t=5s.

```bash
ffmpeg -i input.mp4 \
  -vf "drawtext=text='Save £840/year':fontsize=64:fontcolor=white:borderw=3:bordercolor=black:x=(w-text_w)/2:y=h-100:enable='between(t,2,5)'" \
  -c:v libx264 -crf 18 -c:a copy \
  output.mp4
```

### Text with fade-in animation

Text fades in over 0.25 seconds starting at t=2s.

```bash
ffmpeg -i input.mp4 \
  -vf "drawtext=text='Save £840/year':fontsize=64:fontcolor=white@%{eif\\:min(1,(t-2)*4)\\:d}:x=(w-text_w)/2:y=h-100:enable='gte(t,2)'" \
  -c:v libx264 -crf 18 -c:a copy \
  output.mp4
```

### Multiple text overlays on the same clip

Comma-separate each `drawtext` filter.

```bash
ffmpeg -i input.mp4 \
  -vf "drawtext=text='Line 1':fontsize=48:fontcolor=white:x=(w-text_w)/2:y=h*0.7:enable='between(t,1,4)',\
       drawtext=text='Line 2':fontsize=36:fontcolor=0xCCCCCC:x=(w-text_w)/2:y=h*0.8:enable='between(t,2,5)'" \
  -c:v libx264 -crf 18 -c:a copy \
  output.mp4
```

### Drawtext alignment reference

| Position | x expression | y expression |
|----------|-------------|-------------|
| Centre horizontal | `(w-text_w)/2` | — |
| Left margin | `80` | — |
| Right-align | `w-text_w-80` | — |
| Vertical centre | — | `(h-text_h)/2` |
| Lower third | — | `h*0.75` |
| Bottom bar | — | `h-100` |
| Top bar | — | `60` |

---

## 10. Final Export (YouTube-Optimized)

### Standard YouTube upload settings

```bash
ffmpeg -i assembled.mp4 \
  -c:v libx264 -preset slow -crf 16 -profile:v high -level:v 4.1 \
  -pix_fmt yuv420p -r 30 \
  -b:v 10M -maxrate 12M -bufsize 20M \
  -c:a aac -b:a 192k -ar 48000 -ac 2 \
  -movflags +faststart \
  -metadata title="Ad Title" \
  final-output.mp4
```

### Export parameters explained

| Parameter | Value | Why |
|-----------|-------|-----|
| `-preset slow` | Slower encode, better quality | Worth the extra time for the final output — only run once |
| `-crf 16` | High quality (scale: 0–51, lower = better) | YouTube re-encodes on upload; start higher than you think you need |
| `-profile:v high` | H.264 High Profile | Best quality + compatibility combination |
| `-level:v 4.1` | H.264 Level 4.1 | Supports 1080p30; widely supported by players |
| `-b:v 10M` | Target 10 Mbps video | YouTube recommended bitrate for 1080p30 |
| `-maxrate 12M` | Max 12 Mbps | Caps bitrate spikes on fast-motion scenes |
| `-bufsize 20M` | 2x maxrate buffer | Standard HLS/streaming buffer size recommendation |
| `-movflags +faststart` | Move moov atom to file start | Required for web streaming; allows playback before full download |
| `-ar 48000` | 48kHz audio | YouTube standard; mismatches cause audio drift |
| `-ac 2` | Stereo | Standard for ads; YouTube does not require 5.1 |

---

## 11. Useful Inspection Commands

Run these before and after assembly to verify clip properties and catch issues early.

### Get video stream properties

```bash
ffprobe -v error \
  -select_streams v:0 \
  -show_entries stream=codec_name,width,height,r_frame_rate,duration \
  -of default=noprint_wrappers=1 \
  input.mp4
```

### Get audio stream properties

```bash
ffprobe -v error \
  -select_streams a:0 \
  -show_entries stream=codec_name,sample_rate,channels,duration \
  -of default=noprint_wrappers=1 \
  input.mp4
```

### Get file duration (numeric output for scripting)

```bash
ffprobe -v error \
  -show_entries format=duration \
  -of default=noprint_wrappers=1:nokey=1 \
  input.mp4
```

### Get file size in human-readable format

```bash
du -sh output.mp4
```

### Full diagnostic — all streams and format info

```bash
ffprobe -v quiet -print_format json -show_format -show_streams input.mp4
```

### Check if two clips are compatible for stream-copy concatenation

Run this on both clips and compare the output. Every value must match for `-c copy` to be safe.

```bash
ffprobe -v error \
  -select_streams v:0 \
  -show_entries stream=codec_name,width,height,r_frame_rate,pix_fmt \
  -select_streams a:0 \
  -show_entries stream=codec_name,sample_rate,channels,bit_rate \
  -of default=noprint_wrappers=1 \
  input.mp4
```

---

## 12. Complete Assembly Pipeline Example

A full pipeline for a 27-second ad with 5 scenes. Adapt durations and file names to match the script spec from the skill.

```bash
#!/bin/bash
# Complete YouTube Ad Assembly Pipeline
# Adjust scene durations and file names to match your script

set -e  # Exit on any error

# --- Step 1: Normalize all selected clips ---
# Ensures identical codec, resolution, frame rate, and audio settings
echo "Step 1: Normalizing clips..."
for i in 1 2 3 4 5; do
  ffmpeg -i "selected/scene-${i}.mp4" \
    -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p -r 30 -s 1920x1080 \
    -c:a aac -b:a 192k -ar 48000 -ac 2 \
    "selected/scene-${i}-norm.mp4"
done

# --- Step 2: Trim clips to scene durations ---
# Durations come from the script spec
echo "Step 2: Trimming clips to duration..."
ffmpeg -i selected/scene-1-norm.mp4 -t 5.0 -c copy selected/scene-1-trim.mp4
ffmpeg -i selected/scene-2-norm.mp4 -t 5.0 -c copy selected/scene-2-trim.mp4
ffmpeg -i selected/scene-3-norm.mp4 -t 8.0 -c copy selected/scene-3-trim.mp4
ffmpeg -i selected/scene-4-norm.mp4 -t 5.0 -c copy selected/scene-4-trim.mp4
ffmpeg -i selected/scene-5-norm.mp4 -t 4.0 -c copy selected/scene-5-trim.mp4

# --- Step 3: Generate CTA card ---
# Dark navy background with silent audio track (required for concat)
echo "Step 3: Generating CTA card..."
ffmpeg -f lavfi -i "color=c=0x1a1a2e:s=1920x1080:d=4" \
  -f lavfi -i anullsrc=r=48000:cl=stereo \
  -c:v libx264 -pix_fmt yuv420p -c:a aac -shortest \
  cta-card.mp4

# --- Step 4: Create concat list ---
echo "Step 4: Building concat list..."
cat > concat_list.txt << 'EOF'
file 'selected/scene-1-trim.mp4'
file 'selected/scene-2-trim.mp4'
file 'selected/scene-3-trim.mp4'
file 'selected/scene-4-trim.mp4'
file 'selected/scene-5-trim.mp4'
file 'cta-card.mp4'
EOF

# --- Step 5: Concatenate all clips ---
echo "Step 5: Concatenating clips..."
ffmpeg -f concat -safe 0 -i concat_list.txt -c copy assembled-video.mp4

# --- Step 6: Mix VeO ambient audio with ElevenLabs VO ---
# VeO audio lowered to -15dB as bed; ElevenLabs VO is primary
echo "Step 6: Mixing audio..."
ffmpeg -i assembled-video.mp4 -i audio/full-vo.mp3 \
  -filter_complex \
    "[0:a]volume=-15dB[bg];
     [bg][1:a]amix=inputs=2:duration=first:dropout_transition=2[outa]" \
  -map "0:v" -map "[outa]" \
  -c:v copy -c:a aac -b:a 192k \
  mixed-audio.mp4

# --- Step 7: Final export with YouTube optimization ---
echo "Step 7: Exporting final file..."
mkdir -p output
ffmpeg -i mixed-audio.mp4 \
  -c:v libx264 -preset slow -crf 16 -profile:v high -level:v 4.1 \
  -pix_fmt yuv420p -r 30 \
  -b:v 10M -maxrate 12M -bufsize 20M \
  -c:a aac -b:a 192k -ar 48000 -ac 2 \
  -movflags +faststart \
  output/final-ad.mp4

# --- Step 8: Verify output ---
echo "Step 8: Verifying output..."
echo "Duration and size:"
ffprobe -v error \
  -show_entries format=duration,size \
  -of default=noprint_wrappers=1 \
  output/final-ad.mp4

echo "Video stream:"
ffprobe -v error \
  -select_streams v:0 \
  -show_entries stream=codec_name,width,height,r_frame_rate \
  -of default=noprint_wrappers=1 \
  output/final-ad.mp4

echo "Audio stream:"
ffprobe -v error \
  -select_streams a:0 \
  -show_entries stream=codec_name,sample_rate,channels \
  -of default=noprint_wrappers=1 \
  output/final-ad.mp4

echo ""
echo "Assembly complete. Output: output/final-ad.mp4"
```

### Pipeline notes

- Run `set -e` at the top of any assembly script so it halts on first error rather than silently continuing with broken intermediate files.
- Intermediate files (`-norm.mp4`, `-trim.mp4`) can be deleted after the final output is verified.
- The CTA card always needs a silent audio track added before concatenation — video-only clips break the concat demuxer.
- If `-c copy` in Step 5 produces a file with audio sync issues, replace it with the filter-based concat from Section 5.

---

## Quick Reference — Common Parameter Values

| Setting | Safe default | Notes |
|---------|-------------|-------|
| CRF (intermediate) | 18 | Good quality, reasonable file size |
| CRF (final export) | 16 | Higher quality for YouTube upload |
| Video bitrate | 10M | YouTube recommended for 1080p30 |
| Audio bitrate | 192k | YouTube standard |
| Frame rate | 30 | Normalizes VeO variable-rate output |
| Preset (intermediate) | medium | Balanced speed/quality |
| Preset (final) | slow | Better compression, use for final only |
| Transition duration | 0.3–0.5s | Shorter = more professional feel |
| Ambient audio level | -15dB | Sits under VO without competing |

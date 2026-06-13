# FFmpeg Command Reference — Web Design Video Assembly

A comprehensive reference for assembling web design videos from VeO-generated clips. Every command is copy-pasteable. All parameters are explained.

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
13. [Web-Optimised Exports](#13-web-optimised-exports)
14. [Loop Creation](#14-loop-creation)

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
| `-r 30` | 30fps | Normalizes variable-rate VeO clips |
| `-s 1920x1080` | 1080p | Target resolution |
| `-ar 48000` | 48kHz sample rate | Standard audio sample rate |
| `-ac 2` | Stereo | Standard for web video |

---

## 4. Colour Normalization

### Apply BT.709 colour space (standard for web video)

VeO clips may use different colour primaries. This forces BT.709 throughout.

```bash
ffmpeg -i input.mp4 \
  -vf "colorspace=all=bt709:iall=bt709" \
  -c:v libx264 -preset medium -crf 18 \
  -c:a aac \
  output.mp4
```

### Basic colour grading — warm look for home/comfort content

Slightly brighter, slightly warmer. Suitable for plumbing, home improvement, and interior service content.

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

**Recommendation**: Use `fade` for all transitions in professional web content. Transition duration of 0.3–0.5s. Longer transitions feel indecisive.

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
       drawtext=text='yourdomain.co.uk':fontsize=96:fontcolor=0x4FC3F7:x=(w-text_w)/2:y=(h-text_h)/2+50:fontfile=/path/to/font.ttf" \
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
  -vf "drawtext=text='Book a Free Survey':fontsize=64:fontcolor=white:borderw=3:bordercolor=black:x=(w-text_w)/2:y=h-100:enable='between(t,2,5)'" \
  -c:v libx264 -crf 18 -c:a copy \
  output.mp4
```

### Text with fade-in animation

Text fades in over 0.25 seconds starting at t=2s.

```bash
ffmpeg -i input.mp4 \
  -vf "drawtext=text='Book a Free Survey':fontsize=64:fontcolor=white@%{eif\\:min(1,(t-2)*4)\\:d}:x=(w-text_w)/2:y=h-100:enable='gte(t,2)'" \
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
  -metadata title="Video Title" \
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
| `-ar 48000` | 48kHz audio | Standard; mismatches cause audio drift |
| `-ac 2` | Stereo | Standard for web video |

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

A full pipeline for a multi-scene web video with voiceover. Adapt durations and file names to match the script spec from the skill.

```bash
#!/bin/bash
# Complete Web Video Assembly Pipeline
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

# --- Step 7: Final export with optimization ---
echo "Step 7: Exporting final file..."
mkdir -p output
ffmpeg -i mixed-audio.mp4 \
  -c:v libx264 -preset slow -crf 16 -profile:v high -level:v 4.1 \
  -pix_fmt yuv420p -r 30 \
  -b:v 10M -maxrate 12M -bufsize 20M \
  -c:a aac -b:a 192k -ar 48000 -ac 2 \
  -movflags +faststart \
  output/final-video.mp4

# --- Step 8: Verify output ---
echo "Step 8: Verifying output..."
echo "Duration and size:"
ffprobe -v error \
  -show_entries format=duration,size \
  -of default=noprint_wrappers=1 \
  output/final-video.mp4

echo "Video stream:"
ffprobe -v error \
  -select_streams v:0 \
  -show_entries stream=codec_name,width,height,r_frame_rate \
  -of default=noprint_wrappers=1 \
  output/final-video.mp4

echo "Audio stream:"
ffprobe -v error \
  -select_streams a:0 \
  -show_entries stream=codec_name,sample_rate,channels \
  -of default=noprint_wrappers=1 \
  output/final-video.mp4

echo ""
echo "Assembly complete. Output: output/final-video.mp4"
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
| CRF (final export) | 16 | Higher quality for final output |
| Video bitrate | 10M | Recommended for 1080p30 |
| Audio bitrate | 192k | Standard |
| Frame rate | 30 | Normalizes VeO variable-rate output |
| Preset (intermediate) | medium | Balanced speed/quality |
| Preset (final) | slow | Better compression, use for final only |
| Transition duration | 0.3–0.5s | Shorter = more professional feel |
| Ambient audio level | -15dB | Sits under VO without competing |

---

## 13. Web-Optimised Exports

These commands produce files appropriate for use on websites — hero background videos, about page films, service showcase clips. Web delivery requires smaller file sizes, silent tracks, and modern codec support alongside H.264 fallbacks.

### WebM VP9 export (for website background videos)

WebM VP9 achieves roughly half the file size of H.264 at equivalent quality. Modern browsers prefer it. Always pair with an MP4 fallback in the HTML `<video>` tag.

```bash
ffmpeg -i input.mp4 \
  -c:v libvpx-vp9 \
  -b:v 0 -crf 33 \
  -deadline good -cpu-used 2 \
  -pix_fmt yuv420p \
  -an \
  output.webm
```

**Parameter guide:**
- `-b:v 0 -crf 33` — Constant quality mode. CRF 33 is a good starting point; lower = better quality, larger file. Range: 15–40.
- `-deadline good -cpu-used 2` — Balanced encode speed and quality. Use `best` + `cpu-used 0` for final exports where encode time is not a concern.
- `-an` — Strips audio. Background videos on websites are always muted; carry no audio track at all to reduce file size.

### Mobile-optimised lower bitrate MP4

For users on mobile connections, serve a smaller version of the background video. At 960x540 and 4 Mbps, this loads quickly without looking soft on phone screens.

```bash
ffmpeg -i input.mp4 \
  -c:v libx264 -preset slow -crf 23 \
  -vf "scale=960:540" \
  -pix_fmt yuv420p \
  -an \
  -movflags +faststart \
  output-mobile.mp4
```

**When to use:** Serve this via the HTML `<source media="(max-width: 768px)">` attribute, or use it as the sole source for autoplay hero videos on mobile-first sites where bandwidth is a concern.

### Poster frame extraction

The poster image displays before the video loads and when the video cannot play. Always generate and provide one.

```bash
# Extract the first frame
ffmpeg -i input.mp4 -ss 0 -vframes 1 poster.jpg

# Extract a specific frame (often more representative than frame 0)
ffmpeg -i input.mp4 -ss 2 -vframes 1 poster.jpg

# Extract and resize poster to match a specific video version
ffmpeg -i input.mp4 -ss 2 -vframes 1 -vf "scale=1920:1080" poster-1920.jpg
ffmpeg -i input.mp4 -ss 2 -vframes 1 -vf "scale=960:540" poster-960.jpg
```

**JPEG quality control:** FFmpeg's default JPEG quality is acceptable but not optimal. Add `-q:v 2` for higher quality (scale 1–31, lower = better):

```bash
ffmpeg -i input.mp4 -ss 2 -vframes 1 -q:v 2 poster.jpg
```

### Silent video export (strip audio)

Website background videos must be muted. Some pipelines retain an audio track even when the HTML `muted` attribute is set — browsers on iOS will refuse to autoplay any video with an audio track unless `muted` is set both in the HTML attribute and in the file itself. The safest approach is to strip the audio track entirely from the file.

```bash
ffmpeg -i input.mp4 -c:v copy -an output-silent.mp4
```

If you also need to re-encode (e.g., to change codec or resolution), combine with `-an`:

```bash
ffmpeg -i input.mp4 \
  -c:v libx264 -preset slow -crf 18 \
  -pix_fmt yuv420p \
  -an \
  -movflags +faststart \
  output-silent.mp4
```

### Seamless loop testing (extract first and last frames for comparison)

Before publishing a loop, verify the edit point looks seamless. Extract the first and last frames and compare them visually.

```bash
# Extract first frame
ffmpeg -i input.mp4 -ss 0 -vframes 1 loop-check-first.png

# Extract last frame
# Get duration, subtract one frame (assuming 30fps, so subtract 0.033s)
DURATION=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 input.mp4)
LAST_FRAME=$(echo "$DURATION - 0.033" | bc -l)
ffmpeg -i input.mp4 -ss $LAST_FRAME -vframes 1 loop-check-last.png

echo "Compare loop-check-first.png and loop-check-last.png."
echo "They should look similar in composition, colour, and motion direction."
```

**What to look for when comparing:**
- Camera position continuity — does the pan/drift direction line up naturally?
- Colour and exposure consistency — no sudden brightness or saturation jump
- Moving elements — subjects or objects should not teleport between frames
- Motion blur similarity — fast movement at the cut point will be visible

If the loop edit point is jarring, use a crossfade technique from Section 14 to smooth it.

### Complete web export pipeline (all formats from one source)

```bash
#!/bin/bash
# Generate all web export formats from a single normalised source file
# Run this after finalising the assembled video

set -e

INPUT="assembled-final.mp4"
BASENAME="hero-video"

echo "Generating web exports from: $INPUT"

# Full-resolution WebM for desktop (no audio)
echo "Exporting WebM (desktop)..."
ffmpeg -i "$INPUT" \
  -c:v libvpx-vp9 -b:v 0 -crf 33 -deadline good -cpu-used 2 \
  -pix_fmt yuv420p -an \
  "${BASENAME}-desktop.webm"

# Full-resolution MP4 fallback for desktop (no audio)
echo "Exporting MP4 (desktop)..."
ffmpeg -i "$INPUT" \
  -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p \
  -an -movflags +faststart \
  "${BASENAME}-desktop.mp4"

# Mobile MP4 (scaled down, no audio)
echo "Exporting MP4 (mobile)..."
ffmpeg -i "$INPUT" \
  -c:v libx264 -preset slow -crf 23 -vf "scale=960:540" \
  -pix_fmt yuv420p -an -movflags +faststart \
  "${BASENAME}-mobile.mp4"

# Poster frame (from 2s mark)
echo "Exporting poster frame..."
ffmpeg -i "$INPUT" -ss 2 -vframes 1 -q:v 2 "${BASENAME}-poster.jpg"

echo ""
echo "Web exports complete:"
ls -lh "${BASENAME}"*
```

---

## 14. Loop Creation

Website hero background videos loop continuously. VeO clips rarely loop perfectly out of the box — the start and end frames differ too much for a seamless cycle. These commands smooth the edit point or extend the apparent loop duration.

### Reversing a clip for ping-pong loops

A ping-pong loop plays the clip forward then backward, creating a seamless infinite loop without any crossfade processing. The total loop duration is `2 × clip duration`.

```bash
# Step 1: Create the reversed version
ffmpeg -i input.mp4 -vf "reverse" -af "areverse" reversed.mp4

# Step 2: Concatenate original + reversed for ping-pong
cat > pingpong_list.txt << 'EOF'
file 'input.mp4'
file 'reversed.mp4'
EOF

ffmpeg -f concat -safe 0 -i pingpong_list.txt -c copy pingpong-loop.mp4
```

**When to use:** Works best with slow camera movements (slow pan, slow zoom) where the reversal reads as a natural ebb and flow rather than a mechanical reverse. Avoid with directional lighting changes (e.g., a sun moving across the frame) — the reversal becomes obvious.

**Important:** Ensure both `input.mp4` and `reversed.mp4` have identical codecs, resolution, and frame rate before using `-c copy`. Run the normalization step from Section 3 on the reversed file if in any doubt.

### Crossfading clip end into clip start for smoother loops

This technique blends the last N seconds of the clip into the first N seconds, creating a smooth dissolve at the loop point. The resulting clip is `clip_duration - crossfade_duration` in length and loops seamlessly.

The crossfade duration should be 1–2 seconds for background videos. Longer crossfades look sluggish; shorter ones may still show a visible jump.

```bash
# Example: 8-second clip with a 1.5-second crossfade
# The output will be 6.5 seconds long and loop seamlessly

CLIP_DURATION=8
CROSSFADE_DURATION=1.5
OFFSET=$(echo "$CLIP_DURATION - $CROSSFADE_DURATION" | bc)

ffmpeg -i input.mp4 -i input.mp4 \
  -filter_complex \
    "[0:v][1:v]xfade=transition=fade:duration=${CROSSFADE_DURATION}:offset=${OFFSET}[outv]" \
  -map "[outv]" \
  -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p \
  -an \
  seamless-loop.mp4
```

**How it works:** The filter overlaps two instances of the same clip — the first plays from 0s to its end; the second starts from 0s but is offset so it begins playing at the crossfade point. The dissolve blends the end of the first instance into the start of the second, creating a smooth transition. Because both instances are the same clip, the dissolve is always coherent.

**Verify the result** using the loop check commands from Section 13 to confirm the first and last frames of the output match well.

### Creating a longer loop by repeating a clip N times

When you need a longer looping background (e.g., 30 seconds from a single 8-second clip), repeat the clip N times before exporting. Use a seamless loop as the source input for best results.

```bash
# Repeat a clip 4 times (creates ~32 seconds from an 8-second loop)
# Step 1: Build the concat list
python3 -c "
n = 4
with open('repeat_list.txt', 'w') as f:
    for i in range(n):
        f.write(\"file 'seamless-loop.mp4'\\n\")
print(f'Created repeat_list.txt with {n} repetitions')
"

# Step 2: Concatenate
ffmpeg -f concat -safe 0 -i repeat_list.txt -c copy repeated-loop.mp4
```

**Shell-only version (no Python required):**

```bash
# Repeat 4 times without Python
N=4
INPUT="seamless-loop.mp4"

# Build the concat list using a loop
> repeat_list.txt  # Empty the file first
for i in $(seq 1 $N); do
  echo "file '${INPUT}'" >> repeat_list.txt
done

ffmpeg -f concat -safe 0 -i repeat_list.txt -c copy repeated-loop.mp4
```

**When to use:** Deliver a pre-repeated file when the site's video player does not support seamless looping via the HTML `loop` attribute (uncommon but can happen with certain CMS embed systems). For standard `<video loop>` implementations on modern browsers, a single clean loop is all you need — the browser handles repetition natively.

**File size note:** Repeating N times multiplies the file size by N. For web delivery, keep the source loop short and let the browser loop it rather than delivering a multi-minute video file.

### Slow-motion loop (stretch clip to longer duration)

If a clip is too short for a comfortable hero loop, use frame interpolation to slow it down and increase the apparent duration.

```bash
# Slow down to 50% speed (doubles duration: 8s → 16s)
ffmpeg -i input.mp4 \
  -vf "minterpolate=fps=60:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1,setpts=2.0*PTS" \
  -r 30 \
  -c:v libx264 -preset slow -crf 18 \
  -an \
  slowed-loop.mp4
```

**Parameter guide:**
- `minterpolate=fps=60` — Generates intermediate frames at 60fps before slowing down, producing smoother motion than simply duplicating frames
- `setpts=2.0*PTS` — Doubles the presentation timestamps, halving the playback speed
- `-r 30` — Re-samples back to 30fps for output

**Caveat:** Frame interpolation introduces minor motion artefacts, particularly around subject edges. It works well for slow panning landscape shots but may look unnatural on clips with fast or complex motion. Always preview the output before using on a client site.

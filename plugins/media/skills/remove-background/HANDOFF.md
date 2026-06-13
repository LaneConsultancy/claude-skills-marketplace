# Handoff: Fix Remove Background Skill

## Problem Summary

The `remove-background` skill is broken. When invoked, it hangs for several minutes and then fails with an API error: `"Could not process image"`.

## Root Cause

The skill's implementation truncates the base64 data URL before sending it to the Replicate API. In the failing session, the code used `head -c 100` to read the data URL file, which truncated a ~48KB base64-encoded image down to just 100 characters of garbage data.

The Replicate API then received malformed/incomplete image data and returned a 400 error.

## Evidence from Debug Session

```
# This was the problematic command in the failing session:
head -c 100 /path/to/data_url.txt
# This truncated the 48KB data URL to 100 bytes before API call
```

The API response was:
```json
{"type":"error","error":{"type":"invalid_request_error","message":"Could not process image"}}
```

## Current Skill Location

```
/Users/georgelane/.claude/skills/remove-background/SKILL.md
```

## Recommended Fix

### Option 1: Use Local `rembg` Library (Preferred)

The `rembg` library is now installed locally and works reliably. Update the skill to use it as the primary method:

```python
from rembg import remove

with open(input_path, 'rb') as f:
    input_data = f.read()

output_data = remove(input_data)

with open(output_path, 'wb') as f:
    f.write(output_data)
```

**Dependencies already installed:**
- `rembg`
- `onnxruntime`
- `pillow`

The u2net model is cached at `~/.u2net/u2net.onnx`.

### Option 2: Fix the Replicate API Call

If you want to keep using Replicate:

1. **For small files (< 256KB):** Use data URLs, but ensure the FULL data URL is passed to the API, not truncated
2. **For larger files:** Upload to Replicate Files API first, then use the resulting URL

The correct way to pass a data URL:
```bash
# Create the full data URL
DATA_URL="data:image/png;base64,$(base64 -i "$INPUT_FILE" | tr -d '\n')"

# Pass it directly to the API - DO NOT truncate or preview it
```

## Suggested Updated SKILL.md Structure

```markdown
# Remove Background from Image

## Primary Method: Local rembg

Use Python with the locally installed rembg library:

1. Read the input image as bytes
2. Call `remove()` from rembg
3. Save the output bytes as PNG

Example:
\`\`\`bash
python3 -c "
from rembg import remove
input_path = '$INPUT_PATH'
output_path = '$OUTPUT_PATH'
with open(input_path, 'rb') as f:
    output = remove(f.read())
with open(output_path, 'wb') as f:
    f.write(output)
print(f'Saved to: {output_path}')
"
\`\`\`

## Fallback: Replicate API

Only if local method fails, use Replicate with proper data URL handling...
```

## Test Case

Use this image to verify the fix works:
```
/Users/georgelane/Dropbox/Projects/thames_boilers_2026/user images/gas-safe-circle.png
```

Expected output should be a PNG with:
- RGBA mode (alpha channel)
- Transparent background (84,000+ transparent pixels)

## Files Created During Debug

- Working output: `/Users/georgelane/Dropbox/Projects/thames_boilers_2026/user images/gas-safe-circle_no_bg.png`
- Model cache: `~/.u2net/u2net.onnx` (176MB)

## Summary of Changes Needed

1. Update `SKILL.md` to use local `rembg` as primary method
2. Remove or fix any code that truncates data URLs
3. Add proper error handling for missing dependencies
4. Test with the Gas Safe logo image

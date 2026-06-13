---
name: servicem8-form-builder
description: Create professional DOCX templates for ServiceM8 forms with full customisation. Supports iterative refinement through parameterised generation - adjust style, density, orientation, and layout without rewriting code.
---

# ServiceM8 Form Template Builder

Create professional DOCX templates for ServiceM8 forms with full customisation and iterative refinement.

## Quick Start

\`\`\`bash
python3 scripts/generate_form.py \\
  --sm8f "form.sm8f" \\
  --company "Company Name" \\
  --logo "logo.png" \\
  --primary "#004aad" \\
  --style bold_trade \\
  --layout compact \\
  --density tight \\
  --repeat-fields grid \\
  --orientation portrait \\
  --output template.docx
\`\`\`

## Parameters

| Parameter | Options | Default | Description |
|-----------|---------|---------|-------------|
| \`--sm8f\` | path | required | Path to SM8F form file |
| \`--company\` | string | required | Company name for footer |
| \`--logo\` | path | optional | Logo image (PNG/JPG) |
| \`--primary\` | hex color | #004aad | Primary brand color |
| \`--style\` | classic, bold_trade, modern_corporate, minimal | bold_trade | Visual styling |
| \`--layout\` | compact, expanded | compact | Overall space usage |
| \`--density\` | tight, normal, spacious | tight | Font/row/margin sizing |
| \`--repeat-fields\` | grid, stacked | grid | How repeating fields display |
| \`--orientation\` | portrait, landscape | portrait | Page orientation |
| \`--font-size\` | integer | auto | Override base font (pt) |
| \`--output\` | path | required | Output DOCX path |

## Iterating on Templates

Adjust parameters to refine output without rewriting code:

\`\`\`bash
# Too cramped? Increase density
--density normal

# Need more columns? Switch to landscape
--orientation landscape

# Repeating fields hard to read? Try stacked
--repeat-fields stacked

# Want larger text? Override font
--font-size 9
\`\`\`

## Density Settings

| Density | Font Size | Row Height | Margins | Best For |
|---------|-----------|------------|---------|----------|
| tight | 7pt | 14pt | 0.3" | Compliance forms, one-page layouts |
| normal | 8pt | 18pt | 0.5" | Standard forms, good readability |
| spacious | 9pt | 24pt | 0.75" | Simple forms, large print |

## Style Options

**classic** - Clean and traditional, thin accent lines, generous whitespace

**bold_trade** - Strong colored header bands, high contrast (recommended for trade businesses)

**modern_corporate** - Logo in banner, colored labels, dark dividers

**minimal** - Maximum whitespace, typography-focused

## Repeating Fields

The generator automatically detects numbered repeating fields (e.g., "Appliance 1", "Appliance 2") and displays them based on \`--repeat-fields\`:

### Grid Mode (Default)
Compact table with all instances in rows:

| # | LOCATION | TYPE | MAKE | MODEL | CLASS |
|---|----------|------|------|-------|-------|
| 1 | «loc_1» | «type_1» | «make_1» | «model_1» | «class_1» |
| 2 | «loc_2» | «type_2» | «make_2» | «model_2» | «class_2» |
| 3 | «loc_3» | «type_3» | «make_3» | «model_3» | «class_3» |
| 4 | «loc_4» | «type_4» | «make_4» | «model_4» | «class_4» |

### Stacked Mode
Each instance as a separate section (takes more space):

\`\`\`
=== APPLIANCE 1 ===
Location: «loc_1»
Type: «type_1»
...

=== APPLIANCE 2 ===
Location: «loc_2»
...
\`\`\`

**Use grid mode** for one-page compliance forms. Use stacked for forms with fewer repeats or more space.

## Understanding Form Complexity

### Simple Forms (Auto-Generate)
- Job completion reports
- Basic service records
- Inspection checklists
- Quote/invoice layouts
- Customer feedback forms

**Use the generator script for these.**

### Complex Compliance Forms (May Need Hand-Crafting)
- Gas Service Certificates with Pass/Fail/N/A tables
- Electrical Installation Certificates
- Landlord Gas Safety Records (CP12)
- Fire safety certificates

**These MAY require manual template creation** if they need:
- Multi-column check tables (Pass/Fail/N/A pattern)
- Precise regulatory formatting
- Industry-specific logos (Gas Safe, NICEIC)

## Complex Form Techniques

### Pass/Fail/N/A Check Tables

ServiceM8 displays checkmarks (✓) for matching values. The SAME merge field appears in each column:

| Check Item | PASS | FAIL | N/A |
|------------|------|------|-----|
| Burner | «form_burner» | «form_burner» | «form_burner» |

ServiceM8 shows ✓ in the column matching the selected value.

### One-Page Layouts

To fit everything on one page:
- Use \`--density tight\` (7pt fonts, minimal margins)
- Use \`--repeat-fields grid\` for compact tables
- Use \`--orientation landscape\` if needed for wide tables
- Consider \`--font-size 6\` for extreme cases

### Conditional Fields

ServiceM8 handles conditional logic in the app. The template includes ALL possible fields - ServiceM8 hides irrelevant ones when rendering the PDF.

## Merge Field Reference

See \`references/merge-fields.md\` for complete documentation.

### Common System Fields
\`\`\`
vendor.name              - Your company name
location.line1           - Your address line 1
location.line2           - Your address line 2
location.state           - Your city/town
location.post_code       - Your postcode
location.phone_1         - Your phone number

job.generated_job_id     - Job number
job.contact_first        - Client first name
job.contact_last         - Client last name
job.job_address          - Site address (multi-line)
job.company_name         - Client company name
job.billing_address      - Client billing address

staff.full_name          - Assigned staff name
calculation.todays_date  - Current date
\`\`\`

### Form Fields
Convert field label to snake_case with \`form_\` prefix:
- "Work carried out?" → \`form_work_carried_out\`
- "Appliance Location 1" → \`form_appliance_location_1\`
- "Gas Safe Card Number" → \`form_gas_safe_card_number\`

## Workflow

### Step 1: Extract and Assess

\`\`\`bash
unzip form.sm8f -d form_contents
cat form_contents/form.json | python3 -m json.tool
\`\`\`

Check for:
- Number of fields
- Repeating field groups (numbered fields)
- Field types (Text, Multiple Choice, Signature, etc.)
- Conditional logic in \`field_data_json\`

### Step 2: Generate Initial Template

\`\`\`bash
python3 scripts/generate_form.py \\
  --sm8f "form.sm8f" \\
  --company "My Company" \\
  --logo "logo.png" \\
  --primary "#004aad" \\
  --output "template_v1.docx"
\`\`\`

### Step 3: Review and Iterate

Open the DOCX, check layout, then adjust parameters:

\`\`\`bash
# Try landscape if too cramped
python3 scripts/generate_form.py \\
  --sm8f "form.sm8f" \\
  --company "My Company" \\
  --orientation landscape \\
  --output "template_v2.docx"
\`\`\`

### Step 4: Upload to ServiceM8

1. Go to Settings → Form Templates
2. Select the form
3. Upload the DOCX as the template
4. Test by completing the form and generating PDF

## File Structure

\`\`\`
servicem8-form-builder/
├── SKILL.md                    # This file
├── scripts/
│   └── generate_form.py        # Main generator script
├── references/
│   └── merge-fields.md         # ServiceM8 field reference
└── templates/                  # Industry template library (future)
\`\`\`

## Best Practices

1. **Always extract the SM8F first** - Understand the form structure before generating
2. **Start with defaults** - Generate once, then iterate with parameter changes
3. **Use grid mode for compliance forms** - Fits more data on one page
4. **Test with real data** - Generate a test PDF in ServiceM8 to verify layout
5. **Keep compliance forms accurate** - Don't modify regulated certificate formats
6. **Consider mobile completion** - Engineers fill forms on phones/tablets

# ServiceM8 Merge Fields Reference

## Vendor Fields (Your Company)

| Merge Field | Description |
|-------------|-------------|
| `vendor.name` | Your company name |
| `vendor.abn` | Business number |
| `vendor.phone` | Phone number |
| `vendor.email` | Email address |

## Location Fields (Your Business Address)

| Merge Field | Description |
|-------------|-------------|
| `location.line1` | Address line 1 |
| `location.line2` | Address line 2 |
| `location.line3` | Address line 3 (city/suburb) |
| `location.state` | State/county |
| `location.post_code` | Postcode/ZIP |
| `location.phone_1` | Business phone |

## Job Fields

| Merge Field | Description |
|-------------|-------------|
| `job.generated_job_id` | Job number (e.g., "J-12345") |
| `job.company_name` | Client/company name |
| `job.job_address` | Full address (multi-line) |
| `job.job_address_singleline` | Address on single line |
| `job.job_description` | Job description |
| `job.work_done_description` | Work completed description |
| `job.status` | Current job status |
| `job.total_invoice` | Invoice total |

## Date/Time Fields

| Merge Field | Description |
|-------------|-------------|
| `calculation.todays_date` | Today's date (short format) |
| `calculation.todays_date_extended` | Today's date (long format) |
| `calculation.time_now` | Current time |

## Company Fields

| Merge Field | Description |
|-------------|-------------|
| `company.name` | Your company name |
| `company.abn` | Business number |
| `company.phone` | Phone number |
| `company.email` | Email address |
| `company.address` | Business address |

## Client Fields

| Merge Field | Description |
|-------------|-------------|
| `client.name` | Client name |
| `client.email` | Client email |
| `client.phone` | Client phone |
| `client.mobile` | Client mobile |
| `client.address` | Client address |

## Form Fields

Form fields are generated from field labels using this conversion:

1. Convert to lowercase
2. Remove special characters (?, !, etc.)
3. Replace spaces with underscores
4. Add `form_` prefix

### Examples

| Field Label | Merge Field Name |
|-------------|------------------|
| Work carried out? | `form_work_carried_out` |
| Materials Used | `form_materials_used` |
| Customer Name | `form_customer_name` |
| Before Photo | `form_before_photo` |
| Customer Signature | `form_customer_signature` |

### Field Type Suffixes

Photos and signatures may use suffixes:
- Photos: `form_fieldname_photo` or `form_fieldname_photo_1`, `form_fieldname_photo_2`
- Signatures: `form_fieldname_signature`

## Staff Fields

| Merge Field | Description |
|-------------|-------------|
| `staff.first` | Staff first name |
| `staff.last` | Staff last name |
| `staff.email` | Staff email |
| `staff.mobile` | Staff mobile |

## Notes

- Merge fields are case-sensitive
- Use Word's MERGEFIELD syntax: `{ MERGEFIELD field_name \* MERGEFORMAT }`
- Photo fields will be replaced with actual images
- Signature fields will be replaced with signature images

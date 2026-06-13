---
name: "source-command-google-ads"
description: "Manage Google Ads campaigns - setup, create, report, optimize"
---

# source-command-google-ads

Use this skill when the user asks to run the migrated source command `google-ads`.

## Command Template

# Google Ads Campaign Management

Route to the appropriate subcommand based on user intent.

## Available Subcommands

- `/google-ads-setup` - Configure credentials and business settings
- `/google-ads-create` - Create new campaigns with keyword research
- `/google-ads-report` - Generate performance reports
- `/google-ads-optimize` - Get optimization suggestions

## Usage

When user runs `/google-ads`:
1. If they specify a subcommand (e.g., `/google-ads setup`), invoke that command
2. If no subcommand, ask what they want to do:
   - **Setup**: Configure credentials, test connection, create business config
   - **Create**: Research keywords, generate ad copy, build campaigns
   - **Report**: View performance metrics and analysis
   - **Optimize**: Get recommendations to improve performance

## Context Preservation

This skill uses subagent delegation to preserve context:
- Large datasets (keywords, reports) are written to JSON files
- Subagents return summaries, not full data
- File paths are provided for detailed review if needed

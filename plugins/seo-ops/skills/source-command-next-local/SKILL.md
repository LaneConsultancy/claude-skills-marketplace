---
name: "source-command-next-local"
description: "Set up SEO-optimised Next.js project with ShadCN for local service pages"
---

# source-command-next-local

Use this skill when the user asks to run the migrated source command `next-local`.

## Command Template

Set up a Next.js project using the latest stable version with the App Router, ShadCN UI, and Tailwind CSS, optimised for SEO and Google crawlability.

Before starting, check the current Next.js documentation for the latest recommended patterns for static generation and metadata.

## Requirements

- Use Server Components by default (no "use client" unless necessary for interactivity)
- Configure static generation (SSG) for all pages using the current recommended approach for pre-rendering at build time
- Set up the Metadata API (or current equivalent) with a reusable pattern for title, description, and Open Graph tags
- Auto-generate a sitemap using Next.js's built-in approach
- Configure robots.txt to allow all crawlers
- Use semantic HTML (proper heading hierarchy, landmark elements)
- Include a basic layout with header, main content area, and footer
- Add ShadCN components: Button, Card, and Navigation Menu

## Project Structure

Set up the project with a clean structure that supports dynamic routing with `[slug]` pages. Do NOT add any example content, placeholder text, or demo pages - just the bare infrastructure.

Explain any version-specific decisions you make.

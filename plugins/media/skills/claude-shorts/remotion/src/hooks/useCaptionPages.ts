import { useMemo } from "react";
import type { Caption } from "../types";

type Token = { text: string; fromMs: number; toMs: number };
type Page = { text: string; startMs: number; durationMs: number; tokens: Token[] };

const MAX_TOKENS_PER_PAGE = 4;

/**
 * Group word/phrase-level captions into readable shortform pages.
 *
 * For continuous speech with no inter-word silence, the upstream
 * `createTikTokStyleCaptions` collapsed everything into one massive page.
 * Instead we cap pages at MAX_TOKENS_PER_PAGE so captions stay readable.
 *
 * The combineMs argument is preserved for API compatibility but acts only as
 * an additional split signal — a gap larger than combineMs forces a new page
 * even before reaching the per-page cap.
 */
export const useCaptionPages = (
  captions: Caption[],
  combineMs: number = 800
) => {
  return useMemo<Page[]>(() => {
    if (!captions || captions.length === 0) return [];

    const pages: Page[] = [];
    let buf: Token[] = [];

    const flush = () => {
      if (buf.length === 0) return;
      const startMs = buf[0].fromMs;
      const endMs = buf[buf.length - 1].toMs;
      pages.push({
        text: buf.map((t) => t.text).join(" "),
        startMs,
        durationMs: Math.max(endMs - startMs, 1),
        tokens: buf,
      });
      buf = [];
    };

    for (let i = 0; i < captions.length; i++) {
      const c = captions[i];
      const token: Token = {
        text: c.text,
        fromMs: c.startMs,
        toMs: c.endMs,
      };

      if (buf.length > 0) {
        const prev = buf[buf.length - 1];
        const gap = token.fromMs - prev.toMs;
        if (gap > combineMs) {
          flush();
        }
      }

      buf.push(token);
      if (buf.length >= MAX_TOKENS_PER_PAGE) {
        flush();
      }
    }
    flush();

    return pages;
  }, [captions, combineMs]);
};

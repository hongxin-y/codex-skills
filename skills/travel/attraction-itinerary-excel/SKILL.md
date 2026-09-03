---
name: attraction-itinerary-excel
description: Extract every attraction and place from itinerary screenshots or documents, verify ticket requirements, prices, and opening hours online, and produce a complete date-based Excel table with RMB estimates and source links.
---

# Attraction Itinerary Excel

Use this skill when the user provides a travel itinerary image/document and asks for a researched Excel list of attractions, tickets, prices, opening hours, or booking links.

## Workflow

1. Read the source image/document carefully and create a locked source manifest before researching anything. Transcribe every numbered item in order, with its original date, wording, and grouping. This manifest is the sole authority for row inclusion: the Excel must contain exactly the same items as the user input—no additions, deletions, substitutions, inferred stops, route-based recommendations, or itinerary expansions. Preserve repeated items (for example, a hotel listed twice) as repeated source entries when they occur. If the source combines two places in one numbered item, keep them in one row unless the user explicitly asks to split them; if the source lists them separately, do not merge them. Treat hotels, restaurants, cafés, streets, squares, bridges, parks, viewpoints, churches, museums, tours, and transport notes as rows only when they are explicitly present. Do not silently drop non-ticket places; mark them as free or not applicable.
2. Reconcile names and spellings using map searches and official websites. Keep both the source-language name and a concise Chinese label where useful. If an item is ambiguous, record the uncertainty in `备注` and retain the original text.
3. Research each row online. Prefer the venue's official ticket and visitor-information pages; use an official tourism or municipal page when no venue site exists. Capture the URL in the workbook. Distinguish free public access from paid interior areas, guided tours, cruises, special events, and restaurant minimum spend.
4. Record current/seasonal adult prices and opening hours. For multiple ticket variants, put the meaningful variants in the same row's `成人票价（参考）` and `票种/说明` cells. Never present an estimate as a guaranteed current price; label approximate, seasonal, or schedule-dependent values.
5. Add a `人民币折算（约）` column. Use one clearly stated reference rate for each currency (for example, HUF and EUR), round to practical whole RMB, and add the rate/estimate caveat in a note or `备注`. Free entries are `¥0`; restaurants, hotels, and places without admission tickets are `不适用`.
6. Create one worksheet containing these columns in this order: `日期`, `景点/地点`, `是否需要购票`, `成人票价（参考）`, `人民币折算（约）`, `票种/说明`, `开放时间（参考）`, `购票/官网`, `备注`.
7. Use the spreadsheet skill and `@oai/artifact-tool` for authoring. Add a formatted table, freeze the header row, wrap long text, set readable widths, and keep plain-text URLs in the source column. Save the final `.xlsx` under the conversation's `outputs` directory.
8. Verify exact fidelity in both directions: every source item has exactly one corresponding Excel row (including explicit duplicates), and every Excel row can be traced back to a source item. Report any mismatch and stop before export until resolved. Check that no location is missing, added, renamed into a different place, or accidentally split/merged. Inspect key ranges, scan for formula errors, render the sheet once, and fix clipped headers or unreadable rows before delivery.

## Output expectations

- Report the number of source items/rows and call out any ambiguous transcription.
- State the exact source-item count and Excel-row count; they must match unless the user explicitly requested a split or merge.
- Include official booking links where tickets are required; use a map or official tourism link for free public places when practical.
- Keep research caveats visible in the workbook rather than hiding them in chat.

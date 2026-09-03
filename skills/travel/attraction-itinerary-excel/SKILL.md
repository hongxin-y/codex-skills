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

## Search and verification method

- Search each place in at least two forms: an English name plus `official tickets`/`opening hours`, and the local-language name plus the local terms for tickets and opening hours (for example, Hungarian `jegyárak`, `jegyvásárlás`, and `nyitvatartás`). Use the venue name, city, and year when prices may be seasonal.
- Prefer the attraction's own official domain. If a page redirects, fails, or is an old subdomain, follow the official site's ticket link and record the final working ticket domain. Do not retain a URL merely because it appeared in a search result. Check the final URL with a direct request or browser page load when possible.
- Use search-engine snippets only to discover candidate pages, never as the sole evidence for a price or policy. When Google is blocked or challenged, use DuckDuckGo HTML search or another accessible search engine, then open and inspect the official result. Record the official page URL in the workbook rather than the search URL.
- For each paid place, explicitly test whether the ticket is online, on-site only, or both. Record operational constraints such as card-only payment, a physical ticket office, timed entry, language/date selection, CAPTCHA, visitor-center sales, or limited same-day leftovers.
- Treat release timing as a separate fact from ticket availability. Look for wording such as `advance`, `available from`, `calendar`, `release`, and local equivalents. If the official source does not publish a fixed release day or advance window, write `未公布固定放票规则；按官方日历滚动开放` rather than inventing a date. Use third-party claims only as a clearly labelled practical tip, not as an official rule.
- Cross-check prices and hours against the date in the itinerary. Prefer the official price page, ticket page, or visitor-information page; if the official page is dynamic or protected by CAPTCHA, retain the official URL and state the verification limitation in `备注`. For a seasonal venue, calculate the applicable season from the itinerary date and preserve both the season rule and the date-specific conclusion.
- When a result conflicts with the workbook, update every affected field together: `成人票价（参考）`, `人民币折算（约）`, `票种/说明`, `开放时间（参考）`, `购票/官网`, and the booking/onsite notes. Never leave an old URL or old price in a parallel column.

## Restaurant reservation handling

- Every restaurant, café, or food venue listed in the source must receive a reservation check, even when no admission ticket is involved. Search the official site for `reservation`, `book a table`, `table reservation`, `asztalfoglalás`, and `foglalás`, and inspect the venue's official contact page and social profile when linked from the official site.
- Record the actual reservation channel, not just the restaurant homepage: use the official online booking URL when a working form or booking widget exists. Verify that the page loads and that the booking flow reaches date/time/party-size selection when possible.
- If no reliable online reservation page exists, look for an official email address, telephone number, contact form, or stated walk-in policy. Put the exact email/phone and the conclusion in `备注` or `线下办理/注意事项`, for example: `无在线订位表单；请发邮件至 … 或致电 …` or `官网写明无需预约，可直接到店`.
- Distinguish among `在线可预约`, `仅邮件/电话预约`, `无需预约（可直接到店）`, and `预约入口存在但当前无法稳定使用`. Do not label a restaurant as requiring reservation solely because third-party reviews recommend it.
- If an official reservation page is listed in search results but cannot be opened or submitted, keep it as a secondary reference only, mark the limitation, and provide the verified contact method instead. Do not invent a booking URL or treat a generic map link as an online reservation channel.
- Preserve practical details such as opening hours, response expectations, walk-in queues, minimum spend, deposits, cancellation rules, and language limitations when they are stated by the venue. If the user asks to contact the restaurant, draft the message using the verified email/phone and the itinerary date, leaving unknown party size, time, and guest name as explicit placeholders.

## Output expectations

- Report the number of source items/rows and call out any ambiguous transcription.
- State the exact source-item count and Excel-row count; they must match unless the user explicitly requested a split or merge.
- Include official booking links where tickets are required; use a map or official tourism link for free public places when practical.
- Keep research caveats visible in the workbook rather than hiding them in chat.

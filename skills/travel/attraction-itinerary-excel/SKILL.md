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

## Date assignment when the source omits dates

- Treat dates explicitly supplied by the user as locked. Never move an item with an explicit date without recording the reason and preserving the original date in `原文条目` or `备注`.
- If the source gives a trip window but does not assign every place to a day, assign dates before researching prices. Cluster nearby places geographically, then fit the clusters to opening hours, reservation windows, realistic visit duration, cross-city travel time, and fixed arrival/departure times.
- Keep the original source order in `原文条目`; use `日期` plus `交通/规划` for the recommended day and visit sequence. Do not create extra attractions to fill a day.
- Put the assignment rationale in `备注`, for example: `日期为建议分配：与同区域景点步行串联；受16:45离开时间约束`. Mark uncertain assignments as `建议日期，需用户确认` rather than presenting them as user-provided facts.
- Recheck capacity after assignment: no day may exceed the available sightseeing hours, venue opening hours, reservation times, or required transfer buffer. For a day with a fixed departure, work backward from the departure point and include a conservative arrival buffer.
- Verify that every source item has one date after assignment and that the date distribution is reflected consistently in any map or route output.

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

## Dress-code and visitor-etiquette handling

- Check dress-code requirements for every source item, including attractions, religious buildings, museums, government buildings, theatres, cruises, restaurants, cafés, hotels, bridges, parks, streets, and transport points. Do not limit this check to ticketed attractions.
- Search official visitor rules, code-of-conduct, FAQ, ticket, and visitor-information pages using terms such as `dress code`, `appropriate clothing`, `attire`, `clothing`, `visitor rules`, and local-language equivalents. For religious venues, also search for shoulder/knee coverage and worship etiquette.
- Classify the result explicitly as `有明确要求`, `有宗教场所礼仪要求`, `有正式参观要求`, `建议整洁/优雅，无严格要求`, or `未发现特殊要求`. Never convert a general travel blog recommendation into a mandatory rule.
- For an official rule, preserve the actionable details: who it applies to, required coverage or garment length, prohibited attire, whether entry can be refused, and whether the rule applies to worship services, tours, performances, or only certain areas.
- For restaurants and cafés, search for an official dress-code statement separately from reservation information. If none exists, write `未发现官方 dress code` and give a modest context-based suggestion only when useful (for example, `smart casual` for fine dining or a hotel café). Do not invent a formal requirement.
- For outdoor, public, bridge, park, street, or transport entries, record `无特殊要求` unless an event or venue rule states otherwise; practical weather, footwear, sun, or safety advice belongs in the note, not in the mandatory requirement field.
- If no official dress-code page is found, distinguish `未发现官方要求` from `确认无需特殊着装`. Cite the page used for the check when available and keep uncertainty visible in `备注` or `着装核验备注`.
- Add dedicated workbook columns `着装要求` and `着装核验备注` when the user asks for attire guidance. Keep one row per source item and update both columns consistently if later research changes the conclusion.

## Output expectations

- Report the number of source items/rows and call out any ambiguous transcription.
- State the exact source-item count and Excel-row count; they must match unless the user explicitly requested a split or merge.
- Include official booking links where tickets are required; use a map or official tourism link for free public places when practical.
- Keep research caveats visible in the workbook rather than hiding them in chat.

## Map deliverable verification

- When maps are part of the deliverable, perform post-export visual QA on every PNG, not just the Excel workbook: inspect the full geographic extent, all numbered points, arrow direction, legend, and image boundaries.
- Confirm that the legend is outside the map viewport and does not hide route points or roads; confirm that no tile is blank, blocked, or an HTTP error placeholder.
- Keep the map route order, segment modes, and distances consistent with the Excel `交通/规划` and `备注` cells. Regenerate any map that fails these checks before delivery.

## Route planning fields

- When the request includes a map or itinerary route, add route-planning details to the relevant `交通/规划` or `备注` cells: recommended order, segment distance, mode, and operator/source link.
- Apply the same practical threshold used by the map skill: segments up to and including 3 km are walking; segments over 3 km require a public-transport search and an explicit mode (metro, tram, bus, train, or shuttle).
- Keep the Excel route details consistent with the map legend. If the map labels a segment as public transport, the workbook must name the same mode and preserve any ticket or timetable caveat.

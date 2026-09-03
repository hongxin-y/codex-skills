---
name: map-itinerary-visualizer
description: Search itinerary places on map services, plan daily visit order, and generate clear date-specific map images with adaptive markers, arrows, and legends.
---

# Map Itinerary Visualizer

Use this skill when the user asks to locate itinerary places on Google Maps or another map service, compare spatial planning, or create map screenshots/route illustrations.

## Workflow

1. Transcribe every source item and preserve its date and original order. Keep restaurants, hotels, viewpoints, streets, bridges, parks, and attractions as distinct points when the source lists them separately. Do not add invented stops.
2. Resolve each place to a specific map location. Prefer the requested map service and use its visible map/search result when available. Keep a direct search URL for every point. If the requested browser/map surface is unavailable, state that limitation and use a clearly labeled fallback only when it still provides reliable coordinates; never present a schematic fallback as a map screenshot.
3. Group points by date and evaluate order using geography, opening times, reservation times, crossing/transport constraints, and the user's original sequence. Explain any reordered stop and distinguish a list number from a recommended visit sequence.
4. Capture a real map screenshot for each date at a useful zoom. Use a closer crop or higher zoom for dense city centers; choose a wider view only when a day's points are geographically spread out.
5. Draw route arrows from point to point in the chosen order. Use large, fully visible numbered markers for isolated points and adaptive smaller markers for nearby points. When points overlap, reduce marker radius, stroke width, and marker-number font; do not let a two-digit number clip.
6. Keep the map visually legible: put long place names in a separate side legend keyed by number instead of writing every name beside crowded markers. Preserve a readable title with the date, a day color, and a legend. Avoid covering important map labels where possible.
7. Produce one PNG per date plus, when useful, a combined overview. Inspect every output at normal size and revise if markers, arrows, labels, or two-digit numbers overlap or clip. Deliver direct links to all images and summarize route assumptions.

## Visual quality rules

- The underlying map must be identifiable as the requested map service; a hand-drawn or schematic map is only a fallback and must be labeled as such.
- Map markers should be anchored close to the actual location. If two locations are nearly coincident, use smaller markers and rely on the numbered legend rather than forcing large text into the map.
- Arrows should terminate before marker edges, remain visible over the map, and follow the displayed order.
- A clear legend is preferable to dense labels. Keep legend text at a readable size even when map markers shrink.

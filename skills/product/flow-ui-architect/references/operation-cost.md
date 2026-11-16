# Operation-cost analysis

Use P/K/D/C/W/E/M to compare complete task routes.

| Lens | Meaning |
| --- | --- |
| P | Pointing and pointer travel |
| K | Keyboard and text input |
| D | Decisions and ambiguity |
| C | Context switching |
| W | Waiting and blocking latency |
| E | Error recovery |
| M | Memory burden |

## Operation count

When a route is concrete, count the meaningful interactions required to reach the same outcome: pointer activation, text entry, selection, navigation and conditional confirmation. Note whether the count is a design estimate or observed measurement.

A click count alone is not an experience score. More steps can be justified by reduced error risk, clearer choices or safer authorization.

Do not invent universal click targets or weighted scores.

## Before/after route

Describe the current and proposed paths from the same starting state to the same completed outcome.

Example:

| Lens | Fragmented flow | Workbench flow |
| --- | --- | --- |
| P | Repeated navigation | Actions near record |
| K | Re-enter search | Query persists |
| D | Ambiguous controls | State-specific actions |
| C | List replaced by detail | List remains visible |
| W | Full reload | Targeted update |
| E | Form resets on failure | Input retained |
| M | Remember next record | Next eligible item available |

## Tradeoffs

A confirmation may increase interactions while lowering error cost. A dedicated page may add navigation while improving complex review. Evaluate the whole route and severity of failure.

Choose the outcome before optimizing its cost. More time may support informed comparison or enjoyable creation; fewer actions may remove desired control. Do not use completion speed, conversion or engagement duration alone as proof of user benefit. Relate any metric to the page's intent and actual evidence.

## Validation

Use real task success, time, error, backtracking and recovery data when available. Otherwise describe qualitative hypotheses and mark numerical estimates as unverified.

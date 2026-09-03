---
name: disk-space-diagnosis
description: "Analyze Windows disk usage, explain what large items are used for, classify what can be cleaned and how, and propose lower-risk optimization paths without deleting or changing anything by default. Use for requests to find why a drive is filling up or what can be safely cleaned."
---

# Disk Space Diagnosis

Analyze Windows storage pressure as a read-only investigation. The default deliverable is an evidence-based attribution report, not a cleanup operation.

## Safety and authorization

- Never delete, move, compress, resize, disable, or modify files, services, registry values, storage settings, or application data during diagnosis.
- Treat any automatic or dynamic allocation change as **high risk** and require a fresh, explicit user confirmation immediately before execution. This includes changing pagefile automatic management or size/location, hibernation or fast-startup state, system-restore/shadow-copy limits, storage quotas, virtual disks, and other system-managed allocations.
- A general request such as "clean up space" is not permission to mutate. Before any cleanup, identify exact paths, estimated reclaimable space, what may be lost, and whether an application or reboot is required; ask for confirmation of that exact action.
- Do not recommend direct deletion of system directories or system-managed files such as `Windows\Installer`, `WinSxS`, `pagefile.sys`, `hiberfil.sys`, or `swapfile.sys`. Prefer supported Windows settings, application cleanup, uninstallers, or vendor tools.
- Preserve user data and privacy. Do not open file contents unless needed to identify a file type; report paths, sizes, timestamps, and metadata only.

## Investigation workflow

1. Establish the target volume(s): capacity, used space, free space, and free percentage. If the user did not name a drive, ask or use the drive implicated by the complaint; do not scan unrelated volumes unnecessarily.
2. Measure top-level directories and large files with read-only filesystem queries. Exclude reparse points/junctions where possible to avoid double-counting; note inaccessible paths and scan limitations.
3. Attribute space by category:
   - user data: documents, downloads, media, game saves, project files;
   - application data: caches, logs, browser profiles, package stores, chat attachments;
   - developer/tooling data: package caches, build caches, virtual environments, container/VM images;
   - Windows maintenance: update downloads, temp files, installer caches, component store;
   - system-managed allocations: pagefile, hibernation file, crash dumps, restore points/shadow copies;
   - duplicated or stale installers, archives, backups, and game libraries.
4. For system-managed allocations, query configuration and actual usage separately. On Windows, use CIM/WMI classes such as `Win32_PageFileUsage`, `Win32_PageFileSetting`, and `Win32_ComputerSystem`; distinguish allocated size from current/peak use. Do not infer that a large allocation is currently consuming the same amount of active memory.
5. If the user has a prior scan, compare the same paths and report deltas. Distinguish true growth from measurement differences, junction double-counting, and files that were removed or moved.
6. Identify the purpose of every material finding, not just its size. Use path components, extensions, timestamps, known application ownership, read-only metadata, and (when available) installed-app or service associations. Do not claim a purpose with high confidence from a folder name alone; label it inferred or unknown when evidence is weak.
7. Classify each finding by content type (user data, application data, cache, log, installer/update payload, build/package cache, system file, or unknown), supported handling, reversibility, and risk. System-managed and automatic allocations are always **high risk / confirmation required**.
8. For each large item, explain why it may be large or growing, what functionality depends on it, what happens after cleanup, and the supported cleanup method. Prefer an application's own storage/cache controls, Windows Storage/Disk Cleanup, an uninstaller, or a vendor tool over manual deletion. Never turn "cache" into an unconditional delete recommendation: verify whether it contains downloads, offline data, thumbnails, shader caches, logs, or user-created content.
9. If the largest items are not suitable for deletion, produce an optimization plan from the remaining candidates. Select a combination of actions by expected reclaimable space, risk, reversibility, and user impact; show the estimated total range and which items would need the user's confirmation. Include non-deletion options such as moving user libraries or game libraries using supported app settings, changing download/cache locations, uninstalling unused software, reducing retention, or adjusting system allocations. Moving or changing locations is a mutation and still requires exact-target confirmation.
10. Rank findings by likely reclaimable space, confidence, reversibility, and user impact. State when a folder is a cache that can regenerate, when it may contain user content, and when only an application or Windows-supported workflow should be used.

## Commands and collection guidance

Use PowerShell or equivalent read-only commands. Prefer `Get-PSDrive`, `Get-ChildItem`, `Measure-Object`, and CIM queries. Avoid broad recursive scans when a targeted scan is enough, and handle access-denied errors without retry loops. For large-file reports include full path, size in GB/MB, and last-write time. For folder totals, make the counting method clear and warn that protected or linked content may be omitted.

For purpose attribution, use read-only evidence where practical: file extensions and names, parent/child structure, last-write patterns, installed application metadata, service/process names, and Windows ownership signals. Do not execute unknown binaries, inspect private message contents, or assume that a vendor-named folder is disposable. Read [references/decision-guide.md](references/decision-guide.md) when interpreting common Windows/application paths or when the user asks for an optimization plan.

Useful Windows-specific checks include:

```powershell
Get-PSDrive -PSProvider FileSystem
Get-CimInstance Win32_PageFileUsage
Get-CimInstance Win32_PageFileSetting
Get-CimInstance Win32_ComputerSystem | Select-Object AutomaticManagedPagefile
```

These checks are diagnostic only. Any command that sets CIM properties, edits the registry, invokes cleanup, or removes files is a mutation and must not run until the user confirms the exact proposed change.

## Report format

Lead with the result: total capacity, used/free space, and the main causes. Then provide a compact table with:

`Priority | Location | Size | What it is/does | Why it grew | Reclaimable estimate | Supported handling | Risk`

For every high-impact item, include a short explanation covering its dependency and likely consequence of cleanup. Do not merely repeat the path and size.

Separate:

- safe-to-review candidates (reversible caches or stale downloads, still requiring exact-target confirmation before deletion);
- application-owned data that must be cleaned inside the application or backed up first;
- system-managed or automatic allocations, explicitly labeled **high risk / confirmation required**;
- items that should not be touched directly.

If the biggest item is not a viable cleanup target, add a section named `Optimization when the biggest items stay` and list a practical combination of smaller candidates, supported relocation/retention options, estimated total savings, and the confirmation required for each mutation. Make clear which savings are one-time and which prevent future growth.

When proposing action, give an estimated reclaimable range rather than promising an exact result. If no mutation was authorized, explicitly say that nothing was changed. If a requested mutation cannot run because elevation or a reboot is required, report that as a blocker and provide the supported manual path.
